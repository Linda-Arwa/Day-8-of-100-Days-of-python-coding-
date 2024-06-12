# A program that checks if a number is a prime number or not
# A prime number is a number that is only cleanly divisible by 1 and itself

# Solution

def prime_number(number):
    
    is_prime = True
    
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is Not a prime number")
            
        
# User input

test_number = int(input("Enter a number\n"))
prime_number(test_number)