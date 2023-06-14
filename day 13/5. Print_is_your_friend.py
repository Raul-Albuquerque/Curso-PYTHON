############DEBUGGING#####################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Tem que imprimir no console as variáveis para saber qual o valor está sendo recebido, no caso específico está sendo recebido o valor '0' declarado inicialmente nas duas primeiras linhas do código, basta apagá-las.

# A varíavel word_per_page está utilizando o sinal de igual duplo, que é utilizado somente para condições, só apagar um também.


# #Print is Your Friend
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
#print(pages)
#print(word_per_page)
total_words = pages * word_per_page
print(total_words)