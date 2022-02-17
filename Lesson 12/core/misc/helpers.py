def is_prime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num < 2: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def fl(*numbers):
    return list(filter(is_prime, numbers))
    print(numbers)
result =fl(2,3,4,5,6,7,8,9,10,11)
print(result)