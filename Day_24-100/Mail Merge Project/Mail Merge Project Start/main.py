
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("Day_24-100\\Mail Merge Project\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_file:
#! Must type double backslashes instead of a single backslash for copy-paste file relative paths on my VScode Windows. I have no idea =)
    the_names = names_file.readlines()
    
print(the_names)