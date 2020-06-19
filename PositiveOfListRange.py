n = int(input ("How many elements do you want in your list ?\n "))
list =  []
output = []

for i in range (1,n+1) :
    element = int(input ("\nPlease enter the element number " + str(i) + " of the list :\n"))
    list.append(element)
    
print ("\nYour list is :\n" ,list)

for a in range (0,n) :
    
    if list [a] >= 0 :
        output.append(list [a])
    
    else :
        continue
        
print ("\nYour list with only positive elements is :\n" ,output)

How many elements do you want in your list ?
 5

Please enter the element number 1 of the list :
1

Please enter the element number 2 of the list :
-2

Please enter the element number 3 of the list :
3

Please enter the element number 4 of the list :
-4

Please enter the element number 5 of the list :
5

Your list is :
 [1, -2, 3, -4, 5]

Your list with only positive elements is :
 [1, 3, 5]

