from flask import request, Response
from models.Orders.Orders import changeOrderStateOrder

async def ChangeStateController(orderId, orderState):
    try:
        messageResponse = await changeOrderStateOrder(orderId, orderState)

        if messageResponse == 'allowed':
            return Response("{ 'type': 'success', 'message': 'Estado do pedido alterado!' }", status=201)
        elif messageResponse == 'not allowed':
            return Response("{ 'type': 'error', 'message': 'Não permitido alterar para esse estado!' }", status=405)
        else:
            return Response("{ 'type': 'error', 'message': 'Id do pedido não encontrado!' }", status=404)

    except:
        return Response("{ 'type': 'error', 'message': 'Erro ao alterar estado do pedido!' }", status=500)