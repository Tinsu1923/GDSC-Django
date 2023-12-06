# The rules of the pattern:
# 1. No vowels are allowed.
# 2. length of the input must not be greater than 1.
# 3. No functions are allowed.
character = input("Enter the character. ")
count = 0
for i in character: # To find the length of the inputted character.
    count += 1
if count > 1:
    print("The length of the character has exceeded 1. ")    
elif character in ["a","e","i","o","u","A","E","I","O","U"]:
    print("Vowels are not allowed. ")
else:
    for i in range(1,10,2):
        print(character * i) # We repeat the character 'i' times.

