iNumber = int(input("Input number: "))
x = 1
for i in range(6):
    if i >= 1:
        x = x * 2
    pNumber = iNumber * x
    print(f"The answer is: {pNumber}")