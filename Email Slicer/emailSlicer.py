email = input("Enter Your Email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")