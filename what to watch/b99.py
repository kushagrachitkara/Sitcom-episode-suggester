import random
import collections
S= {}
S[1] = [i for i in range (1,23)]
S[2] = [i for i in range (1,24)]
S[3] = [i for i in range (1,24)]
S[4] = [i for i in range (1,22)]
S[5] = [i for i in range (1,22)]
S[6] = [i for i in range (1,19)]
S[7] = [i for i in range (1,17)]
seas = random.choice(list(S))
print("Watch: S" + str(seas) + "E" + str(random.choice(S[seas])))
input()
