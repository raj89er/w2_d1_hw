# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

num = 1
cubed = []

while True:
    all_cubed = num ** 3
    if all_cubed >=1001:
        break
    else:
        cubed += [all_cubed]
        num += 1
print(cubed)

# Exercise #2
# Get first prime numbers up to 100

for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1): # I do not understand the math part of this code. I got help from my friend who tried their best to explain this line, but to no avail.
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input("What is your age?"))
if age <= 17:
    print("Kids - Where are your parents?")
elif age >= 66:
    print("Seniors: Tonight is not bingo, come another night.")
else:
    print("Adult: Do you know where you're kids are?")