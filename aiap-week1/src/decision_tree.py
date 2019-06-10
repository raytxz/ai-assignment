class DecisionTree:
	def gini(self, arrayOne, arrayTwo):
		giniOne = self.subNodeGini(arrayOne)
		giniTwo = self.subNodeGini(arrayTwo)
		weightedGini = (len(arrayOne)/(len(arrayOne)+len(arrayTwo))) * giniOne + (len(arrayTwo)/(len(arrayOne)+len(arrayTwo))) * giniTwo

		return weightedGini

	def subNodeGini(self, subNode):
		countZero = 0
		countOne = 0

		for i in subNode:
			if i == 0:
				countZero += 1
			else:
				countOne += 1

		giniScore = 1 - (countZero/len(subNode))**2 - (countOne/len(subNode))**2

		return giniScore
