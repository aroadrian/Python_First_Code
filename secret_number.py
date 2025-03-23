def main():
    secret_num= 15
    guess_count = 0
    guess_limit = 6
    print("Try this While Looping")
    while guess_count < guess_limit:
        guess = int(input("Input your guess number 1 to 15: "))
        guess_count += 1
        if guess == secret_num:
            print("You win!")
            break
    else:
        print("You lose!")


if __name__ == "__main__":
    main()  