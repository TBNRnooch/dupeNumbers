# dupeNumbers
def function(numbers):
    res = 0    
    for i, n in enumerate(numbers):
        for m in numbers[i+1:]:
            if m == n:
                res = n
                break
    
    return res


def runTest(numbers):
    print('Input:', numbers)

    x = function(numbers)

    print('Output:', x)


def start():
    runTest([1, 2, 3, 2])
    runTest([1, 3, 2, 1, 5, 6])

start()
