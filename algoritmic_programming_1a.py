from random import randint

#1
def opdracht1for():
    star = "*"
    height = int(input("how high should the pyramid be: "))
    for i in range(1, height + 1):
        print(f"{star *i}")
    for i in range(height -1, 0, -1):
        print(f"{star *i}")

def opdracht1while():
    star = "*"
    height = 5 + 1
    count = 0
    while height > count:
        print(f"{star * count}")
        count += 1
    while count != 0:
        print(f"{star * count}")
        count -= 1

def reverse_pyramid():
    star = "*"
    height = int(input("how high should the pyramid be: "))
    for i in range(height , 0, -1):
        print(f"{star *i}")
    for i in range(2, height + 1):
        print(f"{star *i}")


#2
def compare():
    text1, text2 = input("text1 :"), input("text2 :")
    for i in range(len(min(text1, text2))):
        if text1[i] != text2[i]:
            print(f"after {i +1} is when the sentence starts to differ")
        else:
            return print(f"after {min(len(text1), len(text2))} is when the sentence starts to differ")

#3
def count1(lst, number):
    count = 0
    for i in lst:
        if number == i:
            count += 1
    return count

def count2(lst):
    diff = 0
    for i in range(0, len(lst)-1):
        if lst[i+1]-lst[i] > diff:
            diff = lst[i+1]-lst[i]
    return diff

def count3(lst):
    return count1(lst, 1) > count1(lst, 0) and count1(lst, 0) < 12


#4
def palindroom(woord):
    return woord == woord[::-1]

#5
def QuickSort(lst):
    if not lst:
        return []
    else:
        pivot = (len(lst) // 2)
        pivot_value = lst[pivot]
        lesser = QuickSort([l for i, l in enumerate(lst)
                           if l < pivot_value
                            and i != pivot])

        greater = QuickSort([l for l in lst
                             if l > pivot_value])

        equal = [l for l in lst
                 if l == pivot_value]

        return lesser + equal + greater



#6
def average(lst):
    result = 0
    for i in lst:
        result += i
    return result/len(lst)

def averagelst(lst):
    result = []
    for i in lst:
        lstresult = 0
        for j in i:
            lstresult += j
        result.append(lstresult / len(i))
    return result


lst = [1, 1, 2, 3]
lst1 = [1, 1, 2, 3]
lst2 = [1, 1, 2, 3, 2, 4, 5, 8, 9]
combined = [lst, lst1, lst2]


#7
def guessnumber():
    random_number = randint(0, 10)
    print(random_number)
    number_guessed = False
    while not number_guessed:
        guess = int(input("guess a number: "))
        number_guessed = guess == random_number

#8


#9


#10
def fibonaci(n, input0=0, input1=1):
    return fibonaci(n-1, input1, input0 +input1) if n > 1 else(input0, input1) [n]

#11


#12

