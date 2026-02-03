op = str(input())

nums = sorted([num for num in op if num != "+"])

res = []
for num in nums:
    res.append(str(num))
    res.append("+")

print("".join(res[:-1]))
