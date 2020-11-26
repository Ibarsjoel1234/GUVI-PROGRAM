def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    print(fact)
    
    
a = int(input())
factorial(a)
