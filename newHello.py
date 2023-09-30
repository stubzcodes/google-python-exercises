# import module

import sys

# main function

def main():
    print("Hello there", sys.argv[1], sys.argv[2])
    #Command line args = sys.argv[1], sys.argv[2], etc
    #sys.argv[0] is the script name itself and can be ignored

#Standard boilerplate to call the main() function to begin the program

if __name__ == '__main__':
    main()