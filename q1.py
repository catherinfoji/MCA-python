#1. LIST
#Write a PYTHON script with List comprehension for the following
#• Is the given list divisible by 3 or NOT?
#• Square of even numbers in a list
# Sum of digits of all EVEN numbers in a list
#• Remove duplicate numbers in a list
#a
list=[2,4,5,6,9,8,10]
for x in list:
    if x%3==0:
        print("list divisible by 3")
        break
else : 
    print("list not divisible by 3") 
#b
result = [x**2 for x in list if x%2==0]
print(result)

#c
sum = 0 
for x in list:  
    if   x% 2==0:  
        sum += x
print(sum)

            
#d         
uni=[]
for x in list:
    if x not in uni:
        uni.append(x)
print("the list after removing duplicates:",uni) 

            
