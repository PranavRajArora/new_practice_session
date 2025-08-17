# This program prints numbers from 1 to 10
# and specifies whether each number is even or odd.

for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
