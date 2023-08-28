def additionOfTwoNumnersWithoutParams():
    print("addition ")


additionOfTwoNumnersWithoutParams()

def additionOfTwoNumners(num1,num2):
    print("addition ",num1+num2)


additionOfTwoNumners(10,20)

a=10
b=20
additionOfTwoNumners(a,b)


def additionOfTwoNumnersDefaultPram(num1=200,num2=100):
    print("addition ",num1+num2)

additionOfTwoNumnersDefaultPram()


def additionOfTwoNumnersDefaultPram(num1=200,num2=100):
    print("addition ",num1-num2)

#additionOfTwoNumnersDefaultPram(num1=500,num2=600)

additionOfTwoNumnersDefaultPram(500,num2=600)
#additionOfTwoNumnersDefaultPram(num1=500,600)  #SyntaxError: positional argument follows keyword argument