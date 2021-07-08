original_string = input("Enter any String : ")
size = len(original_string) - 1
concat_string = ""

for i in range(size + 1):
    concat_string += original_string[size - i]
    print(concat_string)