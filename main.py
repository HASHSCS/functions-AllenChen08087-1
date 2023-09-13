def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
    pass  # Implement your solution here
    return number*number
    


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    pass  # Implement your solution here
    r=""
    l = len(s) -1
    for i in range (l,-1,-1):
        r = r +s[i]
    return r


def is_prime(n):
    """
    This function takes a number as input and returns True if the number is prime, otherwise False.
    :param n: int
    :return: bool, True if the number is prime, otherwise False
    """
    pass  # Implement your solution here
    
    prime = True
    for i in range (2,(n),1):
        if n%i == 0:
            prime=False
    return(prime)

    

def factorial(n):
    """
    This function takes a number as input and returns its factorial.
    :param n: int
    :return: int, the factorial of the input number
    """
    pass  # Implement your solution here
    l =1
    for i in range (n,0,-1):
        l = l*i
    return (l)
    

def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    pass  # Implement your solution here
    l = lst[1]
    for i in (lst):
        if (i > l):
            l = i
    return l
    

def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    pass  # Implement your solution here
    if n%2 == 0:
        return ("Even")
    if n%2 != 0:
        return("Odd")

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    pass  # Implement your solution here
   
    f = ""
    for i in range (len(s)-1,-1,-1):
        f = f + s[i]
    if (s == f):
        haha = True
        return haha
    if (s != f):
        haha = False
        return haha


def find_gcd(a, b):
    """
    This function takes two positive integers `a` and `b` and returns their greatest common divisor (GCD).
    
    :param a: int
    :param b: int
    :return: int, the greatest common divisor of `a` and `b`.
    """
    pass  # Implement your solution here
    l = 1
    if (a < b): 
        g =a
    if (b<a):
        g = b
    for i in range (1,g,1):
        if (a%i == 0) and (b%i == 0):
            l = i
    return l


