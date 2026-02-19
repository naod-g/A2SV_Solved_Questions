def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())

points = list_()
points.sort()

print(points[n // 2 - 1] if n%2 == 0 else points[n//2])

