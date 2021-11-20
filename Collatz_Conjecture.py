#Collatz Conjecture Pattern
#Author: @Joshua W Smith (jws8)
#Date: 11/19/21
#Method to show Collatz pattern based off of a number
#Input: number to generate Collatz pattern
#Output:
#Iterations to show length vs. num 
#Range of pattern

def collatz_conjecture(num):
    conject_list = [num]
    #While loop to catch repetitive Collatz pattern 4-2-1
    while num > 1:
        #Number is even
        if num % 2 == 0:
            num = num//2
        #Number is odd   
        else:
            num = num*3 + 1
        conject_list.append(num)

    print(conject_list)
    conject_list.sort()
    print("Range of Collatz Conjecture: [" + str(conject_list[0]) + ", " + 
    str(conject_list[len(conject_list) - 1]) + "]")
    print("Iterations in Collatz Conjecture: " + str(len(conject_list)))

#Run
num = int(input("Enter a number for the Collatz Conjecture: "))
collatz_conjecture(num)

