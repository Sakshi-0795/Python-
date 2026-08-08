numbers  = [10,20,30,40,50,20]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicates:", duplicates)        