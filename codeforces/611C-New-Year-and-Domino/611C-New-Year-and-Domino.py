def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

row, col = list_()
s = []
for i in range(row):
    s.append(input())

queries = []
q = int(input())
for _ in range(q):
    queries.append([x-1 for x in list_()])

vpre = [[0] * (col+2) for _ in range(row+2)]
hpre = [[0] * (col+2) for _ in range(row+2)]


for i in range(1, row+1):
    for j in range(1, col+1):
        val = 1 if i - 2 >= 0 and s[i-1][j-1] == "." and s[i-2][j-1] == "." else 0
        vpre[i][j] = vpre[i-1][j] + vpre[i][j-1] - vpre[i-1][j-1] + val

        val = 1 if j - 2 >= 0 and s[i-1][j-1] == "." and s[i-1][j-2] == "." else 0
        hpre[i][j] = hpre[i-1][j] + hpre[i][j-1] - hpre[i-1][j-1] + val


def sumRegion(row1, col1, row2, col2):
    print(vpre[row2+1][col2+1] - vpre[row2+1][col1] - vpre[row1+1][col2+1] + vpre[row1+1][col1] + hpre[row2+1][col2+1] - hpre[row2+1][col1+1] - hpre[row1][col2+1] + hpre[row1][col1+1])

for row1, col1, row2, col2 in queries:
    sumRegion(row1, col1, row2, col2)