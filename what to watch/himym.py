import random
import collections
S= {}
S[1] = [i for i in range (1,23)]
S[2] = [i for i in range (1,23)]
S[3] = [i for i in range (1,21)]
for j in range (4,10):
    S[j] = [i for i in range (1,25)]
seas = random.choice(list(S))
print("Watch: S" + str(seas) + "E" + str(random.choice(S[seas])))
input()
