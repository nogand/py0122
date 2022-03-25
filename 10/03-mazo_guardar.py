import requests
import pickle
from imprimirmazo import imprimir

mazo=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()["deck_id"]
todas=requests.get("https://deckofcardsapi.com/api/deck/"+mazo+"/draw/?count=52").json()["cards"]
print("El mazo es {} y contiene:".format(mazo))
imprimir(todas)
with open("/tmp/mazos/"+mazo+".pkl","wb") as archivo:
  pickle.dump({"mazo": mazo, "cartas": todas},archivo)
