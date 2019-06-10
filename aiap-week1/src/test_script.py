from decision_tree import DecisionTree
import numpy as np

# Test for Gini Calcuation
giniScore = DecisionTree().gini([1, 0, 0, 0, 0], [1, 1, 1, 1, 0])
print("Gini score: " + str(giniScore))