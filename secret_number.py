def main():
    secret_num= 10
    guess_count = 0
    guess_limit = 5
    print("Try While Looping")
    while guess_count < guess_limit:
        guess = int(input("Input your guess number 1 to 10: "))
        guess_count += 1
        if guess == secret_num:
            print("You won!")
            break
    else:
        print("You lose!")


if __name__ == "__main__":
    main()  