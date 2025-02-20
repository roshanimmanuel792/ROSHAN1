print("urk24cs1268")
def is_perfect_number(n):
    """Function to check if a number is perfect."""
    if n < 1:
        return False
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

num=int(input("enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")


2.print('URK24CS1268')
def is_happy_number(n):
    """Function to check if a number is a Happy Number."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1 

num=int(input("enter a number:"))
if is_happy_number(num):
    print(f"{num} is a Happy Number.")
else:
    print(f"{num} is not Happy Number.")




3.def fun1(*numbers):
    if not numbers:
        print("no numbers providewd")
        return
    last_num = numbers[-1]
    divisors = [i for i in range(1, last_num +1) if last_num % i == 0]
    print(f"{last_num} :"," ".join(map(str,divisors)))

    #sample function calls
    fun1(6,7,8)
    fun1(1,2,5,7,9)
    fun1(1,3,5,7,9)
