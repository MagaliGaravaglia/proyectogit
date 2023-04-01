def calculo_dosis():
    cd=int(input("Ingrese la cantidad de días que debe suministrarse el remedio: "))
    xd=int(input("Ingrese la cantidad de veces por día que debe tomar el remedio: "))
    cc=int(input("Ingrese la cantidad de comprimidos que trae el envase: "))
    return (cd,xd,cc)

dosis=cargo_dosis()

print(dosis[2] >= (dosis[0]*dosis[1]))

