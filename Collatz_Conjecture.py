#Collatz Conjecture Pattern
#Author: @Joshua W Smith (jws8)
#Date: 11/19/21
#Method to show Collatz pattern based off of a number
#Input: number to generate Collatz pattern
#Output:
#Range of pattern
#Iterations 
import matplotlib.pyplot as plt
import numpy as np

def collatz_conjecture(num):
    conject_list = [num]
    conj_list7 = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    iterations = 1
    #While loop to catch repetitive Collatz pattern 4-2-1
    while num > 1:
        #Number is even
        if num % 2 == 0:
            num = num//2
            #Number is odd   
        else:
            num = num*3 + 1
        iterations+=1
        conject_list.append(num)
    #numpy to arrange data 
    y = np.array(conject_list)
    x = np.arange(0, iterations)
    u = np.array(conj_list7)
    v = np.arange(0,17)
    #plt to draw
    #labels
    plt.title("Collatz Conjecture Model Given Integer")
    plt.xlabel("Iterations")
    plt.ylabel("Value")
    plt.plot(x,y, label = "collatz curve n given",linestyle ="-")
    plt.plot(v,u, label = "comparison with n = 7", linestyle ="--")
    plt.legend()
    plt.show()

#Run
num = int(input("Enter a number for the Collatz Conjecture: "))
collatz_conjecture(num)


