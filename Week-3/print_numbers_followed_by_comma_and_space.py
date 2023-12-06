# So to print numbers in ascending order, we need to use a for loop.
for number in range(0,100): # Integers between 0 and 100, excluding 100:
    if number >= 0 and number < 10: # We want to display everything in this range as as 2 digit number.
        print(f"0{number} ", end = "," ) # I used the end attribute to not make the next iteration go on a new line.
    else:
        print(f"{number} ", end = "," ) # The comma at the end attribute makes the next iteration be printed after a comma. 
    