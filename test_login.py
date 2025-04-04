user_db = {
    'amin1': 'admin1',
    'admin2': 'admin2'
}

def login(username, password):
    if username in user_db and user_db[username] == password:
        return "Login successful!"
    else:
        return "Wrong username or password. Please try again"

def main():
    print("Welcome to the login system")
    username = input("Enter your username: ").strip()  # Strips extra whitespace
    password = input("Enter your password: ").strip()  # Strips extra whitespace
    
    result = login(username, password)
    print(result)

if __name__ == "__main__":
    main()