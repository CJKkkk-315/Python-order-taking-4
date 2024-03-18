import re

def preprocessLine(inputLine):
	c = re.findall('Body="(.*?)"', inputLine)
	c = c[0]
	for i in [['&lt;', '<'], ['&gt;', '>'], ['&apos;', "'"], ['&quot;', '"'], ['&amp;', '&']]:
		c = c.replace(i[0], i[1])
	c = c.replace('&#xA;', ' ')
	c = c.replace('&#xD;', ' ')
	pattern = re.compile(r'<[^>]+>', re.S)
	outputLine = pattern.sub('', c)
	return outputLine



def splitFile(inputFile, outputFile_question, outputFile_answer):
	res = []
	with open(inputFile, encoding='utf8') as f:
		lines = f.readlines()
		for i in lines:
			res.append(i.replace('\n',''))
	del res[0]
	del res[0]
	del res[-1]
	a = open(outputFile_question, 'w', encoding='utf8')
	q = open(outputFile_answer, 'w', encoding='utf8')
	for i in res:
		if re.findall('PostTypeId="(.*?)"', i)[0] == '1':
			a.write(preprocessLine(i) + '\n')
		elif re.findall('PostTypeId="(.*?)"', i)[0] == '2':
			q.write(preprocessLine(i) + '\n')
	a.close()
	q.close()



if __name__ == "__main__":

	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)
