def excluir_pedido(pedidos):
    if len(pedidos) == 0:
        print("\nNenhum pedido para excluir.")
        return

    listar_historico(pedidos)
    pedido = buscar_por_id(pedidos, ler_inteiro("\nDigite o ID do pedido: "))

    if pedido is None:
        print("Pedido não encontrado.")
        return

    confirmacao = input(f"Excluir o pedido {pedido['id']} de {pedido['agricultor']}? (s/n): ").strip().lower()

    if confirmacao == "s":
        pedidos.remove(pedido)
        salvar_pedidos(pedidos)
        print("Pedido excluído.")
    else:
        print("Exclusão cancelada.")
