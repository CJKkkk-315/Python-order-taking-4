import re
from preprocessData_studentID import preprocessLine


class Parser:
	"""docstring for ClassName"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()

	def __str__(self):
		#print ID, Question/Answer/Others, creation date, the main content
		return ','.join([self.ID, self.type, self.dateQuarter, self.cleanBody])
		#write your code here

	def getID(self):
		c = re.findall('Id="(.*?)"', self.inputString)
		return c[0]
		

	def getPostType(self):
		c = re.findall('PostTypeId="(.*?)"', self.inputString)
		if c[0] == '1':
			return 'question'
		elif c[0] == '2':
			return 'answer'
		else:
			return 'others'
		

	def getDateQuarter(self):
		c = re.findall('CreationDate="(.*?)"', self.inputString)
		c = c[0].split('-')
		y = c[0]
		t = 0
		if c[1] in ['01','02','03']:
			t = 1
		if c[1] in ['04','05','06']:
			t = 2
		if c[1] in ['07','08','09']:
			t = 3
		if c[1] in ['10','11','12']:
			t = 4
		return f'{y}Q{t}'
		

	def getCleanedBody(self):
		return preprocessLine(self.inputString)
		

	def getVocabularySize(self):
		l = []
		for i in self.getCleanedBody().split():
			aw = []
			for c in i:
				if not c.isalpha():
					continue
				aw.append(c)
			if aw:
				if ''.join(aw) not in l:
					l.append(''.join(aw).lower())
		return len(l)
		




