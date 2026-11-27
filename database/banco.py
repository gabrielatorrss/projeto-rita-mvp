import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "pedidos.json")


def carregar_pedidos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Arquivo de pedidos com problema. Começando com a lista vazia.")
        return []


def salvar_pedidos(pedidos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(pedidos, arquivo, ensure_ascii=False, indent=4)


def proximo_id(pedidos):
    maior = 0
    for pedido in pedidos:
        if pedido["id"] > maior:
            maior = pedido["id"]
    return maior + 1
