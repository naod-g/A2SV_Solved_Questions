def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())


for i in range(n):
    word = str_()
    length = len(word[0])

    if length > 10:
        val = str(word[0][0]) + str(length-2) + str(word[0][-1])
        print(val)
    else:
        print(word[0])