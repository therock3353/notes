# We want to calculate if 25 is a prime or not.
# Start from 2 and go upto 25 to find all unique prime numbers between 2 to 25
# 2 -> is prime ->  all_primes_so_far = [2]
# 3 -> is prime ->  all_primes_so_far = [2, 3]
#  divide 3 by all primes so far (2)
#   since 3 cannot be divided by any of the primes found so far, 3 is a prime.
# 4 -> not prime -> all_primes_so_far = [2, 3]
#   divide 4 by all primes so far (2, 3)
#       since 4 is divided by 2 => 4 is not a prime
# 5 -> is prime -> all_primes_so_far = [2,3]
#   divide 5 by all primes so far (2, 3)
#       since 5 cannot be divided by 2 or 3, 5 is a prime.
# ...
# ...
# 11 -> is prime -> all_primes_so_far (2, 3, 5, 7)
#  divide 11 by all primes so far (2,3,5,7)
#       since 11 cannot be divided by 2, 3, 5, or 7 => 11 is a prime.
# ...
# continue this process till user provided num
def is_num_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    all_primes_so_far = []
    for intermediate_num in range(2, num+1):
        is_prime = True
        for prime_num in all_primes_so_far:
            if intermediate_num % prime_num == 0:
                is_prime = False
                break
        if is_prime is True:
            if num % intermediate_num == 0:
                return False
            all_primes_so_far.append(intermediate_num)
    if num == all_primes_so_far[-1]:
        return True
    else:
        return False

if __name__=="__main__":
    num = 49
    print(is_num_prime(num))