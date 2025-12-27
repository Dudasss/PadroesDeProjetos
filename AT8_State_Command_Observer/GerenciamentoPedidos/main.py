from PadroesDeProjetos.AT8_State_Command_Observer.GerenciamentoPedidos.Classes.Pedido import Pedido


def SistemaGerenciamentoPedido():
    # Criando pedido, ele já começa sendo Recebido
    pedido = Pedido()
    # Recebido -> Processando
    pedido.processar_pedido()
    # Processando -> Enviado
    pedido.processar_pedido()
    # Enviado -> Entregue
    pedido.processar_pedido()
    # Entregue
    pedido.processar_pedido()


if __name__ == "__main__":
    SistemaGerenciamentoPedido()
