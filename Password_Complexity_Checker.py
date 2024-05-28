
# Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength


def password_complexity_check(passwd):

    specialsymbol = ["@","$","#","%","&","*"]
    val = True

    if len(passwd) < 8:
        print("Password length should be at least 8:")
        val = False
    if len(passwd) > 15:
        print("Password length should not more then 15:")
        val = False
    if not any(char.isdigit() for char in passwd):
        print("Password should Have at least one number:")
        val = False
    if not  any(char.isupper() for char in passwd):
        print("Password should have at least on uppercase:")
        val = False
    if not any(char.islower() for char in passwd):
        print("Password should have at least on uppercase:")
        val = False
    if not any(char in specialsymbol for char in passwd):
        print("Password should have at least one special symbol:")
        val = False
    if val:
        return val

def main():
    passwd = input("Enter Password:")
    if (password_complexity_check(passwd)):
        print("Password is Valid:")
    else:
        print("Invalid Password:")

# Driver Code
if __name__ == '__main__':
    main()
