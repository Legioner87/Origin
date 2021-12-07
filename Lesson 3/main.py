# 1
def lesson3(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for dano in range(1, 100):
    if lesson3(dano):
        print(dano, end=' ')

# 2

t = 'мой код худшее что вы запускали'
str_t = set(t)
res = ''
for x in str_t:
    if t.count(x) == 1:
        res += x
print(res)