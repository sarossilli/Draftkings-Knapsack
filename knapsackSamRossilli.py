def printA(a):
    for l in a:
        print()
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in l]))

def knapSack(W, wt, val, n,l): 
    K = [[[0 for x in range(W + 1)] for x in range(n + 1)] for x in range(l+1)]
    B = []
    # Build table K[L][I][W] in bottom up manner
    for i in range(n + 1): 
        for w in range(W + 1): 
            for L in range(l+1):
                if i<=L:
                    if i == 0 or w == 0 or L==0: 
                        K[L][i][w] = 0
                    elif wt[i-1] <= w: 
                        K[L][i][w] = max(val[i-1] + K[L][i-1][w-wt[i-1]],  K[L][i-1][w])

                    else: 
                        K[L][i][w] = K[L][i-1][w] 
                else:
                    if i == 0 or w == 0 or L==0: 
                        K[L][i][w] = 0
                    elif wt[i-1] <= w: 
                        K[L][i][w] = max(val[i-1] + K[L-1][i-1][w-wt[i-1]],  K[L][i-1][w]) 
                    else: 
                        K[L][i][w] = K[L][i-1][w] 
    
    res = K[l][n][w]    
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[l][i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            B.append(i) 
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1] 

    return K[l][n][w],B



import pandas as pd 

df = pd.read_csv('Dk.csv')

df = df[df['Roster Position'] == 'FLEX']
df = df[df['Salary']>2000]

df = df.reset_index()

wt = df['Salary'].tolist()
wt[:] = [x / 100 for x in wt]
wt[:] = [round(x) for x in wt]

val = df['AvgPointsPerGame'].tolist()
val[:] = [(x * 100 )for x in val]
val[:] = [round(x) for x in val]


W = int(50000/100)
n = len(val) 
l = 6

print(df)

a,b = knapSack(W,wt,val,n,l)
print(b)
# Driver program to test above function 
#val = [5, 10, 50,100] 
#wt = [10,50, 20, 10] 
#W = 70
#n = len(val) 
#l = 5


#print(b) 
def print(a,b):
    print("EXPECTED POINTS")
    print(a/100)
    print('\n')

    print("PLAYERS")
    for i in b:
        print( df.iloc[i]['Name'] )