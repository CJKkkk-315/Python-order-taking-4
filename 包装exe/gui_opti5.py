import datetime
import os
import numpy as np
from pymoo.core.problem import ElementwiseProblem



def optimize(project_name,xl_list,xu_list,optimize_direction,targetl_list,targetu_list,offspring_num,iterations):
	import pandas as pd
	#打开AnsysEM，并打开模型
	from win32com import client
	oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
	oDesktop = oAnsoftApp.getAppDesktop()
	# oProject = oDesktop.OpenProject("C:/Users/Deng/Desktop/rm.aedt")

	def run(im,pTooh,pEm,pLenth,name1):

		oProject = oDesktop.SetActiveProject(project_name)
		oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
		oModule = oDesign.GetModule("Optimetrics")
		oModule.DeleteSetups(["ParametricSetup1"])
		oModule.InsertSetup("OptiParametric",
			[
				"NAME:ParametricSetup1",
				"IsEnabled:="		, True,
				[
					"NAME:ProdOptiSetupDataV2",
					"SaveFields:="		, False,
					"CopyMesh:="		, False,
					"SolveWithCopiedMeshOnly:=", False
				],
				"InterpolationPoints:="	, 0,
				[
					"NAME:StartingPoint"
				],
				"Sim. Setups:="		, ["Setup1"],
				[
					"NAME:Sweeps",
					[
						"NAME:SweepDefinition",
						"Variable:="		, "$im",
						"Data:="		, "{}A".format(im),
						"OffsetF1:="		, False,
						"Synchronize:="		, 0
					],
					[
						"NAME:SweepDefinition",
						"Variable:="		, "pbeta",
						"Data:="		, "0",
						"OffsetF1:="		, False,
						"Synchronize:="		, 0
					],
					[
						"NAME:SweepDefinition",
						"Variable:="		, "pTooth",
						"Data:="		, "{}mm".format(pTooh),
						"OffsetF1:="		, False,
						"Synchronize:="		, 0
					],
					[
						"NAME:SweepDefinition",
						"Variable:="		, "pEm",
						"Data:="		, "{}".format(pEm),
						"OffsetF1:="		, False,
						"Synchronize:="		, 0
					],
					[
						"NAME:SweepDefinition",
						"Variable:="		, "pLenth",
						"Data:="		, "{}mm".format(pLenth),
						"OffsetF1:="		, False,
						"Synchronize:="		, 0
					]
				],
				[
					"NAME:Sweep Operations"
				],
				[
					"NAME:Goals",
					[
						"NAME:Goal",
						"ReportType:="		, "Transient",
						"Solution:="		, "Setup1 : Transient",
						[
							"NAME:SimValueContext",
							"Domain:="		, "Sweep"
						],
						"Calculation:="		, "avg(Moving1.Torque)",
						"Name:="		, "avg(Moving1.Torque)",
						[
							"NAME:Ranges",
							"Range:="		, [						"Var:="			, "Time",						"Type:="		, "a"]
						]
					],
					[
						"NAME:Goal",
						"ReportType:="		, "Transient",
						"Solution:="		, "Setup1 : Transient",
						[
							"NAME:SimValueContext",
							"Domain:="		, "Sweep"
						],
						"Calculation:="		, "pk2pk(Moving1.Torque)/avg(Moving1.Torque)*100",
						"Name:="		, "pk2pk(Moving1.Torque)/avg(Moving1.Torque)*100",
						[
							"NAME:Ranges",
							"Range:="		, [						"Var:="			, "Time",						"Type:="		, "a"]
						]
					],
					[
						"NAME:Goal",
						"ReportType:="		, "Transient",
						"Solution:="		, "Setup1 : Transient",
						[
							"NAME:SimValueContext",
							"Domain:="		, "Sweep"
						],
						"Calculation:="		, "max(InducedVoltage(PhaseA))",
						"Name:="		, "max(InducedVoltage(PhaseA))",
						[
							"NAME:Ranges",
							"Range:="		, [						"Var:="			, "Time",						"Type:="		, "a"]
						]
					],
					[
						"NAME:Goal",
						"ReportType:="		, "Fields",
						"Solution:="		, "Setup1 : Transient",
						[
							"NAME:SimValueContext",
							"Context:="		, "Polyline1",
							"PointCount:="		, 1001
						],
						"Calculation:="		, "max(Br)",
						"Name:="		, "max(Br)",
						[
							"NAME:Ranges",
							"Range:="		, [						"Var:="			, "Distance",						"Type:="		, "a"],
							"Range:="		, [						"Var:="			, "Time",						"Type:="		, "d",						"DiscreteValues:="	, "0.0015625s"]
						]
					]
				]
			])
		oModule.CopySetup("ParametricSetup1")
		oModule = oDesign.GetModule("AnalysisSetup")
		oModule.ResetSetupToTimeZero("Setup1")
		oProject.Save()
		oModule = oDesign.GetModule("Optimetrics")
		oModule.SolveSetup("ParametricSetup1")
		# oModule.ExportOptimetricsResult("ParametricSetup1", "C:/Users/Deng/Desktop/moor/{}.csv".format(name1), False)
		oModule.ExportOptimetricsResult("ParametricSetup1", "{}.csv".format(name1), False)
		oProject.Save()


	creatfile = open("log.csv",'w')
	logger = open("log.csv",'a')
	global logger_flag
	logger_flag = 0



	def create_tittle(name1):
		f = open("{}.csv".format(name1), 'r')
		line0 = f.readlines()[0]
		print(line0)
		logger.write(line0)
		return (1)

	def add_data(name1):
		def delt_alpha(x):
			x = str(x)
			temp = re.sub('[a-zA-Z]', '', x)
			x = str(x)
			return temp
		f = open("{}.csv".format(name1), 'r')
		line1 = f.readlines()[1]
		line1_c = delt_alpha(line1)
		logger.write(line1_c)



	import re
	def generator0(x1,x3,x4,x5,name1):
		def delt_alpha(x):
			x = str(x)
			temp = re.sub('[a-zA-Z]', '', x)
			x = str(x)
			return temp

		run(x1, x3, x4, x5, name1)

		data = pd.read_csv("{}.csv".format(name1))
		data0 = pd.DataFrame({})
		for i in data.columns:
			data0[i] = data[i].apply(delt_alpha)
		res = list(data0.iloc[0, 1:6])
		res1 = list(data0.iloc[0, 6:])
		print(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
		print(res, res1, list(map(abs, map(float, res1))))
		# print(list(map(abs,map(float,res1))))

		#记录过程
		global logger_flag
		if logger_flag == 0:
			create_tittle(name1)
			logger_flag = 1
		else:
			pass
		add_data(name1)
		#移除临时文件并返回
		# os.remove('temp1.csv')
		return (list(map(float,res1)))

	def generator(inputx):
		x1 = inputx[0]
		x2 = 0
		x3 = inputx[1]
		x4 = inputx[2]
		x5 = inputx[3]
		name1 = "temp1"
		return(generator0(x1,x3,x4,x5,name1))




	class MyProblem(ElementwiseProblem):

		def __init__(self):
			super().__init__(n_var=4,
							 n_obj=4,
							 n_constr=4,
							 # xl=np.array([129, 3.8, 0.83, 115]),
							 # xu=np.array([135, 4.2, 0.88, 125]))
							 # xl = np.array([120, 3.5, 0.80, 110]),
							 # xu = np.array([140, 4.5, 0.90, 130]))
							 xl = np.array(xl_list),
							 xu = np.array(xu_list))

		def _evaluate(self, x, out, *args, **kwargs):
			res_gene = generator(x)
			if optimize_direction[0] == 1:
				f1 = optimize_direction[0]*(-1)*(1 * res_gene[0] - targetl_list[0]) * 1
			else:
				f1 = optimize_direction[0] * (-1) * (1 * res_gene[0] - targetu_list[0]) * 1
			if optimize_direction[1] == 1:
				f2 = optimize_direction[1] * (-1) * (res_gene[1] - targetl_list[1]) * 1
			else:
				f2 = optimize_direction[1]*(-1)*(res_gene[1] - targetu_list[1]) * 1
			if optimize_direction[2] == 1:
				f3 = optimize_direction[2] * (-1) * (abs(res_gene[2]) - targetl_list[2]) * 0.001
			else:
				f3 = optimize_direction[2]*(-1)*(abs(res_gene[2])-targetu_list[2])*0.001
			if optimize_direction[3] == 1:
				f4 = optimize_direction[3]*(-1)*(res_gene[3]-targetl_list[3])
			else:
				f4 = optimize_direction[3] * (-1) * (res_gene[3] - targetu_list[3])

			if optimize_direction[0] == 1:
				g1 = optimize_direction[0]*(1 * res_gene[0] - targetu_list[0]) * 1
			else:
				g1 = optimize_direction[0] * (1 * res_gene[0] - targetl_list[0]) * 1
			if optimize_direction[1] == 1:
				g2 = optimize_direction[1]*(res_gene[1] - targetu_list[1]) * 1
			else:
				g2 = optimize_direction[1] * (res_gene[1] - targetl_list[1]) * 1
			if optimize_direction[2] == 1:
				g3 = optimize_direction[2]*(abs(res_gene[2])-targetu_list[2])*0.001
			else:
				g3 = optimize_direction[2] * (abs(res_gene[2]) - targetl_list[2]) * 0.001
			if optimize_direction[3] == 1:
				g4 = optimize_direction[3]*(res_gene[3] - targetu_list[3])
			else:
				g4 = optimize_direction[3] * (res_gene[3] - targetl_list[3])


			out["F"] = [f1, f2,f3,f4 ]
			out["G"] = [g1, g2, g3,g4]


	problem = MyProblem()

	from pymoo.algorithms.moo.nsga2 import NSGA2
	from pymoo.operators.sampling.rnd import FloatRandomSampling
	from pymoo.operators.crossover.sbx import SBX
	from pymoo.operators.mutation.pm import PolynomialMutation

	algorithm = NSGA2(
		# 设置群体大小
		pop_size=10,
		# 设置后代大小
		n_offsprings=offspring_num,
		sampling=FloatRandomSampling(),
		crossover=SBX(prob=0.9, eta=15),
		mutation=PolynomialMutation(prob=0.9, eta=20),
		# 设置重复检查
		eliminate_duplicates=False
	)

	from pymoo.termination import get_termination

	# 终止条件
	termination = get_termination("n_gen", iterations)
	from pymoo.optimize import minimize

	res = minimize(problem,
				   algorithm,
				   termination,
				   seed=10,
				   save_history=True,
				   verbose=True)

	X = res.X
	F = res.F
	G = res.G
	l = []
	logger.close()
	print("优化结束！")


import tkinter as tk
from tkinter import ttk
from functools import partial


def run_optimization():
    project_name = project_name_entry.get()
    xl_list = [float(xl1_entry.get()), float(xl2_entry.get()), float(xl3_entry.get()), float(xl4_entry.get())]
    xu_list = [float(xu1_entry.get()), float(xu2_entry.get()), float(xu3_entry.get()), float(xu4_entry.get())]
    optimize_direction = [int(x) for x in direction_entry.get().split(',')]
    targetl_list = [float(targetl1_entry.get()), float(targetl2_entry.get()), float(targetl3_entry.get()), float(targetl4_entry.get())]
    # targetl_list = [float(x) for x in targetl_entry.get().split(',')]
    targetu_list = [float(targetu1_entry.get()), float(targetu2_entry.get()), float(targetu3_entry.get()), float(targetu4_entry.get())]
    offspring_num = int(offspring_entry.get())
    iterations = int(iterations_entry.get())

    # 调用优化函数
    optimize(project_name, xl_list, xu_list, optimize_direction, targetl_list, targetu_list, offspring_num, iterations)
    # output_text.insert(tk.END, '优化已完成。\n')
    from tkinter import messagebox
    messagebox.showinfo('提示', '优化已完成！')

# 创建主窗口
root = tk.Tk()
root.title('优化程序')

# 添加项目名称输入框和标签
project_name_label = tk.Label(root, text='模型名称：')
project_name_label.grid(row=0, column=0)
project_name_entry = tk.Entry(root)
project_name_entry.insert(0, 'rm')
project_name_entry.grid(row=0, column=1)

# 添加参数1下限输入框和标签
xl1_label = tk.Label(root, text='参数im下限：')
xl1_label.grid(row=1, column=0)
xl1_entry = tk.Entry(root)
xl1_entry.insert(0, '110')
xl1_entry.grid(row=1, column=1)

# 添加参数1上限输入框和标签
xu1_label = tk.Label(root, text='参数im上限：')
xu1_label.grid(row=1, column=2)
xu1_entry = tk.Entry(root)
xu1_entry.insert(0, '150')
xu1_entry.grid(row=1, column=3)

# 添加参数2下限输入框和标签
xl2_label = tk.Label(root, text='参数pTooh下限：')
xl2_label.grid(row=2, column=0)
xl2_entry = tk.Entry(root)
xl2_entry.insert(0, '2.5')
xl2_entry.grid(row=2, column=1)

# 添加参数2上限输入框和标签
xu2_label = tk.Label(root, text='参数pTooh上限：')
xu2_label.grid(row=2, column=2)
xu2_entry = tk.Entry(root)
xu2_entry.insert(0, '5.5')
xu2_entry.grid(row=2, column=3)

# 添加参数3下限输入框和标签
xl3_label = tk.Label(root, text='参数pEm下限：')
xl3_label.grid(row=3, column=0)
xl3_entry = tk.Entry(root)
xl3_entry.insert(0, '0.70')
xl3_entry.grid(row=3, column=1)

# 添加参数3上限输入框和标签
xu3_label = tk.Label(root, text='参数pEm上限：')
xu3_label.grid(row=3, column=2)
xu3_entry = tk.Entry(root)
xu3_entry.insert(0, '1.00')
xu3_entry.grid(row=3, column=3)

# 添加参数4下限输入框和标签
xl4_label = tk.Label(root, text='参数pLenth下限：')
xl4_label.grid(row=4, column=0)
xl4_entry = tk.Entry(root)
xl4_entry.insert(0, '100')
xl4_entry.grid(row=4, column=1)

# 添加参数4上限输入框和标签
xu4_label = tk.Label(root, text='参数pLenth上限：')
xu4_label.grid(row=4, column=2)
xu4_entry = tk.Entry(root)
xu4_entry.insert(0, '150')
xu4_entry.grid(row=4, column=3)

# 添加目标最大化/最小化输入框和标签
direction_label = tk.Label(root, text='优化方向：')
direction_label.grid(row=5, column=0)
direction_entry = tk.Entry(root)
direction_entry.insert(0, '1, -1, -1,-1')
direction_entry.grid(row=5, column=1)


targetl1_label = tk.Label(root, text='avg(Mov)下限：')
targetl1_label.grid(row=6, column=0)
targetl1_entry = tk.Entry(root)
targetl1_entry.insert(0, '75.1')
targetl1_entry.grid(row=6, column=1)

targetu1_label = tk.Label(root, text='avg(Mov)上限：')
targetu1_label.grid(row=6, column=2)
targetu1_entry = tk.Entry(root)
targetu1_entry.insert(0, '75.5')
targetu1_entry.grid(row=6, column=3)

targetl2_label = tk.Label(root, text='pk2pk下限：')
targetl2_label.grid(row=7, column=0)
targetl2_entry = tk.Entry(root)
targetl2_entry.insert(0, '3')
targetl2_entry.grid(row=7, column=1)

targetu2_label = tk.Label(root, text='pk2pk上限：')
targetu2_label.grid(row=7, column=2)
targetu2_entry = tk.Entry(root)
targetu2_entry.insert(0, '5')
targetu2_entry.grid(row=7, column=3)

targetl3_label = tk.Label(root, text='max(IndV)下限：')
targetl3_label.grid(row=8, column=0)
targetl3_entry = tk.Entry(root)
targetl3_entry.insert(0, '200')
targetl3_entry.grid(row=8, column=1)

targetu3_label = tk.Label(root, text='max(IndV)上限：')
targetu3_label.grid(row=8, column=2)
targetu3_entry = tk.Entry(root)
targetu3_entry.insert(0, '1000')
targetu3_entry.grid(row=8, column=3)

targetl4_label = tk.Label(root, text='max(Br)下限：')
targetl4_label.grid(row=9, column=0)
targetl4_entry = tk.Entry(root)
targetl4_entry.insert(0, '0.4')
targetl4_entry.grid(row=9, column=1)

targetu4_label = tk.Label(root, text='max(Br)上限：')
targetu4_label.grid(row=9, column=2)
targetu4_entry = tk.Entry(root)
targetu4_entry.insert(0, '1')
targetu4_entry.grid(row=9, column=3)



offspring_label = tk.Label(root, text='种群数量：')
offspring_label.grid(row=10, column=0)
offspring_entry = tk.Entry(root)
offspring_entry.insert(0, '10')
offspring_entry.grid(row=10, column=1)

iterations_label = tk.Label(root, text='迭代次数：')
iterations_label.grid(row=11, column=0)
iterations_entry = tk.Entry(root)
iterations_entry.insert(0, '100')
iterations_entry.grid(row=11, column=1)

submit_button = tk.Button(root, text='开始优化', command=run_optimization)
submit_button.grid(row=12, column=1)

root.mainloop()

