import sys

def sos(input):
    ft_dict ={
        " " : "/ ",
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----"
    }
    output = ""
    try:
        for char in input:
            if char.isalpha() or char.isdigit():
                for k in ft_dict:
                    if (k == char or k.lower() == char):
                        output+=ft_dict[k]
            else:
                output = ""
        print(output)
    except Exception as e:
        print(f"{e}")

def main():
    try:
        sos(sys.argv[1])
    except Exception as e:
        print(f"{e}")
if __name__ == "__main__":
    main()