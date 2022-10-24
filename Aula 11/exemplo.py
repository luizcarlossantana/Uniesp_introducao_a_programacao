'''matriz = [
[[1,2,3],[33,34,45],[22,66,67]],
[4,5,6],
[9,8,0]

]

print(matriz[1][2])
print(matriz[0][2][2])'''

'''matriz =[[1,2,3],[2,3,4],[4,5,6]] 
for linha in matriz:
    for coluna in linha:
        print(coluna)'''

'''matriz =[[1,2,3],[2,3,4],[4,5,6]] 
for i in range(len(matriz)):
    for j in range (len(matriz[i])):
        print(matriz[i][j])'''


mtz = [

    [78,90,100],
    [56,77,93],
    [10,4,73]
]

for l in range(len(mtz)):
    for c in range(len(mtz[l])):
        if l==c:
            print(mtz[l][c])
  


