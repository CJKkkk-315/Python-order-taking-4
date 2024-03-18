df_cluster = df.groupby(["State","City","Year","Month"],as_index=False)["AvgTemperature"].mean()
df_cluster = pd.DataFrame(df_cluster)
df_cluster.rename(columns={'AvgTemperature':'AvgTemperature'}, inplace = True)
df_cluster = df_cluster.pivot(index=["State","City"],columns=["Year","Month"],values="AvgTemperature")
df_cluster.columns = [f"{tt[0]}_{tt[1]}" for tt in df_cluster.columns]
df_cluster.index = [f"{tt[0]}_{tt[1]}" for tt in df_cluster.index]
df_cluster

from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt
df_cluster.dropna(how='any',inplace=True)
scores1=[]
for k in range(2,10):
    kmeans = KMeans(n_clusters=k,random_state=123987654)
    kmeans.fit(df_cluster)
    labels = kmeans.labels_
    scores1.append(davies_bouldin_score(df_cluster, labels))
best_num_clusters = scores1.index(min(scores1))+2


df_temp_pred = df[df['Year']>=2019]
df_temp_pred = df_temp_pred.groupby(["State","City","Year","Month"],as_index=False)["AvgTemperature"].mean()
df_temp_pred = pd.DataFrame(df_temp_pred)
df_temp_pred.rename(columns={'AvgTemperature':'AvgTemperature'}, inplace = True)
df_temp_pred = df_temp_pred.pivot(index=["State","City"],columns=["Year","Month"],values="AvgTemperature")
df_temp_pred.columns = [f"AvgTemperature_{tt[0]}_{tt[1]}" for tt in df_temp_pred.columns]
df_temp_pred_train, df_temp_pred_test = train_test_split(df_temp_pred, test_size=0.1,random_state=123987654)