import matplotlib.pyplot as plt
from parser_studentID import Parser

def visualizeWordDistribution(inputFile, outputImage):
	res = []
	with open(inputFile, encoding='utf8') as f:
		lines = f.readlines()
		for i in lines:
			res.append(i.replace('\n', ''))
	del res[0]
	del res[0]
	del res[-1]
	y = [0,0,0,0,0,0,0,0,0,0,0]
	for i in res:
		k = Parser(i)
		n = k.getVocabularySize()
		if n >= 100:
			y[-1] += 1
		else:
			y[n//10] += 1
	x = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', 'others']
	plt.bar(x, y)
	plt.tick_params()
	plt.savefig(outputImage)




def visualizePostNumberTrend(inputFile, outputImage):
	q = {}
	a = {}
	res = []
	with open(inputFile, encoding='utf8') as f:
		lines = f.readlines()
		for i in lines:
			res.append(i.replace('\n', ''))
	del res[0]
	del res[0]
	del res[-1]
	for i in res:
		k = Parser(i)
		if k.getPostType() == 'question':
			q[k.getDateQuarter()] = q.get(k.getDateQuarter(), 0) + 1
		elif k.getPostType() == 'answer':
			a[k.getDateQuarter()] = a.get(k.getDateQuarter(), 0) + 1
	q = [[i, j] for i, j in q.items()]
	a = [[i, j] for i, j in a.items()]
	q.sort(key=lambda x: int(x[0].replace('Q', '')))
	a.sort(key=lambda x: int(x[0].replace('Q', '')))
	q_x = [i[0] for i in q]
	q_y = [i[1] for i in q]
	a_x = [i[0] for i in a]
	a_y = [i[1] for i in a]
	plt.clf()
	plt.plot(q_x, q_y, 'blue', label='question')
	plt.plot(a_x, a_y, 'red', label='answer')
	plt.tick_params(labelsize=5)
	plt.legend()
	plt.savefig(outputImage)



if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
