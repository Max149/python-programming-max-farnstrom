import math

TP = 2
FP = 2
FN = 11
TN = 985

Possitive = TP + TN

negative = FP + FN

Total = Possitive + negative

accuracy = Possitive / Total

print(f"{accuracy:.1%}")

