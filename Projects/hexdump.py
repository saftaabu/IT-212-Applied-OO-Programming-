# HexDump Utility
# Display characters in a file in both hex and character.

# Load file into the string chars.
filename = input("Enter filename: ")
f = open(filename, "rb")
chars = f.read( )

# Start at line 0
line = 0

# Get number of characters in file.
file_len = len(chars)

while line <= file_len:

    # Find maximum index of line.
    max_index = min(line + 16, file_len)
    
    # Print line number in hex.
    print("{0:05x} ".format(line), end="")
	
    # Print byte in hex.
    for index in range(line, max_index):
        print("{0:02x} ".format(chars[index]), end="")
    print( )
		
    # Print character in line.
    print("      ", end="")
    for index in range(line, max_index):
        if chars[index] == 0x7f:
            print("^? ", end="")
        elif chars[index] >= 0x80:
            print(" . ", end="")
        elif chars[index] >= 0x20:
            print(" " + chr(chars[index]) + " ", end="")
        elif chars[index] == ord("\a"):
            print("\\a ", end="")
        elif chars[index] == ord("\b"):
            print("\\b ", end="")
        elif chars[index] == ord("\f"):
            print("\\f ", end="")
        elif chars[index] == ord("\n"):
            print("\\n ", end="")
        elif chars[index] == ord("\r"):
            print("\\r ", end="")
        elif chars[index] == ord("\t"):
            print("\\t ", end="")
        elif chars[index] == ord("\v"):
            print("\\v ", end="")
        elif chars[index] == ord("\a"):
            print("\\a ", end="")
        else:
            print("^{0} ".format(chr(chars[index] + 0x40)), end="")
    print( )
  
    # Go to next line.
    line += 16

# Close input file.
f.close( )
