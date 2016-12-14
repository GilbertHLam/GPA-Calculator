class Course:
	
	def __init__(self, weight, grade):
		self.__weight = weight
		self.__grade = grade*weight
	
	def returnWeight(self):
		return self.__weight
	
	def returnGrade(self):
		return self.__grade