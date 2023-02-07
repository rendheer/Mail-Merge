#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import time
with open("Input/Names/invited_names.txt", mode="r") as names:
    lines = names.readlines()
    for line in lines:
        print(line)
        filename = f"letter_for_{line.strip()}.txt"
        print(filename)
        with open("Input/Letters/starting_letter.txt") as template:
            verbiage = template.read()
            letter = verbiage.replace("[name]", line.strip())
            print(verbiage)
            print(letter)
            path = f"Output/ReadyToSend/{filename}"
            print(path)
            with open(path, mode="a") as new_file:
                new_file.write(letter)


