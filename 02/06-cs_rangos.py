salario = int(input("Por favor introduzca el salario: "))


# Revisamos cuanto se debe agregar de carga social:
if salario > 1000000 :
    carga_social = float(0.3) #float es para decirle a la computadora que va a usar un numero flotante 0.00
    cs="30%"
else :
    if salario > 500000 :
        carga_social = float(0.2)
        cs="20%"
    else : 
        carga_social = float(0.1)
        cs="10%"

# Imprimimos el resultado
print("Con la carga social (",cs,") sería:",salario+(salario*carga_social)) #toma la variable salario y le suma el 30% de cargas sociales
