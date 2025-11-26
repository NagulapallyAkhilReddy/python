#TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as names:
    list_of_names=names.readlines()
    for name in list_of_names:
        with open("./Input/Letters/starting_letter.txt") as letter:
            letter_content = letter.read()
        letter_content=letter_content.replace("[name]",f"{name.strip("\n")}")
        with open(f"./Output/ReadyToSend/letter_for_{name.strip("\n")}.txt","w") as individual_letter:
            individual_letter.write(letter_content)
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp