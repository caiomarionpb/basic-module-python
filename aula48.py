"""
faça um jogo para o usuário advinhar qual a palavra secreta.
- você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra
- qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- se a letra digitada estiver na palavra secreta, exiba a letra.
- se a letra digitada não estiver na palavra secreta, exiba *.
faça a contagem de tentativas do seu usuário
"""

# Palavra secreta definida
palavra_secreta = "python"
# Criando uma lista com * para ocultar as letras
progresso = ["*"] * len(palavra_secreta)

# Contador de tentativas
tentativas = 0

print("🎮 Bem-vindo ao jogo de adivinhar a palavra!")
print("A palavra secreta tem", len(palavra_secreta), "letras.")
print("Você pode digitar uma letra por tentativa.")

while "*" in progresso:
    print("\nPalavra até agora:", "".join(progresso))
    letra = input("Digite uma letra: ").lower()

    # Verifica se o input é válido
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas UMA letra.")
        continue

    tentativas += 1

    # Verifica se a letra está na palavra
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                progresso[i] = letra
        print("✅ A letra está na palavra!")
    else:
        print("❌ Letra incorreta.")

print("\n🎉 Parabéns! Você descobriu a palavra:", palavra_secreta)
print("Tentativas totais:", tentativas)
