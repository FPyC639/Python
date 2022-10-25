def LCS(X,Y):
    m,n = len(X),len(Y)
    c = [ [0] * (n+1) for i in range(m+1)]
    for i in range(m-1):
        for j in range(n-1):
            if(X[i] == Y[j]):
                c[i+1][j+1] = c[i-1][j-1] + 1
            elif(c[i][j+1]>= c[i+1][j]):
                c[i+1][j+1] = max(c[i][j+1],c[i+1][j])
    new_list = [[i, y] for i,y in zip(Y,c)]
    new_list[0][:] = list(X)
    for i in new_list:
        print(f"{i}")

if __name__ in "__main__":
    a, b = "edcfg", "abcedfec"
    c, d = "abycmhdk", "kasmdhfbcyd"
    LCS(a,b)
    LCS(c,d)




