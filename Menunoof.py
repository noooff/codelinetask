"""Ensure you are running the script in a terminal or command prompt that supports 
interactive input. Some integrated development environments (IDEs) and text editors 
may not provide a proper input interface"""
def print_pattern():
    try:
        num = int(input("\033[31mOption: 1 \n \033[37mEnter the number of rows for the pattern:\033[31m "))
        print("\033[31mOutput:\033[37m")
        if num > 0:
            for i in range(num, 0, -1):
                print("* " * i)
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def rotate_array():
    print("\033[31mOption 2")
    try:
        n = int(input("\033[37mEnter the number \033[34mof \033[37melements (n): \033[31m"))
        k = int(input("\033[37mEnter the number \033[34mof \033[37msteps (k):\033[31m "))
        array = [int(x) for x in input("\033[0mEnter the array elements seperated \033[34mby \033[37mspaces: \033[31m").split()]
        rotated_array = [0] * n
        for i in range(n):
            rotated_array[(i + k) % n] = array[i]

        print("\033[31mOutput:\033[37m", rotated_array)
    except ValueError:
        print("Invalid input. Please enter correct value for number of Element, Steps and Array.")
    except:
        print("Invalid input. Enter Array Element corectly")

def display_help():
    print("\033[31mOption: 3")
    print(" \033[37m--- Help ---")
    print("\033[34mOption \033[31m1: \033[0mPrint a pattern: with \033[2m'n' rows of decreasing asterisks.\033[0m")
    print("\033[34mOption \033[31m2: \033[0mRotate an array of \033[2m'n' element to right by 'k' steps.\033[0m")
    print("\033[34mOption \033[31m3: \033[0mDisplay this help message.")
    print("\033[34mOption \033[31m4: \033[0mExit the program.")

def main():
    print("\nWelcome \033[34mto \033[37mthe Menu-Based program!")
    print("\nPlease \033[34mselect \033[37man \033[34moption: \033[37m ")
    print("\033[91m1. \033[37mPrint Pattern")
    print("\033[91m2. \033[37mRotate Array")
    print("\033[91m3. \033[37mHelp")
    print("\033[91m4. \033[34mExit")
    exit_program = False

    while not exit_program:
       
        choice = input("\n\033[37mPlease \033[34mselect \033[37man \033[34moption\033[37m: ")

        if choice == '1':
            print_pattern()
        elif choice == '2':
            rotate_array()
        elif choice == '3':
            display_help()
        elif choice == '4':
            exit_program = True
            print("\033[31mOption: 4 \033[0m ")
            print("\n\nExiting the program. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
