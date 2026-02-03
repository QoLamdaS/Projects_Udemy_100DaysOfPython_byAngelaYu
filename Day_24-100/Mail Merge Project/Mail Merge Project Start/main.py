
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("Day_24-100\\Mail Merge Project\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_file:
#! Must type double backslashes instead of a single backslash for copy-paste file relative paths on my VScode Windows. I have no idea =)
    the_names = names_file.readlines() #* Transform from a txt file into a Python list of names
    
with open("Day_24-100\\Mail Merge Project\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for i in the_names:
        stripped_name = i.strip() #* Remove the \n from each name
        new_letter = letter_contents.replace("[name]", stripped_name) #* Replace the [name] placeholder with the actual intended name
        with open(f"Day_24-100\\Mail Merge Project\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)