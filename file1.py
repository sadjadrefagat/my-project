# تشخیص اول بودن یک عدد طبیعی
n = int(input("Enter a natural number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is prime number.")
