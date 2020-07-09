# dupeNumbers
def findTheDuplicate(numbers):
    res = 0    
    def findTheDuplicate(numbers):
    res = 0
    numDict = {}
    for n in numbers:
       if n in numDict:
           res = n
           break
       else:
           numDict[n] = n
    return res


def runTest(numbers):
    print('Input:', numbers)

    x = function(numbers)

    print('Output:', x)


def start():
    runTest([1, 2, 3, 2])
    runTest([1, 3, 2, 1, 5, 6])

start()
