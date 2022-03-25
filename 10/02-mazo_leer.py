import pickle
from imprimirmazo import imprimir

with open("mazo.pkl","rb") as archivo:
  todas=pickle.load(archivo)
imprimir(todas)
