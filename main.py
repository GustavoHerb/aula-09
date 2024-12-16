lista_usuario = []
contador_mais18 = 0
contador_mais18_e_cnh = 0


while True:
    pergunta = input("Voce quer cadastrar usuarios? [S/N]")
    if pergunta == "N":
        break
    elif pergunta == "S":
        def criarusuarios(nome, idade, cnh):
            usuario = {
                "Nome": nome,
                "Idade": idade,
                "cnh": cnh
            }
            lista_usuario.append(usuario)

        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        cnh = input("O usuario tem cnh? Responda 'Tem' ou 'N': ")

        criarusuarios(nome, idade, cnh)

        print("Lista de usuários cadastrados:", lista_usuario)


        for usuario in lista_usuario:
            if usuario["Idade"] >= 18 and usuario["cnh"] == "Tem":
                print("É maior de idade! e tem cnh")
                contador_mais18_e_cnh =+ 1
            elif usuario['Idade'] >= 18 and usuario['cnh'] == "N":
                print("É maior de idade, porem não tem cnh!")
                contador_mais18 += 1 
            else:
                print("É menor de idade!")

print(f"Os usuarios que sao maiores de idade e tem cnh é: {contador_mais18_e_cnh}, e os que não tem habilitação e sao maiores são: {contador_mais18}")