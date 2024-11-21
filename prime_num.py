n = int(input("Enter a number: ")) 

if n <= 1:
    print(n, "is not a Prime Number")
elif n == 2:
    print(n, "is a Prime Number")
elif n % 2 == 0:
    print(n, "is Prime Number")
