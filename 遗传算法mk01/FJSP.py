import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文

class FJSP():
	def __init__(self,job_num,machine_num,p1,p2,parm_data):
		self.job_num=job_num     			#工件数
		self.machine_num=machine_num		#机器数
		self.p1=p1  						#全局选择的概率
		self.p2=p2  						#局部选择的概率
		self.Tmachine,self.Tmachinetime,self.tdx,self.work,self.tom,self.machines=parm_data[0],parm_data[1],parm_data[2],parm_data[3],parm_data[4],parm_data[5]  # 数据读取

	# fjsp 编码
	def creat_job(self):
		job=np.copy(self.work)
		np.random.shuffle(job)
		job=np.array(job).reshape(1,len(self.work))
		# 初始化
		machine,machine_time=[],[]
		a_global=np.zeros((1,self.machine_num))
		r=np.random.rand()						
		for i in range(self.job_num):
			machine.append([]),machine_time.append([])
			a_part=np.zeros((1,self.machine_num))
			for j in range(self.machines[i]):
				highs=self.tom[i][j]
				lows=self.tom[i][j]-self.tdx[i][j]
				n_machine=self.Tmachine[i,lows:highs].tolist()
				n_time=self.Tmachinetime[i,lows:highs].tolist()
				index_select=[]
				# 三种随机方式
				if r<self.p1 or r>1-self.p2: 
					for k in range(len(n_machine)):
						m=int(n_machine[k])-1
						index_select.append(m)
						t=n_time[k]
						a_global[0,m]+=t
						a_part[0,m]+=t
					
					if r<self.p1:
						select=a_global[:,index_select]
						idx_select=np.argmin(select[0])
					else:
						select=a_part[:,index_select]
						idx_select=np.argmin(select[0])
					m_select=n_machine[idx_select]
					t_index=n_machine.index(m_select)
					machine[i].append(m_select)
					machine_time[i].append(n_time[t_index])
				else:
					index=np.random.randint(0,len(n_time),1)
					machine[i].append(n_machine[index[0]])
					machine_time[i].append(n_time[index[0]])
		return job,machine,machine_time

	# fjsp 解码
	def caculate(self,job,machine,machine_time):
		jobtime=np.zeros((1,self.job_num))        
		tmm=np.zeros((1,self.machine_num))
		list_M,list_S,list_W=[],[],[]
		count=np.zeros((1,self.job_num),dtype=np.int)
		for i in range(job.shape[1]):
			svg=int(job[0,i])
			sig=int(machine[svg][count[0,svg]])-1
											
			startime=max(jobtime[0,svg],tmm[0,sig])   	
			tmm[0,sig]=startime+machine_time[svg][count[0,svg]]
			jobtime[0,svg]=startime+machine_time[svg][count[0,svg]]
			
			list_M.append(sig+1)
			list_S.append(startime)
			list_W.append(machine_time[svg][count[0,svg]])
			count[0,svg]+=1
		tmax=np.argmax(tmm[0])+1
		C_finish=max(tmm[0])
		return C_finish,list_M,list_S,list_W,tmax
	def axis(self):
		index=['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10']
		scale_ls,index_ls=[],[]
		for i in range(self.machine_num):
			scale_ls.append(i+1)
			index_ls.append(index[i])
		return index_ls,scale_ls

	def draw(self, job, machine, machine_time):  # 画图
		C_finish, list_M, list_S, list_W, tmax = self.caculate(job, machine, machine_time)
		figure, ax = plt.subplots()
		count = np.zeros((1, self.job_num))
		for i in range(job.shape[1]):
			count[0, int(job[0, i]) - 1] += 1
			plt.bar(x=list_S[i], bottom=list_M[i], height=0.5, width=list_W[i], orientation="horizontal", color='white',
					edgecolor='black')
			plt.text(list_S[i] + list_W[i] / 32, list_M[i], '%.0f' % (job[0, i] + 1), color='black', fontsize=10,
					 weight='bold')
		plt.plot([C_finish, C_finish], [0, tmax], c='black', linestyle='-.',
				 label='完工时间=%.1f' % (C_finish))

		plt.xlabel("加工时间")
		plt.title("甘特图")
		plt.ylabel("机器")

		scale_ls, index_ls = self.axis()
		plt.yticks(index_ls, scale_ls)
		plt.axis([0, C_finish * 1.1, 0, self.machine_num + 1])
		plt.tick_params(labelsize=22)
		labels = ax.get_xticklabels()
		[label.set_fontname('SimHei') for label in labels]
		plt.legend()
		plt.xlabel("加工时间")
		plt.show()