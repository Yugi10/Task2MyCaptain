def fibonacci(n) :
    
    a = 0
    b = 1
    
    if n <= 0 :
        print ("The number entered is negative or zero and so, no series is possible")
        
    elif n == 1 :
        print (a)
    
    else :
        print (a)
        print (b)
        
        for i in range (2,n) :
            c = a + b
            a = b
            b = c
            print (c)
            
n = int(input("Enter the number of 'fibonacci numbers' to be printed :\n"))
print ("\nThe fibonacci series of first " + str (n) + " numbers is : \n")
fibonacci (n)
        
Enter the number of 'fibonacci numbers' to be printed :
10

The fibonacci series of first 10 numbers is : 

0
1
1
2
3
5
8
13
21
34
