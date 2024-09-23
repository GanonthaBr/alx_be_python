def perform_operation(num1:float,num2:float,operation:str):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Division by zero is not allowed"
            return num1 / num2
        case _:
            return "Invalid operation"
        

print(perform_operation(1,2,'divide'))