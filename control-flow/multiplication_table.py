#multiplication table of a number from 1 to 10 using for loop
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")