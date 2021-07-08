import random
import collections
S= {}
S[1] = [i for i in range (1,7)]
S[2] = [i for i in range (1,23)]
S[3] = [i for i in range (1,26)]
S[4] = [i for i in range (1,20)]
S[5] = [i for i in range (1,29)]
S[6] = [i for i in range (1,27)]
S[7] = [i for i in range (1,27)]
S[8] = [i for i in range (1,25)]
S[9] = [i for i in range (1,26)]

seas = random.choice(list(S))
print("Watch: S" + str(seas) + "E" + str(random.choice(S[seas])))
input()
