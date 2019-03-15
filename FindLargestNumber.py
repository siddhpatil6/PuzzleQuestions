class FindLargestNumber:

    def findLargestNumber(self, lst1):
        large = lst1[0]
        for index in range(0, 5):
            if large < lst1[index]:
                large = lst1[index]

        return large


lst = [12, 13, 24, 44, 22, 55]
find = FindLargestNumber()
print('Largest Number is: ', find.findLargestNumber(lst))
