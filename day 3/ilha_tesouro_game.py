print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo(a) a Ilha do Tesouro.")
print("A sua missão é achar o tesouro perdido.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_choice = input('Você está em uma encruzilhada, qual caminho você quer seguir? digite: "esquerda" ou "direita".').lower()

if first_choice == "esquerda":
    second_choice = input('Você conseguiu chegar ao lago, você deseja "esperar" ou "atravessar"?').lower()
    if second_choice == "esperar":
        third_choice = input('Excelente. Passou um barco e levou você até o outro lado do lago, onde você se deparou com 3 portas, escolha qual deseja abrir: "vermelha", "azul" ou "amarela".').lower()
        if third_choice == "vermelha":
            print("Você caiu na fogueira e morreu queimado.")
        elif third_choice == "azul":
            print("Você libertou o minotauro e acabou morrendo.")
        elif third_choice == "amarela":
            print("Meus parabéns, você achou o tesouro escondido!!!!")
    else:
        print("O crocodilo comeu você :´(")
else:
    print("Você perdeu :´(")
