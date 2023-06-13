############DEBUGGING#####################

# # Play Computer
#year = int(input("What's your year of birth? "))
#if year > 1980 and year < 1994:
 # print("You are a millenial.")
#elif year > 1994:
  #print("You are a Gen Z.")

#O primeiro 'if' está condicionando apenas os anos maiores que 1980 e os menores que 1994, não incluindo eles.

#Para corrigir, basta incluir o sinal de '=' depois dos sinais atuais.
# # Play Computer
year = int(input("What's your year of birth? "))
if year >= 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")