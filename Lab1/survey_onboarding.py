
# smart survey onboarding engine 

# 1. capture input from use (name , age , developer status)

name = input("What is your name? ").strip()

age = int(input("how old are you? ")) 

developer_answer = input ("are you a developer? (yes/no): ").strip().lower()

# 2. turn the yes/no answer into true/false value

is_developer=developer_answer=="yes" or developer_answer=="y"
print(name ,age, is_developer, type(age))


if age < 18:

     tier = "Tier 3: Guest"

elif age >= 18 and is_developer: 
     tier = " Tier 1: Admin Infrastructure Access"
 
else: 
     tier = " Tier 2: Standard Executive Access"

print(tier)

# 3. print out the final profile card using an f-string

developer_label= "Yes" if is_developer else "No"

print()
print("=" * 40) 
print("          Profile Configuration")
print("=" * 40)
print(f"Name:          {name}")
print(f"Age:           {age}")
print(f"Developer      {developer_label}")
print("=" * 40)
print(f"Welcome        {name}! you have been assigned {tier}. ")
