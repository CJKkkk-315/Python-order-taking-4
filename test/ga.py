import numpy as np
import random


class GA():
	def __init__(self,generation,popsize,to,p1,p2,parm_data,C_size):
		self.generation = generation  # 迭代次数
		self.popsize = popsize      # 种群规模
		self.p1 = p1  # 交叉概率
		self.p2 = p2  # 变异概率
		self.to = to  # FJSP编码
		self.Tmachine,self.Tmachinetime,self.tdx,self.work,self.tom,self.machines=parm_data[0],parm_data[1],parm_data[2],parm_data[3],parm_data[4],parm_data[5]
		self.C_size=C_size
	def job_cross(self,chrom_L1,chrom_L2):       #工序的pox交叉
		num=list(set(chrom_L1[0]))
		np.random.shuffle(num)
		index=np.random.randint(0,len(num),1)[0]
		jpb_set1=num[:index+1]                  #固定不变的工件
		C1,C2=np.zeros((1,chrom_L1.shape[1]))-1,np.zeros((1,chrom_L1.shape[1]))-1
		sig,svg=[],[]
		for i in range(chrom_L1.shape[1]):#固定位置的工序不变
			ii,iii=0,0
			for j in range(len(jpb_set1)):
				if(chrom_L1[0,i]==jpb_set1[j]):
					C1[0,i]=chrom_L1[0,i]
				else:
					ii+=1
				if(chrom_L2[0,i]==jpb_set1[j]):
					C2[0,i]=chrom_L2[0,i]
				else:
					iii+=1
			if(ii==len(jpb_set1)):
				sig.append(chrom_L1[0,i])
			if(iii==len(jpb_set1)):
				svg.append(chrom_L2[0,i])
		signal1,signal2=0,0             #为-1的地方按顺序添加工序编码
		for i in range(chrom_L1.shape[1]):
			if(C1[0,i]==-1):
				C1[0,i]=svg[signal1]
				signal1+=1
			if(C2[0,i]==-1):
				C2[0,i]=sig[signal2]
				signal2+=1
		return C1,C2
	def ma_cross(self,m1,t1,m2,t2):  #机器均匀交叉
		MC1,MC2,TC1,TC2=[],[],[],[]
		for i in range(len(self.machines)):     
			MC1.append([]),MC2.append([]),TC1.append([]),TC2.append([]);
			for j in range(self.machines[i]):
				index=np.random.randint(0,2,1)[0]
				if(index==0):  #为0时继承继承父代的机器选择
					MC1[i].append(m1[i][j]),MC2[i].append(m2[i][j]),TC1[i].append(t1[i][j]),TC2[i].append(t2[i][j]);
				else:                #为1时另一个父代的加工机器选择
					MC2[i].append(m1[i][j]),MC1[i].append(m2[i][j]),TC2[i].append(t1[i][j]),TC1[i].append(t2[i][j]);
		return MC1,TC1,MC2,TC2
	def job_mul(self,job):
		location=random.sample(range(job.shape[1]),2)
		job[0,location[0]],job[0,location[1]]=job[0,location[1]],job[0,location[0]]
		return job
	def ma_mul(self,machine,machine_time):
		for i in range(len(self.machines)):
			r=np.random.randint(0,self.machines[i],1)[0]   #挑选位置
			mul_idx=random.sample(range(self.machines[i]),r)
			for j in mul_idx:
				highs=self.tom[i][j]
				lows=self.tom[i][j]-self.tdx[i][j]         
				n_machine=self.Tmachine[i,lows:highs]      #取出加工机器
				n_time=self.Tmachinetime[i,lows:highs] 		#取出加工时间
				machine_time[i][j]=min(n_time) 				#挑选最小加工时间
				index=np.argwhere(n_time==machine_time[i][j])
				machine[i][j]=n_machine[index[0,0]]
		return machine,machine_time

	def ga_total(self):
		answer=[]
		result=[]
		work_job1,work_job=np.zeros((self.popsize,len(self.work))),np.zeros((self.popsize,len(self.work)))
		work_M,work_T=[],[]
		for gen in range(self.generation):
			if(gen<1):                      #第一次生成多个可行的工序编码，机器编码，时间编码
				for i in range(self.popsize):
					job,machine,machine_time=self.to.creat_job()
					C_finish,_,_,_,_=self.to.caculate(job,machine,machine_time)
					answer.append(C_finish)
					work_job[i]=job[0]
					work_M.append(machine),work_T.append(machine_time);
				result.append([gen,min(answer)])#记录初始解的最小完工时间
			answer1,work_M1,work_T1=[],[],[]
			for i in range(0,self.popsize,2):    
				W1,M1,T1=work_job[i:i+1],work_M[i],work_T[i]
				W2,M2,T2=work_job[i+1:i+2],work_M[i+1],work_T[i+1]
				if np.random.rand()<self.p1:
					W1,W2=self.job_cross(W1,W2)
					M1,T1,M2,T2=self.ma_cross(M1,T1,M2,T2)
				if np.random.rand()<self.p2*(1-gen/self.generation):
					W1=self.job_mul(W1)
					M1,T1=self.ma_mul(M1,T1)
				if np.random.rand()<self.p2*(1-gen/self.generation):
					W2=self.job_mul(W2)
					M2,T2=self.ma_mul(M2,T2)
				C_finish,_,_,_,_=self.to.caculate(W1,M1,T1)
				work_job1[i]=W1[0]  #更新工序编码
				answer1.append(C_finish)
				work_M1.append(M1),work_T1.append(T1);

				C_finish,_,_,_,_=self.to.caculate(W2,M2,T2)
				work_job1[i+1]=W2[0]  #更新工序编码
				work_M1.append(M2),work_T1.append(T2);
				answer1.append(C_finish)
			work_job2,work_M2,work_T2=np.vstack((work_job,work_job1)),np.vstack((work_M,work_M1)),np.vstack((work_T,work_T1))
			answer2=answer+answer1
			best_idx=answer2.index(min(answer2))             #找到最小完工时间的个体
			result.append([gen+1,min(answer2)])#记录每一次迭代的最优个体
			for i in range(self.popsize):
				cab=random.sample(range(self.popsize*2),self.C_size)      #按照C_size生成一组不重复的索引用于锦标赛选择 
				index,time=[],[]
				for j in range(self.C_size):
					index.append(cab[j]),time.append(answer2[cab[j]]);  
				min_time=time.index(min(time))
				min_idx=index[min_time]
				work_job[i],work_M[i],work_T[i]=work_job2[min_idx],work_M2[min_idx],work_T2[min_idx] #选择出的个体，用于下次遗传
				answer[i]=answer2[min_idx]
			
		return work_job2[best_idx:best_idx+1],work_M2[best_idx],work_T2[best_idx],result  #
