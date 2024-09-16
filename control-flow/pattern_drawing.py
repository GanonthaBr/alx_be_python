# Utilize while loops and nested for loops to draw a simple text-based pattern
row = int(input("Enter the size of the pattern: "))

while(row):
    for i in range(row):
        print("*", end=" ")
    print("")
    row-=1