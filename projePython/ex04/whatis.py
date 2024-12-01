import sys
def whatis():
        try:
            if len(sys.argv) == 1:
                 return
            elif len(sys.argv) == 2:
                number = int(sys.argv[1])
            elif len(sys.argv) > 2:
                raise Exception("AssertionError: more than one argument is provided")


            if number >= 0:
                print("I'm Even")
            elif number < 0:
                print("I'm Old")
        except ValueError:
             print("AssertionError: argument is not an integer")
        except Exception as e:
            print(f"{e}")


whatis()