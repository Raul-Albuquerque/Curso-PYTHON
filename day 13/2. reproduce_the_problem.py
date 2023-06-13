############DEBUGGING#####################

# # Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
#print(dice_imgs[dice_num])

#O RANDINT retorna um número aleatório contando com os próprios números informados.

#Já a lista começa a contar em zero, quando o randint retornar o número 6 ele vai ficar fora do range da lista.
# # Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = 6
#print(dice_imgs[dice_num])

#Para corrigir, basta informar o '0' como início e o '5' como fim do randint, dessa forma o retorno estará sempre dentro dos itens da lista.

# # SOLUTION
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])