import random
a=eval(input('Set a range(min)='))
b=eval(input('Set a range(max)='))
ans=random.randint(a,b)
print(f'The password is generated,the answer is between {a}~{b}')
peo=eval(input('Guess a number='))
count=1
while peo!=ans:
    if peo>ans:
        print('The number is too big')
        b=peo-1
        print(f'The password is generated,the answer is between {a}~{b}')
        peo=eval(input('Guess a number='))
        count=count+1
    elif peo<ans:
        print('The number is too small')
        a=peo+1
        print(f'The password is generated,the answer is between {a}~{b}')
        peo=eval(input('Guess a number='))
        count=count+1
print(f'Congratulations you got the password，you has been guess {count} times')
