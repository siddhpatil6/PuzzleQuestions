class SecondLargestNumbers(object):
    def secondLargestNumber(self, lst):
        largestNumber = 0
        secondLargestNumber = 0
        for index in range(0,len(lst)):
            if largestNumber < lst[index]:
                secondLargestNumber = largestNumber
                largestNumber = lst[index]
            elif secondLargestNumber < lst[index]:
                secondLargestNumber = lst[index]

        return secondLargestNumber


lst = [23, 42, 42, 14, 32, 53, 22]
secondLargestNumber = SecondLargestNumbers()
print('Second Largest Number is :', secondLargestNumber.secondLargestNumber(lst))
