from flask import request, Response
from models.Orders.Orders import deleteOrder

async def DeleteController(orderId):
    try:

        if await deleteOrder(orderId):
            return Response("{ 'type': 'success', 'message': 'Pedido excluído com sucesso!' }", status=201)
        else:
            return Response("{ 'type': 'error', 'message': 'Id do pedido não encontrado!' }", status=404)

    except:
        return Response("{ 'type': 'error', 'message': 'Erro ao deletar pedido!' }", status=500)