# Menu do RPG
print("-------====++====-------")
print("Seja bem vindo ao RPG!")
nome = input("Qual o nome do seu herói? ")
heroi = int(input('''Selecione sua classe:
1 - Guerreiro
2 - Mago
3 - Monge
4 - Ninja
            '''))

# Definindo a classe do herói
def classe():
    if heroi == 1:
        return "guerreiro"

    elif heroi == 2:
        return "mago"

    elif heroi == 3:
        return "monge"

    elif heroi == 4:
        return "ninja"

# Definindo a arma do herói
def arma():
    if classe() == "guerreiro":
        return "espada"

    elif classe() == "mago":
        return "magia"

    elif classe() == "monge":
        return "artes marciais"

    elif classe() == "ninja":
        return "shuriken"

classe_heroi = classe()
arma_ataque = arma()
    
# Exibição de nome, classe e arma do herói
print( nome, "da classe", classe_heroi, "atacou usando", arma_ataque,"!")
print("-------====++====-------")
