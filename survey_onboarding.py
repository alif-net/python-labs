
# smart survey onboarding engine 

# 1. capture input from use (name , age , developer status)

name = input("What is your name? ").strip()

age = int(input("how old are you? ")) 

developer_answer = input ("are you a developer? (yes/no): ").strip().lower()

# turn the yes/no answer into true/false value

is_developer=developer_answer=="yes" or developer_answer=="y"
print(name ,age, is_developer, type(age))

