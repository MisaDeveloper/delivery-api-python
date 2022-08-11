from flask import request, Response
from models.Orders.Orders import changeOrderStateOrder
import json

async def ChangeStateController(orderId, orderState):
    try:
        messageResponse = await changeOrderStateOrder(orderId, orderState)

        if messageResponse == 'allowed':
            return Response(json.dumps({ 'type': 'success', 'message': 'Estado do pedido alterado!' }, ensure_ascii=False, indent=4), status=201)
        elif messageResponse == 'not allowed':
            return Response(json.dumps({ 'type': 'error', 'message': 'Não permitido alterar para esse estado!' }, ensure_ascii=False, indent=4), status=405)
        else:
            return Response(json.dumps({ 'type': 'error', 'message': 'Id do pedido não encontrado!' }, ensure_ascii=False, indent=4), status=404)

    except:
        return Response(json.dumps({ 'type': 'error', 'message': 'Erro ao alterar estado do pedido!' }, ensure_ascii=False, indent=4), status=500)