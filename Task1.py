number = input("Enter any Number :")
size = len(number)
sum = 0

for ch in range(size):
    sum += int(number[ch]);
    
print("Sum of number is : ",sum);   
