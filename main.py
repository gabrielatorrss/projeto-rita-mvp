from database.banco import carregar_pedidos, salvar_pedidos
from views.menu_view import exibir_menu
from controllers.cadastro_controller import cadastrar_pedido, listar_historico
from controllers.edicao_controller import atualizar_pedido, excluir_pedido

pedidos = carregar_pedidos()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_pedido(pedidos)

    elif opcao == "2":
        listar_historico(pedidos)

    elif opcao == "3":
        atualizar_pedido(pedidos)

    elif opcao == "4":
        excluir_pedido(pedidos)

    elif opcao == "5":
        salvar_pedidos(pedidos)
        print("Dados salvos. Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
