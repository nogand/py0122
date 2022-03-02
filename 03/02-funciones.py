def divisible (num) :
    # Función que devueleve true cuando se cumplen todas las condiciones.
    if i%2==0 or i%3==0 or i%5==0 :
        return True
    else :
        return False

for i in range(1,101) :
  if divisible(i):
        print(i,"*")
  else :
        print(i)