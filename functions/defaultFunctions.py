def additionOfTwoNumnersWithoutParams():
    print("addition ")


additionOfTwoNumnersWithoutParams()

def additionOfTwoNumners(num1,num2):
    print("addition ",num1+num2)


additionOfTwoNumners(10,20)
'''
a=10
b=20
additionOfTwoNumners(a,b)
'''


def additionOfTwoNumnersDefaultPram(num1=200,num2=100):
    print("addition ",num1+num2)


additionOfTwoNumnersDefaultPram()


def additionOfTwoNumnersDefaultPram(num1=200,num2=100):
    print("addition ",num1-num2)

#additionOfTwoNumnersDefaultPram(num1=500,num2=600)

additionOfTwoNumnersDefaultPram(500,num2=600)
#additionOfTwoNumnersDefaultPram(num1=500,600)  #SyntaxError: positional argument follows keyword argument

def testrecurrsiveFunction(num1):
    print('number = ',num1)
    next=num1-1
    if(next>0):
        testrecurrsiveFunction(next)

testrecurrsiveFunction(5)


def fun():
   global a
   a = 10
   print("a from inside function is :",a)

fun()
print("a from outside function is :",a)
