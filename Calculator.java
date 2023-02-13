import java.util.*;
public class Calculator {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int num1=sc.nextInt();
        int num2=sc.nextInt();
        char operator=sc.next().charAt(0);
        switch(operator) {
        case '+':
            System.out.println(num1+" + "+num2+" = "+addition(num1,num2));
            break;
        case '-':
            System.out.println(num1+" - "+num2+" = "+subtraction(num1,num2));
            break;
        case '*':
            System.out.println(num1+" * "+num2+" = "+muliplication(num1,num2));
            break;
        case '/':
            System.out.println(num1+" / "+num2+" = "+division(num1,num2));
            break;
        case '^':
            System.out.println(num1+" ^ "+num2+" = "+power(num1,num2));
            break;
        case '%':
            System.out.println(num1+" % "+num2+" = "+modulo(num1,num2));
            break;
        case '!':
            System.out.println(num1+"! = "+factorial(num1));
            break;
        }
    }
    private static int factorial(int num1) {
        //Write Logic to generate factorial of a number
      return 0;
    }
    private static int modulo(int num1, int num2) {
        // Write Logic to produce the result for modulo of two numbers
      return 0;
    }
    private static int power(int num1, int num2) {
        // Write Logic to generate power of a number
      return 0;
    }
    private static int division(int num1, int num2) {
        // Write Logic to produce the result when we divide two numbers
      return 0;
    }
    private static int muliplication(int num1, int num2) {
        // Write Logic to produce the result when we multiply two numbers
      return 0;
    }
    private static int subtraction(int num1, int num2) {
        // Write Logic to produce the result when we subtract two numbers
      return 0;
    }
    private static int addition(int num1, int num2) {
        // Write Logic to produce the result when we sum two numbers
      return 0;
    }
}
