import text_utils as tu

def main():
    input_string = input("Enter a string: ")
    reversed_string = tu.reverse_string(input_string)
    uppercase_string = tu.uppercase_string(input_string)
    lowercase_string = tu.lowercase_string(input_string)
    
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)
    print("Uppercase String:", uppercase_string)
    print("Lowercase String:", lowercase_string)

if __name__ == "__main__":
    main()
