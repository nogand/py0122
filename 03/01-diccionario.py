colores={
    "puerta": "rojo",
    "pared" : "blanco",
    "piso"  : "negro"
}
print(colores["pared"])

for pieza in colores :
    print("El color de "+pieza+" es "+colores[pieza]+".")