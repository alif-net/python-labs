
# smart survey onboarding engine 

# 1. capture input from use (name , age , developer status)

name = input("What is your name? ").strip()

age = int(input("how old are you? ")) 

developer_answer = input ("are you a developer? (yes/no): ").strip().lower()

# turn the yes/no answer into true/false value

is_developer=developer_answer=="yes" or developer_answer=="y"
print(name ,age, is_developer, type(age))


if age < 18:

     tier = "Tier 3: Guest"

elif age >= 18 and is_developer: 
     tier = " Tier 1: Admin Infrastructure Access"
 
else: 
     tier = " Tier 2: Standard Executive Access"

print(tier) 
