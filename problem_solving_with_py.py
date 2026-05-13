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
fibonacci(13)
