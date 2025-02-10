def main():
   print("Basic Calculator")
   print("Select operation:")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")

   operation = input()

   if operation == '1':
       num1 = input("Enter first number: ")
       num2 = input("Enter second number: ")
       print("The sum is: " + str(int(num1) + int(num2)))
   elif operation == '2':
       num1 = input("Enter first number: ")
       num2 = input("Enter second number: ")
       print("The sum is: " + str(int(num1) - int(num2)))
   elif operation == '3':
       num1 = input("Enter first number: ")
       num2 = input("Enter second number: ")
       print("The sum is: " + str(int(num1) *  int(num2)))
   elif operation == '4':
       num1 = input("Enter first number: ")
       num2 = input("Enter second number: ")
       print("The sum is: " + str(int(num1) / int(num2)))
   

if __name__ == "__main__":
    main()