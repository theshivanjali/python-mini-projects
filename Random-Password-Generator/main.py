import string
import secrets

def random_password(len):
    letters = string.ascii_letters + string.digits + "@#$&*()+_{}-.=%"
    password = "".join(secrets.choice(letters) for i in range(len))
    return password

if __name__ == '__main__':

    passwordLength = int(input("Enter the Length Of Password:"))
    print("Suggested Password:", random_password(passwordLength))