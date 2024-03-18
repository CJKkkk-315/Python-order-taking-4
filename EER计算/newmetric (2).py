
import numpy as np
from numpy.linalg import eig
import pandas as pd
from scipy.linalg import sqrtm
from sklearn.metrics import roc_curve, auc
from scipy.spatial.distance import cityblock, mahalanobis, euclidean
import matplotlib.pyplot as plt
data = pd.read_csv("./DSL-StrongPasswordData.csv")

subjects = data["subject"].unique()

def evaluateEER(user_scores, imposter_scores):
    labels = [0]*len(user_scores) + [1]*len(imposter_scores)
    fpr, tpr, thresholds = roc_curve(labels, user_scores + imposter_scores)
    missrates = 1 - tpr
    farates = fpr
    dists = missrates - farates
    idx1 = np.argmin(dists[dists >= 0])
    idx2 = np.argmax(dists[dists < 0])
    x = [missrates[idx1], farates[idx1]]
    y = [missrates[idx2], farates[idx2]]
    a = ( x[0] - x[1] ) / ( y[1] - x[1] - y[0] + x[0] )
    eer = x[0] + a * ( y[0] - x[0] )
    return eer
def evaluatefpr(user_scores, imposter_scores):
    labels = [0]*len(user_scores) + [1]*len(imposter_scores) # 分别计算两个集合的大小
    fpr, tpr, thresholds = roc_curve(labels, user_scores + imposter_scores)
    return fpr
def evaluatetpr(user_scores, imposter_scores):
    labels = [0]*len(user_scores) + [1]*len(imposter_scores) # 分别计算两个集合的大小
    fpr, tpr, thresholds = roc_curve(labels, user_scores + imposter_scores)
    return tpr

def ROCPlot(rst,algorithm_name):
    fpr1 = rst[2][1]
    tpr1 = rst[3][1]
    FT = np.array((fpr1, tpr1)).T
    data = pd.DataFrame(FT)
    roc_auc1 = auc(fpr1, tpr1)
    plt.plot(fpr1, tpr1, 'k--', label='initial keystroke dataset (ROC area = {0:.2f})'.format(roc_auc1), lw=2)
    
    plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，以免和边缘重合，更好的观察图像的整体
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')  # 可以使用中文，但需要导入一些库即字体
    plt.title(algorithm_name)
    plt.legend(loc="lower right")
    plt.show()
"""
class ManhattanScaledDetector:
    
    def __init__(self, subjects):
        
        self.user_scores = []
        self.imposter_scores = []
        self.mean_vector = []
        self.subjects = subjects
        
    def training(self):
        self.mean_vector = self.train.mean().values
        self.mad_vector = self.train.mad().values
        
    def testing(self):
        for i in range(self.test_genuine.shape[0]):
            cur_score = 0
            for j in range(len(self.mean_vector)):
                cur_score = cur_score + \
                            abs(self.test_genuine.iloc[i].values[j] - \
                                self.mean_vector[j]) / self.mad_vector[j]
            self.user_scores.append(cur_score)
            
        for i in range(self.test_imposter.shape[0]):
            cur_score = 0
            for j in range(len(self.mean_vector)):
                cur_score = cur_score + \
                            abs(self.test_imposter.iloc[i].values[j] - \
                                self.mean_vector[j]) / self.mad_vector[j]
            self.imposter_scores.append(cur_score)
    
    def evaluate(self):
        eers = []
        fpr = []
        tpr =[]
        
        for subject in subjects:
            
            self.user_scores = []
            self.imposter_scores = []
    
            # Consider current subject as genuine and rest as imposters
            genuine_user_data = data.loc[data.subject == subject, "H.g":"H.f.3"]
            imposter_data = data.loc[data.subject != subject, :]
    
            # genuine user's first 200 time vectors for training
            self.train = genuine_user_data[:20]
    
            # True set (200 records)
            self.test_genuine = genuine_user_data[20:]
    
            # False set (250 records, 5 per imposter, 50 imposters in all)
            self.test_imposter = imposter_data.groupby("subject").head(1).loc[:, "H.g":"H.f.3"]
            
            self.training()
            
            self.testing()
    
            eers.append(evaluateEER(self.user_scores, self.imposter_scores))
            fpr.append(evaluatefpr(self.user_scores, self.imposter_scores))
            tpr.append(evaluatetpr(self.user_scores, self.imposter_scores))
        
        return np.mean(eers), np.std(eers), fpr, tpr      

result1=ManhattanScaledDetector(subjects).evaluate()
print("ManhattanScaledDetector:")
print(result1[0:2])
ROCPlot(result1,"Manhattan_scaled")


    
class NearestNeighbourMahalanobisDetector:
    
    def __init__(self, subjects):
       
        self.user_scores = []
        self.imposter_scores = []
        self.mean_vector = []
        self.subjects = subjects
        
    def training(self):
        self.covinv = np.linalg.inv(np.cov((self.train).T))        
        
    def testing(self):
        for i in range(self.test_genuine.shape[0]):
            cur_scores = []
            for j in range(self.train.shape[0]):
                diff = self.test_genuine.iloc[i].values - self.train.iloc[j]
                cur_scores.append(np.dot(np.dot(diff.T, self.covinv), diff))
            self.user_scores.append(min(cur_scores))
            
        for i in range(self.test_imposter.shape[0]):
            cur_scores = []
            for j in range(self.train.shape[0]):
                diff = self.test_imposter.iloc[i].values - self.train.iloc[j]
                cur_scores.append(np.dot(np.dot(diff.T, self.covinv), diff))
            self.imposter_scores.append(min(cur_scores))
    
    def evaluate(self):
        eers = []
        fpr = []
        tpr = []
        
        for subject in subjects:
            
            self.user_scores = []
            self.imposter_scores = []
    
            # Consider current subject as genuine and rest as imposters
            genuine_user_data = data.loc[data.subject == subject, "H.period":"H.Return"]
            imposter_data = data.loc[data.subject != subject, :]
    
            # genuine user's first 200 time vectors for training
            self.train = genuine_user_data[:200]
    
            # True set (200 records)
            self.test_genuine = genuine_user_data[200:]
    
            # False set (250 records, 5 per imposter, 50 imposters in all)
            self.test_imposter = imposter_data.groupby("subject").head(5).loc[:, "H.period":"H.Return"]
            
            self.training()
            
            self.testing()
    
            eers.append(evaluateEER(self.user_scores, self.imposter_scores))
            fpr.append(evaluatefpr(self.user_scores, self.imposter_scores))
            tpr.append(evaluatetpr(self.user_scores, self.imposter_scores))
        
        return np.mean(eers), np.std(eers), fpr, tpr        

result2=NearestNeighbourMahalanobisDetector(subjects).evaluate()
print(result2[0:2])
ROCPlot(result2,"NearestNeighbourMahalanobisDetector")
"""
class NearestNeighbourNewMetric:
    
    def __init__(self, subjects):
        
        self.user_scores = []
        self.imposter_scores = []
        self.mean_vector = []
        self.subjects = subjects
        
    def training(self):
        self.mx = np.cov((self.train).T)
        w,v = eig(self.mx)
        diag = np.dot(np.dot(np.linalg.inv(v), self.mx), v)
        diag_sqrt = sqrtm(diag)
        sqr_root = np.dot(np.dot(v, diag_sqrt), np.linalg.inv(v))
        
        self.covinv = np.linalg.inv(sqr_root)     
        self.mean_vector = self.train.mean().values 
    """
    def testing(self):
        for i in range(self.test_genuine.shape[0]):
            cur_scores = []
            for j in range(self.train.shape[0]):
                diff = cityblock((np.dot(self.covinv, self.test_genuine.iloc[i].values)), (np.dot(self.covinv, self.train.iloc[j])))
                cur_scores.append(diff)
            self.user_scores.append(min(cur_scores))
        
        for i in range(self.test_imposter.shape[0]):
            cur_scores = []
            for j in range(self.train.shape[0]):
                diff = cityblock((np.dot(self.covinv, self.test_imposter.iloc[i].values)), (np.dot(self.covinv, self.train.iloc[j])))
                cur_scores.append(diff)
            self.imposter_scores.append(min(cur_scores))
    """
    def testing(self):
        for i in range(self.test_genuine.shape[0]):
            cur_scores = 0
            for j in range(len(self.mean_vector)):
                print(np.dot(self.covinv, self.test_genuine.iloc[i].values).shape)
                cur_scores = cur_scores + \
                             cityblock((np.dot(self.covinv, self.test_genuine.iloc[i].values)), (np.dot(self.covinv, self.mean_vector)))

            self.user_scores.append(cur_scores)
        
        for i in range(self.test_imposter.shape[0]):
            cur_scores = 0
            for j in range(len(self.mean_vector)):
                cur_scores = cur_scores + \
                             cityblock((np.dot(self.covinv, self.test_imposter.iloc[i].values[j])), (np.dot(self.covinv, self.mean_vector[j])))
            self.imposter_scores.append(cur_scores)   

    def evaluate(self):
        eers = []
        fpr = []
        tpr =[]
        
        for subject in subjects:
            
            self.user_scores = []
            self.imposter_scores = []
    
            # Consider current subject as genuine and rest as imposters
            genuine_user_data = data.loc[data.subject == subject, "H.period":]
            imposter_data = data.loc[data.subject != subject, :]
    
            # genuine user's first 200 time vectors for training
            self.train = genuine_user_data[:200]
    
            # True set (200 records)
            self.test_genuine = genuine_user_data[200:]
    
            # False set (250 records, 5 per imposter, 50 imposters in all)
            self.test_imposter = imposter_data.groupby("subject").head(5).loc[:, "H.period":]
            
            self.training()
            
            self.testing()
    
            eers.append(evaluateEER(self.user_scores, self.imposter_scores))
            fpr.append(evaluatefpr(self.user_scores, self.imposter_scores))
            tpr.append(evaluatetpr(self.user_scores, self.imposter_scores))
        
        return np.mean(eers), np.std(eers), fpr, tpr      

result3=NearestNeighbourNewMetric(subjects).evaluate()
print("NewMetric:")
print(result3[0:2])
ROCPlot(result3,"Nearest Neighbour New Metric")

