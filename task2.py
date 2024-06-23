## calculator 

n1 =  int(input("enter a num1:"))
n2 =  int(input("enter a num2:"))
lt1 = ["+ , - , / , * , // , % , **"] 
print(lt1)  
operator = input("enter above opeartor:") 

match operator:

    case "+":
       print("sum is:",n1+n2)
    case "-":
       print("sub is:",n1-n2)
    case "*":
       print("multiplie is:",n1*n2)
    case "/":
       print("division is:",n1/n2)
    case "//":
       print("floor division is:",n1//n2)
    case "%":
       print("modulo is:",n1%n2)
    case "**":
       print("exponent is:",n1**n2)   
    case _ :
       print("enter valid operator!")      


   
   
