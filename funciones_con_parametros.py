def divisibles(valor):
    if (int(valor) % 2 == 0 and int(valor) % 3 == 0):
        print(str(valor) + " Es divisible por 2 y 3")
    else:
        divisibles(valor= int(input("No es divisible por 2 y 3, ingrese nuevo valor: ")))
divisibles(valor = int(input("Ingresa un numero para dividir por 2 y 3:  ")))


#########


def multiplicacion (num1,num2):
    
    suma = num1 * num2
    print ("El resultado de " + str(num1) + " * " + str(num2) + " = "+ str(suma))


multiplicacion(num1 = int(input("Ingrese se primer numero:  ")),num2 = int(input("Ingrese su 2° numero:  ")))


##########
  

def regla3 (num1, num2, num3):
    calculo = (num1 * num2)/num3
    print ("El resultado de " + str("(") + str(num1) + " * " + str(num2) + str(")") + str(" \ ") + str(num3) + " = " + str(calculo))

regla3(num1 = int(input("Ingrese se primer numero para la regla de 3 simple:  ")),num2 = int(input("Ingrese su segundo numero:  ")),num3 = int(input("Ingrese su tercer numero:  ")))


###########

def potenciacion (num1, elevacion):
    calculo = num1 ** elevacion
    print (" El numero: " + str(num1) + " Elevado a: " + str(elevacion) + " Es igual a: " + str(calculo))
potenciacion(num1 = int(input(" Ingrese el numero a elevar:  ")), elevacion = int(input(" Ingrese a que potencia desea elevar el numero: ")))
