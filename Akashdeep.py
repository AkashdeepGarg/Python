print("This is a python programme for a calculator.")
print('press 1 for code of sequential approach ')
print('press 2 for code of conditional approach ')
print('press 3 for code of iterational approach')
print('press 4 for code of string approach')
print('press 5 for code of list approach')

choice =int(input('enter your choice: '))
if choice==1:
    print('you have selected sequential approach to check the multiplication of two numbers ')
    n1=float(input('enter first number: '))
    n2=float(input('enter second number: '))
    multiplication=n1*n2
    print('the product of entered numbers is= ',multiplication)

elif choice==2:
    print('you have selected conditional approach to check wether a nuber is even or odd ')
    n=int(input('enter a number: '))
    if n%2==0:
        print('even number')
    else:
        print('odd number')

elif choice==3:
    print('you have selected iterational approach. Select any one of the two ')
    choose =int(input('1)FOR loop\n2)WHILE loop '))
    if choose==1:
        print('FOR loop selected')
        num=int(input('enter a number to get the sum of numbers while approaching given number: '))
        sum=0
        for i in range (1,num+1):
            sum+=i
        print(sum)
    elif choose==2:
        print('WHILE loop selected')
        n=1
        j=int(input('enter a number: '))
        while n<=j:
            print(n)
            n+=1
    else:
        print('invalid choice')

elif choice==4:
    print('you have selected string  approach ')
    string=str(input('enter a string '))
    print('length of entered string is = ',len(string))
    index=int(input('enter no of  your choice: '))
    if index<=string:
        print('the character in the string for your chosen no is = ',string[index])
    else:
        print('out of string')
    

elif choice==5:
    print('list approach selected ')
    l1=[]
    b=int(input('enter number of elements in the list: '))
    print('Enter the values of the elements ')
    for i in range (1,b+1):
        ele=input()
        l1.append(ele)
    print(l1)

else :
    print('invalid choice')
print("Thank you")

        
        
    
            
            
    
