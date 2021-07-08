def capitalized(type1):
    print(type1)
    
    
original_string = input("Enter any String : ")
size = len(original_string)
temp = ""
capital_text = ""

temp += original_string[0].capitalize();

for ch in  range(1,size):
     
    if(original_string[ch] == "." or original_string[ch] == "?"):
        
        i = 1
        
        temp+= original_string[ch]
        
        if ((ch+1) < size and (ch+2) < size):
            
            while(original_string[ch+i] == " "):
                
                capital_text += original_string[ch+2].capitalize()
                i = i+1;
               
    else:
        if(capital_text == original_string[ch].capitalize()):
            temp += capital_text
            capital_text = ""
        else:
            temp += original_string[ch]
    
capitalized(temp)