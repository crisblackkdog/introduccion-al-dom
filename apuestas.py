monto = float(input("Ingrese el monto inicial: "))  

for dia in range(1, 31):  
    ganancia_diaria = monto * 0.05
    monto *= 1.05
    print(f"Día {dia}: Monto: ${monto:.2f}, Ganancia Diaria: ${ganancia_diaria:.2f}") 

print("Monto final después de 30 días:", monto)  
