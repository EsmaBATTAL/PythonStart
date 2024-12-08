import sys

def sos(input):
    ft_dict ={
        " " : "/ ", "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".",
        "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-",
        "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-",
        "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-",
        "Y" : "-.--", "Z" : "--..", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", 
        "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "0" : "-----"
    }
    output = ""
    check = True
    for char in input:
        if char.isalnum() or char.isspace():
            check = True
        else:
            check = False
            break
    
    if check == True:
        for char in input:
            for k in ft_dict:
                if (k == char or k.lower() == char):
                        output+=ft_dict[k]
                        output += " "
        print(output)
    else:
        raise Exception("AssertionError: the arguments are bad")

def main():
    try:
        if len(sys.argv) == 2:
            sos(sys.argv[1])
        else:
            raise Exception("AssertionError: the arguments are more")
    except Exception as e:
        print(f"{e}")
if __name__ == "__main__":
    main()