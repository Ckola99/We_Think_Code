# Objective is to take a string and change it's characters please search "ROT-13 python" on youtube 

# define function
def rot13(string):
  
    # list of characters that we will change
    result = []

    # loop through string character by character
    for char in string:

        # check if character is an uppercase
        if 'A' <= char <= 'Z':
            # compute ROT-13 algorithm
            result.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        # check if character is lowercase 
        elif 'a' <= char <= 'z':
            # compute ROT-13 algorithm
            result.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        # add any other character
        else:
            result.append(char)
    # create a string from our list of characters and return it        
    return ''.join(result)
