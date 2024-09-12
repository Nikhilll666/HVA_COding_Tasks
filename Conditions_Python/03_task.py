# Write a program that categorizes a person's age into different life stages based on the following conditions:
# 0-2 years: Infant
# 3-12 years: Child
# 13-19 years: Teenager
# 20-65 years: Adult
# Above 65 years: Senior
# The program takes an age as input and prints the age group category the person belongs to. 


age = int(input())
if age<=2:
    print("Infant")
elif age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<66:
    print("Adult")
else:
    print("Senior")


