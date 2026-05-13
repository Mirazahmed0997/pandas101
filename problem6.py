
# 1 -----------------



def odd_even_detector(a):
    if a%2==0:
        print('Even number') 
    else:
        print('Odd number') 


# odd_even_detector(7)



# 2 -------------------

numbers= [10,25,15]

def max_numb(arr):
    print(max(arr))
    print(len(arr))

# max_numb(numbers)

# 3 --------------------

def factorial_numb(num):
    fact=1
    for i in range(1, num+1, 1):
        fact= i * fact
    print(fact)
            

# factorial_numb(5)

# 4 --------------------

def reverse_string(str):
    print(str[::-1])

# reverse_string('Miraz ahmed') 


# 5 ------------------------
char='Programming'

def vowels_count(str):
    count=0
    for i in str:
        if i in 'aeiou':
            count +=1

    print(count)

# vowels_count(char)

# 6 ------------------------

char='madam'

def chk_Palindrome(str):
    if str == str[::-1]:
        print("Palindrome")
    else:
        print("not Palindrome")

# chk_Palindrome(char)

#7 --------------------------

lists=[1,2,3,4,5]

def total(numbs):
    total=sum(numbs)
    print(total)


#using loop

def total_loop(numbs):
    total=0
    for i in range (len(numbs)):
        total+=numbs[i]
    print(total)    
        

# total_loop(lists)  

# 8 --------------------------
def chk_max(numbs):
    max_numb=max(numbs)
    print(max_numb) 

# chk_max(lists)

# 9 ---------------------------

number=[1,2,3,3,4,5,5,6,6]

def rmv_dup(num):
    
    for i in range (len(num)-2,-1,-1):
        if num[i] == num[i+1]:
            num.pop(i)
        
    print(num)


# rmv_dup(number)

        

    
