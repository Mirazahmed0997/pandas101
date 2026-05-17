# 1  --------check prime number-----------

def chk_prime(num):
    if num <= 1:
        print("One is Not a prime")
        return
    for i in range (2,num):
        if num % i == 0:
            print("Not prime")
            return
    print("Prime Number")

# chk_prime(5)

# 2 ------------------

def fibonacci(numb):
    arr=[0,1]
    for i in range(1,numb):
        arr.append(arr[i]+ arr[i-1])
    print(arr)

# fibonacci(7)

# 3 ---------------------
# formula (c * 9/5) + 32

def cel_to_farenheit(cel):
        conv_to_far=(cel* 9/5) + 32
        print(conv_to_far, "Farenheit")


# cel_to_farenheit(5)


# 4 --------------find the missing value in sequence array--------------------


def detect_missing(numbs):
    missing_val=[]
    for i in range (len(numbs)):
        # print(i)
        if i+1 != numbs[i]:
            missing_val=i+1
            break
        
    print(missing_val)


# detect_missing(arr)        
arr=[1,3,4,7,9]

def missing_values(numbs):
    # print(len(numbs))
    missing_vals=[]
    for i in range (1,max(numbs)):
        # print(i)
        if i not in numbs:
            missing_vals.append(i)
    print(missing_vals)



missing_values(arr)