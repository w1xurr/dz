# 1 
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

def avg(aF, bF, cF, dF, eF):
    res = (aF+bF+cF+dF+eF)/5
    return res

print("Average: ", avg(a, b, c, d, e))

# 2
inp = int(input("Enter num: "))

def count_in_num(i):
    count = 0
    while i > 0:
        count += 1
        i = i // 10
    return count

print(count_in_num(inp))

# 3
inputt = int(input("Enter num: "))

def count_0_in_bin_from_num(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            count+=1
        num = num // 2
    return count
print("Количество нулей: ", count_0_in_bin_from_num(inputt))

