# This program is a palindrome checker.
check = input("Enter the word to check.")
reverse = "" # Empty string.
for index in range(len(check) - 1, -1, -1): # From the last index of the character to the first, decrementing 1.
    reverse = reverse + check[index] # We add every single character from the last to the first, into the empty string.
if check == reverse: 
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
#########################
# Or, a much easier way, using list comprehension.
string = input("Enter the word to check. ")
rev_string = "".join([string[index] for index in range(len(string) - 1, -1,-1)]) # This adds the reversed string inside an empty string.
print("The word is " + "a palindrome. " if rev_string==string else "not a palindrome.")