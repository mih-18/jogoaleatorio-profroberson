import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 10
    tentativas_usadas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while tentativas > 0:
        palpite = int(input(f"Você tem {tentativas} tentativas restantes. Faça seu palpite: "))
        tentativas_usadas += 1
        tentativas -= 1
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas_usadas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
    
    if tentativas == 0:
        print(f"Você não conseguiu adivinhar o número. O número correto era {numero_secreto}.")
    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        jogar()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()
