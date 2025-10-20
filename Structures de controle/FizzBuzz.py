# Pour les nombres de 1 à 100 :
# - Si divisible par 3 : "Fizz"
# - Si divisible par 5 : "Buzz"  
# - Si divisible par 3 et 5 : "FizzBuzz"
# - Sinon : le nombre

for i in range(1,100):
    if i % 3 == 0:
      if i % 5 == 0:
         print("FizzBuzz")
      else:
         print("Fizz")
    elif i % 5 == 0:
       if i % 3 == 0:
          print("FizzBuzz")
       else:
          print("Buzz")
    else:
        print(i)