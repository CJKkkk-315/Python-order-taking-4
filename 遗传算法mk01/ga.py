import numpy as np
import random


class GA():
	def __init__(self,generation,popsize,to,p1,p2,T,parm_data,C_size):
		self.generation = generation  # 迭代次数
		self.popsize = popsize      # 种群规模
		self.p1 = p1  # 交叉概率
		self.p2 = p2  # 变异概率
		self.to = to  # FJSP编码
		self.T = T  # 退火算法初始温度
		self.Tmachine,self.Tmachinetime,self.tdx,self.work,self.tom,self.machines=parm_data[0],parm_data[1],parm_data[2],parm_data[3],parm_data[4],parm_data[5]
		self.C_size=C_size # 选择框大小

	# 工序交叉算法
	def job_cross(self,L1,L2):
		num = list(set(L1[0]))
		np.random.shuffle(num)
		index = np.random.randint(0,len(num),1)[0]
		jpb_set1 = num[:index+1]
		C1,C2 = np.zeros((1,L1.shape[1]))-1,np.zeros((1,L2.shape[1]))-1
		sig,svg= [], []
		for i in range(L1.shape[1]):
			i1,i2=0,0
			for j in range(len(jpb_set1)):
				if L1[0,i]==jpb_set1[j]:
					C1[0,i]=L1[0,i]
				else:
					i1+=1
				if L2[0,i]==jpb_set1[j]:
					C2[0,i]=L2[0,i]
				else:
					i2+=1
			if i1==len(jpb_set1):
				sig.append(L1[0,i])
			if i2==len(jpb_set1):
				svg.append(L2[0,i])
		signal1,signal2=0,0             #为-1的地方按顺序添加工序编码
		for i in range(L1.shape[1]):
			if C1[0,i]==-1:
				C1[0,i]=svg[signal1]
				signal1+=1
			if C2[0,i]==-1:
				C2[0,i]=sig[signal2]
				signal2+=1
		return C1,C2

	# 机器交叉算法
	def ma_cross(self,m1,t1,m2,t2):
		MC1,MC2,TC1,TC2=[],[],[],[]
		for i in range(len(self.machines)):     
			MC1.append([]),MC2.append([]),TC1.append([]),TC2.append([])
			for j in range(self.machines[i]):
				# 随机概率
				p=np.random.randint(0,2,1)[0]
				# 继承两个父代的概率55开
				if p==0:
					MC1[i].append(m1[i][j]),MC2[i].append(m2[i][j]),TC1[i].append(t1[i][j]),TC2[i].append(t2[i][j]);
				else:
					MC2[i].append(m1[i][j]),MC1[i].append(m2[i][j]),TC2[i].append(t1[i][j]),TC1[i].append(t2[i][j]);
		return MC1,TC1,MC2,TC2

	# 工序变异算法
	def job_mul(self,job):
		location=random.sample(range(job.shape[1]),2)
		job[0,location[0]],job[0,location[1]]=job[0,location[1]],job[0,location[0]]
		return job

	# 机器变异算法
	def ma_mul(self,machine,machine_time):
		for i in range(len(self.machines)):
			r=np.random.randint(0,self.machines[i],1)[0]
			mul_idx=random.sample(range(self.machines[i]),r)
			for j in mul_idx:
				highs=self.tom[i][j]
				lows=self.tom[i][j]-self.tdx[i][j]         
				n_machine=self.Tmachine[i,lows:highs]
				n_time=self.Tmachinetime[i,lows:highs]
				machine_time[i][j]=min(n_time)
				index=np.argwhere(n_time==machine_time[i][j])
				machine[i][j]=n_machine[index[0,0]]
		return machine,machine_time

	# GA总函数
	def ga(self):
		answer=[]
		result=[]
		work_job1,work_job=np.zeros((self.popsize,len(self.work))),np.zeros((self.popsize,len(self.work)))
		work_M,work_T=[],[]
		# 初始化种群，记录最优解
		for i in range(self.popsize):
			job, machine, machine_time = self.to.creat_job()
			C_finish, _, _, _, _ = self.to.caculate(job, machine, machine_time)
			answer.append(C_finish)
			work_job[i] = job[0]
			work_M.append(machine), work_T.append(machine_time)
		result.append([0, min(answer)])
		# 迭代进化
		for gen in range(self.generation):
			# 当前温度由迭代次数决定，迭代次数增加不断降低
			gen_T = self.T * (1-gen/self.generation)
			answer1,work_M1,work_T1=[],[],[]
			for i in range(0,self.popsize,2):
				W1,M1,T1=work_job[i:i+1],work_M[i],work_T[i]
				W2,M2,T2=work_job[i+1:i+2],work_M[i+1],work_T[i+1]
				# 通过概率 交叉编译产生子代
				if np.random.rand()<self.p1:
					W1,W2=self.job_cross(W1,W2)
					M1,T1,M2,T2=self.ma_cross(M1,T1,M2,T2)
				# 当前温度越高，越容易发生变异接受新的解
				if np.random.rand()<self.p2 * gen_T:
					W1=self.job_mul(W1)
					M1,T1=self.ma_mul(M1,T1)
				if np.random.rand()<self.p2 * gen_T:
					W2=self.job_mul(W2)
					M2,T2=self.ma_mul(M2,T2)
				C_finish,_,_,_,_=self.to.caculate(W1,M1,T1)
				work_job1[i]=W1[0]
				answer1.append(C_finish)
				work_M1.append(M1)
				work_T1.append(T1)

				C_finish,_,_,_,_=self.to.caculate(W2,M2,T2)
				work_job1[i+1]=W2[0]
				work_M1.append(M2)
				work_T1.append(T2)
				answer1.append(C_finish)
			# 合并种群
			work_job2,work_M2,work_T2=np.vstack((work_job,work_job1)),np.vstack((work_M,work_M1)),np.vstack((work_T,work_T1))
			answer2=answer+answer1
			# 记录最优解
			best_idx=answer2.index(min(answer2))
			result.append([gen+1,min(answer2)])
			# 通过竞标赛筛选机制产生下次遗传的种群
			for i in range(self.popsize):
				cab=random.sample(range(self.popsize*2),self.C_size)
				index,time=[],[]
				for j in range(self.C_size):
					index.append(cab[j]),time.append(answer2[cab[j]])
				min_time=time.index(min(time))
				min_idx=index[min_time]
				work_job[i],work_M[i],work_T[i]=work_job2[min_idx],work_M2[min_idx],work_T2[min_idx]
				answer[i]=answer2[min_idx]
		# 返回最优解时长和具体结果
		return work_job2[best_idx:best_idx+1],work_M2[best_idx],work_T2[best_idx],result  #
