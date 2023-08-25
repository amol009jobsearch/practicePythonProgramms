
age=input('give me age : ')
print(type(age))
if int(age) > 18:
    print('eligible for voting')
else:
    print('Not eligible for voting')

print('----------------------')
age=input('give me age : ')
if int(age) > 0 and int(age) <= 10:
    print('1000/-')
    if int(age) == 5:
        print('age is 5 hence discount')
elif int(age) > 10 and int(age) <= 20:
    print('2000/-')
else:
    print('3000/- ')


print('----------------------')
age=input('enter age')
age = age if int(age) > 0 and int(age) <= 10 else 11
print(age)


