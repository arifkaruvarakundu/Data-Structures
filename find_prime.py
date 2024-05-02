def find_prime(limit):
    prime_numbers = []
    for num in range(2, limit + 1):
        flag = 0
        for i in range(2, num):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            prime_numbers.append(num)
    return prime_numbers

# Example: Find prime numbers between 0 and 100
result = find_prime(100)
print("Prime numbers between 0 and 100:", result)



            




