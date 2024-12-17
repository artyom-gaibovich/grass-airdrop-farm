a = int(input())
res = sum([int(digit) * 10**(3-i) for i, digit in enumerate(str(abs(a))[-4:])])
if a < 0:
    res *= -1
print(res)
