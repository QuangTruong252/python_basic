import random
import math
import collections
from vietnam_number import n2w

# Cau 1
def Question1():
    print('**** Question 1 ****')
    a1 = int(input('Input a: '))
    b1 = int(input('Input b: '))
    multiplication = a1*b1
    if(multiplication > 1000) :
        print('Case > 1000 --- Result:', (a1 + b1))
    else : print('Case <= 1000 --- Result:', multiplication)

# Cau 2
def Question2():
    print('**** Question 2 ****')
    n2 = int(input('Input n: '))
    listRange = list(range(0,n2))
    sum = 0
    for number in listRange:
        sum += number
    print("listRange:" , listRange)
    print("Sum:" , sum)

# Cau 3
def Question3():
    print('**** Question 3 ****')
    str3 = input('Input string: ')
    for index, char in enumerate(str3):
        if(index % 2 == 0):
            print(char,end=' ')        
    print('\n')

# Cau 4
def Question4():
    print('**** Question 4 ****')
    str4 = input('Input string: ')
    n4 = int(input('Input n: '))
    print('Last n char on string:', str4[len(str4) - n4:])

# Cau 5
def Question5():
    print('**** Question 5 ****')
    print('---- Note: Input must have spaces between numbers')
    print('---- Example: 1 2 1 3 1')
    list5 = [int(x) for x in input("Input list n number: ").split()]
    if(type(list5) == list and len(list5) > 1): 
        print('List n is: ', list5)
        if(list5[0] == list5[len(list5) - 1]): print('Result: ',True)
        else : print('Result: ', False)
    else:
        print('Error, please retype')
        Question5()

# Cau 6
def Question6():
    print('**** Question 6 ****')
    n6 = int(input('Input n: '))
    ranNumber = sorted(random.sample(range(100),n6))
    print('Range List:',ranNumber)
    def isPrimeNumber(n):
        if (n < 2):
            return False
        squareRoot = int(math.sqrt(n))
        for i in range(2, squareRoot + 1):
            if (n % i == 0):
                return False
        return True
    for number in ranNumber:
        if(isPrimeNumber(number)): print('Number Prime:', number)

# Cau 7
def Question7():
    print('**** Question 7 ****')
    str7 = input('Input string: ')
    listStr7 = []
    for char in str7:
        if(char.islower()): listStr7.append(char.upper())
        else : listStr7.append(char.lower())
    reversedStr = ''.join(reversed(listStr7))
    print(reversedStr)

# Cau 8
def Question8():
    print('**** Question 8 ****')
    n8 = int(input('Input n: '))
    listNumber = sorted(random.sample(range(100),n8))
    print('Range List:',listNumber)

    with open("f.txt",'w',encoding = 'utf-8') as f:
        for index, number in enumerate(listNumber):
            listSpace = []
            for i in range(0,index):
                listSpace.append('')
            listWrite = listSpace + list([str(number)]) + ['\n']
            write = " ".join([str(char) for char in listWrite])
            f.writelines(write)
                
    text = open('f.txt')
    print('Content in the file after writing:')
    print(text.read())
    text.close()

# Cau 9
def Question9():
    print('**** Question 9 ****')
    file = open("f.txt")
    print('Content in the file:')
    print(file.read())
    file.seek(0)
    sum = 0
    listInt = []
    for line in file.readlines():
        listInt.append(int(line))
        sum += int(line)
    expression = " + ".join([str(char) for char in listInt])
    print('Result: ', expression , ' = ' , sum)
    file.close()

# Cau 10
def Question10():
    print('**** Question 10 ****')
    with open("f.txt",'r',encoding = 'utf-8') as f:
        print('Content in the file before write:')
        print(f.read())
    with open("f.txt",'a',encoding = 'utf-8') as f:
        f.write('Lập trình ứng dụng WEB\n')
    with open("f.txt",'r',encoding = 'utf-8') as f:
        print('Content in the file after write:')
        print(f.read())

# Cau 11
def Question11():
    print('**** Question 11 ****')
    list11 = [int(input("Enter the " + str(i) + " element: ")) for i in range(10)]
    list_no_overlap = [number for number, v in collections.Counter(list11).items() if v <= 1]
    print("List number no overlap:",list_no_overlap)
    with open("f.txt",'a',encoding = 'utf-8') as f:
        f.write(" ".join([str(char) for char in list_no_overlap]))
    with open("f.txt",'r',encoding = 'utf-8') as f:
        print('Content in the file after write:')
        print(f.read())

# Cau 12
def Question12():
    print('**** Question 12 ****')
    n12 = int(input('Enter n number: '))
    listNumber12 = sorted(random.sample(range(10000000),n12))
    print('Range List:',listNumber12)
    listString12 = []

    with open("input.txt",'w',encoding = 'utf-8') as f:
        for number in listNumber12:
            numberWrite = list([str(number)]) + ['\n']
            writeInput = " ".join([str(char) for char in numberWrite])
            f.writelines(writeInput)

    with open("input.txt",'r',encoding = 'utf-8') as f:
        for line in f.readlines():
            listString12.append(n2w(line[0:len(line) - 2]))


    with open("output.txt",'w',encoding = 'utf-8') as f:
        for string in listString12:
            stringWrite = list([str(string)]) + ['\n']
            writeOutput = " ".join([str(char) for char in stringWrite])
            f.writelines(writeOutput)

    with open("output.txt",'r',encoding = 'utf-8') as f:
        print('Content in the output.txt:')
        print(f.read())

def switch(x):
    if (x == 1): Question1()
    elif (x == 2): Question2()
    elif (x == 3): Question3()
    elif (x == 4): Question4()
    elif (x == 5): Question5()
    elif (x == 6): Question6()
    elif (x == 7): Question7()
    elif (x == 8): Question8()
    elif (x == 9): Question9()
    elif (x == 10): Question10()
    elif (x == 11): Question11()
    elif (x == 12): Question12()
    else: print("Please choose the number that corresponds to the question!!!")

def app():
    print("List question:")
    for x in range(1,13):
        print(x,"<=> Question", x )
    question = int(input("Select question:"))
    switch(question)
    is_continue = input("Continues (yes/no):")
    if(is_continue == 'yes'):
        app()
    else: print('See you again!!!')

app()


