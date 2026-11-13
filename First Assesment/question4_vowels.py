# Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) present in the string.




text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1

print("Total vowels:", count)
