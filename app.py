import flet as ft

def main(page: ft.Page):
    # Criação de uma variável de texto para armazenar o nome do usuário
    nome_usuario = ft.Text()

    # Função que atualiza o texto com o nome fornecido pelo usuário
    def atualizar_nome(e):
        nome_usuario.value = f"Olá, {input_nome.value}!"
        input_nome.value = ""
        page.update()

    # Função que altera a cor do nome exibido
    def mudar_cor(cor):
        nome_usuario.style = ft.TextStyle(color=cor)
        page.update()

    # Input para o usuário digitar o nome
    input_nome = ft.TextField(label="Digite seu nome", autofocus=True)

    # Botão para atualizar o nome
    btn_atualizar = ft.ElevatedButton("Mostrar nome", on_click=atualizar_nome)

    # Botões para mudar a cor do nome
    btn_vermelho = ft.ElevatedButton("Vermelho", on_click=lambda e: mudar_cor("red"))
    btn_azul = ft.ElevatedButton("Azul", on_click=lambda e: mudar_cor("blue"))
    btn_verde = ft.ElevatedButton("Verde", on_click=lambda e: mudar_cor("green"))

    # Adiciona os elementos na página
    page.add(input_nome, btn_atualizar, nome_usuario, btn_vermelho, btn_azul, btn_verde)

# Executa o aplicativo
ft.app(target=main)
