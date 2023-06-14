#for number in range(1, 101):
  #if number % 3 == 0 or number % 5 == 0:
   # print("FizzBuzz")
  #if number % 3 == 0:
   # print("Fizz")
  #if number % 5 == 0:
   # print("Buzz")
 # else:
    #print([number])

# A condição para ser fizzbuzz é que o número precisa ser divisível por 3 e por 5, dessa forma, é preciso substituir o 'or' pelo 'and'.
# Os 'if' depois do primeiro precisam ser substituidos pelo 'elif'.
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])