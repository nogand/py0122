import requests
import pickle
from imprimirmazo import imprimir
import sys

if len(sys.argv)==1 :
  mazo=input("Mazo: ")
else :
  mazo=sys.argv[1]

with open("/tmp/mazos/"+mazo+".pkl","rb") as archivo:
  todas=pickle.load(archivo)["cartas"]
imprimir(todas)
devolver=",".join([card["code"] for card in todas ])
requests.get("https://deckofcardsapi.com/api/deck/"+mazo+"/return/?cards="+devolver)
