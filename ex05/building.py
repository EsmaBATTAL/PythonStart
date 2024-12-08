import sys

def building(input):
    try:
        totalchar_count = len(input)
        print(f"The text contains {totalchar_count} characters:")
        uppercase_count = sum(1 for char in input if char.isupper())
        print(f"{uppercase_count} upper letters")
        lowercase_count = sum(1 for char in input if char.islower())
        print(f"{lowercase_count} lower letters")
        punctuation_count = sum(1 for char in input if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
        print(f"{punctuation_count} punctuation marks")
        space_count = sum(1 for char in input if char.isspace())
        print(f"{space_count} spaces")
        digit_count = sum(1 for char in input if char.isdigit())
        print(f"{digit_count} digits")
    except EOFError:
        print("\nEnd of input detected. Program terminated.")

def main():
    try:
        if len(sys.argv) == 1:
            building(sys.stdin.read())

        if len(sys.argv) == 2:
           building(sys.argv[1])
        else:
             raise Exception("Only one argument is allowed.")
           
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()