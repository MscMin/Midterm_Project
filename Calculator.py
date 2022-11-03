import Arithmetic_operation
import Logging

def reconfirm(x):
    while x.lower()!="no" and x.lower()!="yes":
        x = input("Please Enter the 'no' or 'yes'!: ")
    return x

print("Select operation.") 
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 



while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first numbeyesr: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            add_value = Arithmetic_operation.add(num1, num2)
            print(num1, "+", num2, "=", add_value)
            message = "Add: " + str(num1) +" + " + str(num2) + " = " + str(add_value)
            Logging.Arithmetic_Add(message)

        elif choice == '2':
            sub_value = Arithmetic_operation.subtract(num1,num2)
            print(num1, "-", num2, "=", sub_value)
            message = "Subtract: " + str(num1) +" - " + str(num2) + " = " + str(sub_value)
            Logging.Arithmetic_Sub(message)

        elif choice == '3':
            mul_value = Arithmetic_operation.multiply(num1,num2)
            print(num1, "*", num2, "=", mul_value)
            message = "Multiply: " + str(num1) +" * " + str(num2) + " = " + str(mul_value)
            Logging.Arithmetic_Mul(message)
            
        elif choice =='4':
            if num2==0:
                print(Arithmetic_operation.divide(num1,num2))
                Logging.DivByZero()
            else: 
                div_value = Arithmetic_operation.divide(num1,num2)
                print(num1, "/", num2, "=", div_value)
                message = "Divide: " + str(num1) +" / " + str(num2) + " = " + str(div_value)
                Logging.Arithmetic_Div(message)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        next_calculation = reconfirm(next_calculation)
        if next_calculation.lower() == "no":
            next_calculation = input("Are you sure?(yes/no): ")
            next_calculation = reconfirm(next_calculation)
            if next_calculation.lower() =="yes":
                break

    else:
        print("Invalid Input")
        Logging.InvalidInput()
