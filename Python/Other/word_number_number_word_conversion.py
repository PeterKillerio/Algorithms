# This algorithm takes as an input integer and spells out the number
# Input can also be a spelled number and the algirithm writes out the integer

# exapmple input: "fivethousandthreehundred" ouput: 5300
# input: "twohundredfivethousandfivehundredone" output: 200501
# input: 165800 output: "onehundredsixtyfivethousandeighthundredninetynine"

# range: 1-999 999



TenthsDividers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
SingleNums = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# NUMBER DICTIONARY GENERATOR FOR 1-99
generatedNumbers = []
# 10-19
teenNums = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

for n in SingleNums:
    generatedNumbers.append(n)
for n in teenNums:
    generatedNumbers.append(n)
for tens in range(len(TenthsDividers)):
    generatedNumbers.append(TenthsDividers[tens])
    for singles in range(len(SingleNums)):
        newStr = TenthsDividers[tens] + SingleNums[singles]
        generatedNumbers.append(newStr)


# INPUT
inp = input()

try:
    inp = int(inp)
except:
    inp = str(inp)

# Divide word by hundreds then thousands

if(isinstance(inp, str)):
    inpStr = str(inp)

    withoutHundreds = inp.split("thousand")
    withoutThousands = []
    innerNums = []

    for Numstring in withoutHundreds:
        withoutThousands.append(Numstring.split("hundred"))

    for thousands in range(len(withoutThousands)):
        for hundreds in range(len(withoutThousands[thousands])):
            if(len(withoutThousands[thousands][hundreds]) == 0):
                withoutThousands[thousands][hundreds] = 0
                continue

            if(withoutThousands[thousands][hundreds] in generatedNumbers):
                withoutThousands[thousands][hundreds] = int(generatedNumbers.index(withoutThousands[thousands][hundreds]))+1
            else:
                print("ERROR")
                exit()

    # start converting to ints

    finalNum = 0

    for item in range(len(withoutThousands)):
        num1 = 0
        for inn in range(len(withoutThousands[item])):
            if(inn != len(withoutThousands[item])-1):
                num1 += (withoutThousands[item][inn]*100)
            else:
                num1 += withoutThousands[item][inn]

        if(item != (len(withoutThousands)-1)):
            finalNum += (num1*1000)
        else:
            finalNum += num1

    print(finalNum)

else:
    inpInt = int(inp)
    inpString = str(inpInt)

    wordNum = ""

    if(len(inpString) > 3):
        # THOUSANDS PART
        strThousands = inpString[:-3]

        if((int(strThousands) // 100) != 0):
            wordNum += generatedNumbers[(int(strThousands) // 100) - 1] + "hundred"

        if((int(strThousands) % 100) != 0):
            wordNum += generatedNumbers[(int(strThousands) % 100) - 1]
        # # #

        ###
        wordNum += "thousand"
        ###


        # HUNDREDS PART
        strHundreds = inpString[-3:]
        if (int(strHundreds) != 0):

            if ((int(strHundreds) // 100) != 0):
                wordNum += generatedNumbers[(int(strHundreds) // 100) - 1] + "hundred"

            wordNum += generatedNumbers[(int(strHundreds) % 100) - 1]
            # # #
    else:
        # HUNDREDS PART
        strHundreds = inpString

        if ((int(strHundreds) // 100) != 0):
            wordNum += generatedNumbers[(int(strHundreds) // 100) - 1] + "hundred"

        wordNum += generatedNumbers[(int(strHundreds) % 100) - 1]
        # # #
    print(wordNum)




