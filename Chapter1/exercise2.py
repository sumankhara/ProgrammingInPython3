numbers = []
count = 0
total = 0

while True:
    line = input("Enter a number or just Enter/Return to finish: ")
    if line:
        try:
            number = int(line)
        except ValueError as error:
            print(error)
            continue
        numbers.append(number)
        count += 1
        total += number
    else:
        break

if count:
    minimum = numbers[0]
    maximum = numbers[0]
    for value in numbers:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
    print("numbers: ", numbers)
    print("Count = ", count, "Sum = ", total, "Lowest = ", minimum, "Highest = ", maximum, "Mean = ", total / count)


