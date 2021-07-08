tel_number = input("Enter 10 digit Telephone Number in the format of 555-GET-FOOD : ")

while(len(tel_number)!= 12):
    
    print("Please enter 10 digit TelPhone Number in the format of 555-GET-FOOD : ")
    tel_number = input()
    
my_dictionary = dict();
my_dictionary["A"] = "2"
my_dictionary["B"] = "2"
my_dictionary["C"] = "2"
my_dictionary["D"] = "3"
my_dictionary["E"] = "3"
my_dictionary["F"] = "3"
my_dictionary["G"] = "4"
my_dictionary["H"] = "4"
my_dictionary["I"] = "4"
my_dictionary["J"] = "5"
my_dictionary["K"] = "5"
my_dictionary["L"] = "5"
my_dictionary["M"] = "6"
my_dictionary["N"] = "6"
my_dictionary["O"] = "6"
my_dictionary["P"] = "7"
my_dictionary["Q"] = "7"
my_dictionary["R"] = "7"
my_dictionary["S"] = "7"
my_dictionary["T"] = "8"
my_dictionary["U"] = "8"
my_dictionary["V"] = "8"
my_dictionary["W"] = "9"
my_dictionary["X"] = "9"
my_dictionary["Y"] = "9"
my_dictionary["Z"] = "9"
my_dictionary["-"] = "-"
   
concat_string = "555"

for ch in range(len(tel_number)-9 , len(tel_number)):
        
    if(tel_number[ch] in my_dictionary):
        concat_string += my_dictionary[tel_number[ch]]        
tel_number = concat_string        
print(tel_number)        