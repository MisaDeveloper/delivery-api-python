from flask import request, Response
from models.Orders.Orders import deleteOrder
import json

async def DeleteController(orderId):
    try:

        if await deleteOrder(orderId):
            return Response(json.dumps({ 'type': 'success', 'message': 'Pedido excluído com sucesso!' }, ensure_ascii=False, indent=4), status=201)
        else:
            return Response(json.dumps({ 'type': 'error', 'message': 'Id do pedido não encontrado!' }, ensure_ascii=False, indent=4), status=404)

    except:
        return Response(json.dumps({ 'type': 'error', 'message': 'Erro ao deletar pedido!' }, ensure_ascii=False, indent=4), status=500)