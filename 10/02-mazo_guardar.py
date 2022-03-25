import requests
import pickle
from imprimirmazo import imprimir

mazo=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()["deck_id"]
print("El mazo es:",mazo)
todas=requests.get("https://deckofcardsapi.com/api/deck/"+mazo+"/draw/?count=52").json()["cards"]
imprimir(todas)
with open("mazo.pkl","wb") as archivo:
  pickle.dump(todas,archivo)
