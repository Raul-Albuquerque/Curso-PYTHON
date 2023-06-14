############DEBUGGING#####################

# # Fix the Errors
#age = input("How old are you?")
#if age > 18:
#print("You can drive at age {age}.")

# O PRINT precisa estar indentado dentro da condição 'if'.

# O input recebe uma string como resposta, e a condição está pedindo um número inteiro.

# A string que será impressa precisa começar com um f para poder imprimir o valor contido na variável 'age' 

# Só indentar o print dentro do if, transformar o retorno do input em  'int' e colocar um f antes da string que será impressa.
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")