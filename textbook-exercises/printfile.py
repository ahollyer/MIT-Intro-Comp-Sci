# printfile.py
# Prints the contents of a file to the screen

def main():
    file_name = input("Enter the filename: ")
    in_file = open(file_name, "r")
    data = in_file.read()
    print(data)

main()
