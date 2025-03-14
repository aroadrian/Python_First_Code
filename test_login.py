user_db = {
    'adrian': 'admin1',
    'admin': 'admin2'
}

def login(username, password):
    if username in user_db and user_db[username] == password:
        return "Login successful!"
    else:
        return "Invalid username or password."

def main():
    print("Welcome to the login system")
    username = input("Enter your username: ").strip()  # Strips extra whitespace
    password = input("Enter your password: ").strip()  # Strips extra whitespace
    
    result = login(username, password)
    print(result)

if __name__ == "__main__":
    main()