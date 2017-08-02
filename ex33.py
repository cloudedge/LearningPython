def NumberAppend(Init,Max,step):
    i = Init
    numbers = []
    for i in range(Init,Max):
        print "top number is %s" % i
        numbers.append(i)
        i = i + step + 7 # This sentense don't make sense!!!
        print "bottom number is %s" % i
    print "first", numbers
    i = Init
    for numbers[i] in range(Init,Max):
        print" top numbers[%r] = %r " % (i,numbers[i])
        print "numbers[%r] + step = %r" % (i, numbers[i] + step)
        numbers[i] = numbers[i] + step
        print" bottom numbers[%r] = %r " % (i,numbers[i])

    print "second", numbers
    return numbers

print "The numbers is: ", NumberAppend(0,6,2)

'''
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)


    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" %i


print "The numbes: "

for num in numbers:
    print num
'''
