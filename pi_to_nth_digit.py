
import math

x = True

print("This program will generate pi up to a given number of decimal places.")

while x == True:

    digit = (input("Enter a number (max of 50): "))
    pi = math.pi

    if digit.isnumeric():

        digit_ans = int(digit)

        if digit_ans > 50:
            print("The max is 50. Please try again.")

        elif digit_ans <= 50:
            formatted_float = "The answer is {r:.{n}f}".format(r=pi,n=digit_ans)
            print(formatted_float)
            x = False
    else:
        print("Invalid option. Please try again")
        
