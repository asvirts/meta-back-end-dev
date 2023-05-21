# Algorithmic complexity

# Linear | O(n)
for i in range(1001):
    print('O(n): ', i)
print('')

# Quadratic time | O(n^2)

for x in range(10):
    for y in range(10):
        print('O(n^2): ', x, y)

# Constant time | O(1)
drinks = {1: 'Coffee', 2: 'Tea', 3: 'Gatorade'}
print('O(1): ', drinks[3])

# Logarithmic time | O(log n)


def find_num(tar):
    it = 0
    x = range(100)
    left = 0
    right = len(x) - 1

    while left <= right:
        it += 1
        mid = (left + right) // 2
        isNum = x[mid]

        if tar == isNum:
            print('O(log n) iterations: ', it)
            return mid
        elif tar < isNum:
            right = mid - 1
        else:
            left = mid + 1
    print('O(log n) iterations: ', it)


print('O(log n) number was: ', find_num(46))


# Exponential time | O(2^n)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print('O(2^n): ', fibonacci(12))
