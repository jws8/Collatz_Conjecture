#Collatz Conjecture 
#Method to show conjecture pattern based off of a number
#Iterations variable to show length vs. number given
#
def collatz_conjecture(num):
    conject_list = [num]
    #While loop to catch repetitive conjecture pattern 4-2-1
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
    print("Range of conjecture: [" + str(conject_list[0]) + ", " + 
    str(conject_list[len(conject_list) - 1]) + "]")
    print("Iterations: " + str(len(conject_list)))

#Run
num = int(input("Enter a number for the Collatz Conjecture: "))
collatz_conjecture(num)

