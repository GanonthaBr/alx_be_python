def perform_operation(num1,num2,operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Division by zero is not allowed"
            return num1 / num2
        case _:
            return "Invalid operation"
        

