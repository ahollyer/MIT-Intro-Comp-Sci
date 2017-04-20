# userfile.py
#   Program to create a file of usernames in batch mode

def main():

    print("This program creates a file of usernames")
    print("from a file of names.")

    # get the file names
    in_file_name = input("What file are the names in? ")
    out_file_name = input("What file should the usernames go in? ")

    # open the files
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    #process each line of the input file
    for line in in_file:
        # get first and last names from line
        first, last = line.split()
        # create username
        username = (first[0] + last[:7]).lower()
        # write username to output file
        print(username, file=out_file)

    # close both files
    in_file.close()
    out_file.close()

    print("Usernames have been written to", out_file_name)

main()
