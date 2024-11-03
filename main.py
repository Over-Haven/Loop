#input
n = int(input("Enter the number whose sum you want to find: "))
sum=0

#Iterates
for i in range(1, n+1) :
    sum = sum+i 
    print("\nsum =", sum)