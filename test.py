#print('\N{copyright sign} Hassan')
#print('\N{up down arrow} 2020')
#print('\N{left right arrow} 2021')
#print('\N{registered sign} 2022')
#print('\'Hassan\'')
#print("hassan\a")
#print('hassan\t')
#print('hassan\n')
#print('hassan\r')
#print('hassan\b')
#print('hassan\f')
#print('hassan\v')
#name=input('Enter your name:')
#age=input('Enter your age:')
#print('your name is ' + name + " and  your age is :" +age)

#age=int(input("enter your age :"))
#print(type (age))


#price=int(input("enter the price :"))
#print(type(price))


#num1=int(input('Enter first number :'))
#num2=int(input('Enter Second number :'))
#num3=input('Enter the operator :')
#print(num1 + num2 if num3== '+' else num1 - num2 if num3 =='-' else num1 * num2 if num3=='*' else num1 / num2 if num3 == '/' else 'invalid operator try again please ! ' if num3 == '/' and num2 != 0 else 'can not divide by zero ! try again please !') 


from turtle import save 




def calculator(x,y,z):
    if z =="+":
        return x+y
    elif z =="-":
        return x-y
    elif z =="*":
        return x*y
    elif z == "%":
        if y !=0:
            return x%y
    elif z == "//":
        if y != 0:
            return x//y
        else:
            return 'can not divide by  zero ! try again please !'
    else:
     return 'invalid operator try again please !'
num1=int(input('Enter first number :'))
num2=int(input('Enter Second number :'))
operator=input('Enter the operator :')
result = calculator(num1, num2, operator)
print(result)

save =input('do you want to save the result ? (y/n) :')
if save.lower() == 'y':
    with open('result.txt', 'w') as text_file:
        text_file.write(str(result))
        
    print('result saved successfully !') 
if save.lower()== 'n':
  print('result not saved !')
  




