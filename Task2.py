msg = str(input("Enter String :"))
msg1 = {#capital alphabets morse codes
    'A' : '.-'  , 'B' : '-...', 'C' : '-.-.',
    'D' : '-..' , 'E' : '.'   , 'F' : '..-.',
    'G' : '--.' , 'H' : '....', 'I' : '..'  ,
    'J' : '.---', 'K' : '-.-' , 'L' : '.-..',
    'M' : '--'  , 'N' : '-.'  , 'O' : '---' ,
    'P' : '.--.', 'Q' : '--.-', 'R' : '.-.' ,
    'S' : '...' , 'T' : '-'   , 'U' : '..-' ,
    'V' : '...-', 'W' : '.--' , 'X' : '-..-',
    'Y' : '-.--', 'Z' : '--..',
     'a' : '.-'  , 'b' : '-...', 'c' : '-.-.',
    'd' : '-..' , 'e' : '.'   , 'f' : '..-.',
    'g' : '--.' , 'h' : '....', 'i' : '..'  ,
    'j' : '.---', 'k' : '-.-' , 'l' : '.-..',
    'm' : '--'  , 'n' : '-.'  , 'o' : '---' ,
    'p' : '.--.', 'q' : '--.-', 'r' : '.-.' ,
    's' : '...' , 't' : '-'   , 'u' : '..-' ,
    'v' : '...-', 'w' : '.--' , 'x' : '-..-',
    'y' : '-.--', 'z' : '--..',
    ',' : '--..--',
    '.' : '.-.-.-',
    '?' : '..--..',
    ';' : '-.--'  ,
    ':' : '---..' ,
    '-' : '-....-',
    "'" : '.----.',
    '(' : '-.--.' ,
    '1' : '.----' , '2' : '..---' , '3' : '...--',
    '4' : '....-' , '5' : '.....' , '6' : '....-',
    '7' : '--...' , '8' : '---..' , '9' : '----.',
    '0' : '-----'
}
for i in msg:
    if i in msg1:
        print(msg1[i])
    else:
        print("while")