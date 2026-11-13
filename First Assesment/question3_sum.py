# Write a Python program that takes a positive integer N as input and calculates the sum of all numbers from 1 to N.



n = int(input("Enter a positive number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum of numbers is:", total)
