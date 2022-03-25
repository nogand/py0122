PALOS={
  "SPADES": "\u2660", 
  "HEARTS": "\u2661", 
  "DIAMONDS": "\u2662", 
  "CLUBS": "\u2663"
}

CARTAS={
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
    "10": "Diez",
    "JACK": "Jota",
    "QUEEN": "Reina",
    "KING": "Rey",
    "ACE": "As"
}

def imprimir(mazo):
  print(", ".join([ CARTAS[card["value"]]+" de "+PALOS[card["suit"]] for card in mazo ]))
