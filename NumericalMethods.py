from math import *
def f(x):
    return (x ** 4)-x-10

def g(x):
    return (x+10)**0.25

def derivative(x):
    return (4*(x**3))-1

def BisectionMethod(lower_limit,upper_limit):
    print('--------------Bisection Method--------------')
    a=lower_limit
    b=upper_limit
    m=0
    thelist=[]
    for i in range(20):
        m=round((a+b)/2,4)
        if f(m) * f(a) < 0 :
            b=m
        if f(m) * f(b) < 0:
            a=m
        thelist.append(m)
        print(m,end=', ')
        if thelist[i]==thelist[i-1] and i>=1:
            break
    print('\nInterval chosen=[',lower_limit,',',upper_limit,']')
    print('Answer using Bisection Method=',m,'(No.of iterations taken=',i+1,')',sep='')

def NRMethod(guess):
    print('--------------Newton Raphson Method--------------')
    x=guess
    i=0
    thelist=[]
    for i in range(20):
        x -= ( f(x)/derivative(x) )
        x=round(x,4)
        thelist.append(x)
        print(x,end=', ')
        if thelist[i]==thelist[i-1] and i>=1:
            break
    print('\nGuess value chosen=',guess)
    print('Answer using Newton Raphson Method=',x,'(No.of iterations taken=',1+i,')',sep='')

def SecantMethod(x0,x1):
    print('--------------Secant Method--------------')
    lower_limit=x0
    upper_limit=x1
    for i in range(20):
        y=x1
        try:
            x1 = x1 - (((x1-x0)*f(x1)) / (f(x1)-f(x0)) )
        except:
            break
        x1=round(x1,4)
        x0=round(y,4)
        print(x1,end=', ')
    print('\nInterval chosen=[',lower_limit,',',upper_limit,']')
    print('Answer using Secant Method=',x1,'(No.of iterations taken=',i,')',sep='')

def RegulaFalsi(lower_limit,upper_limit):
    print('--------------False Position Method--------------')
    x0=lower_limit
    x1=upper_limit
    thelist=[]
    for i in range(20):
        y=((x0 * f(x1)) - (x1 * f(x0)))/( f(x1) - f(x0) )
        y=round(y,4)
        if f(y) * f(x1) < 0 :
            x0=y
        if f(y) * f(x0) < 0:
            x1=y
        thelist.append(y)
        print(y,end=', ')
        if thelist[i]==thelist[i-1] and i>=1:
            break
    print('\nInterval chosen=[',lower_limit,',',upper_limit,']')
    print('Answer using Regula Falsi(False Position) Method=',y,'(No.of iterations taken=',1+i,')',sep='')

def SFPI(x):
    print('--------------Fixed Point Iteration Method--------------')
    thelist=[]
    guess=x
    for i in range(20):
        x=g(x)
        x=round(x,4)
        thelist.append(x)
        print(x,end=', ')
        if thelist[i]==thelist[i-1] and i>=1:
            break
    print('\nGuess value chosen=',guess)
    print('Answer using Fixed Point Iteration Method=',x,'(No.of iterations taken=',i+1,')',sep='')

print('The precision is set to 4 decimals and the equation is "x^4-x-10=0".')
BisectionMethod(0,2)
NRMethod(1)
SFPI(4)
SecantMethod(0,2) 
RegulaFalsi(0,2)