import sys
class Calculator(object) :
    @staticmethod 
    def main( args) :
        sc =  "Python-inputs"
        num1 = input()
        num2 = input()
        operator = input()[0]
        if (operator=='+'):
            print(str(num1) + " + " + str(num2) + " = " + str(Calculator.addition(num1, num2)))
        elif(operator=='-'):
            print(str(num1) + " - " + str(num2) + " = " + str(Calculator.subtraction(num1, num2)))
        elif(operator=='*'):
            print(str(num1) + " * " + str(num2) + " = " + str(Calculator.muliplication(num1, num2)))
        elif(operator=='/'):
            print(str(num1) + " / " + str(num2) + " = " + str(Calculator.division(num1, num2)))
        elif(operator=='^'):
            print(str(num1) + " ^ " + str(num2) + " = " + str(Calculator.power(num1, num2)))
        elif(operator=='%'):
            print(str(num1) + " % " + str(num2) + " = " + str(Calculator.modulo(num1, num2)))
        elif(operator=='!'):
            print(str(num1) + "! = " + str(Calculator.factorial(num1)))
    @staticmethod    
    def  factorial( num1) :
        # Write Logic to generate factorial of a number
        return 0
    @staticmethod
    def  modulo( num1,  num2) :
        #  Write Logic to produce the result for modulo of two numbers
        return 0
    @staticmethod
    def  power( num1,  num2) :
        # Write Logic to generate power of a number
        return 0
    @staticmethod
    def  division( num1,  num2) :
        #  Write Logic to produce the result when we divide two numbers
        return 0
    @staticmethod
    def  muliplication( num1,  num2) :
        # Write Logic to produce the result when we multiply two numbers
        return 0
    @staticmethod
    def  subtraction( num1,  num2) :
        # Write Logic to produce the result when we subtract two numbers
        return 0
    @staticmethod
    def  addition( num1,  num2) :
        # Write Logic to produce the result when we sum two numbers
        return 0
if __name__=="__main__":
    Calculator.main(sys.argv)
