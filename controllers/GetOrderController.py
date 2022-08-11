from flask import request, Response
from models.Orders.Orders import getOrdersById
import json

async def GetOrderController(orderId):

    data = await getOrdersById(orderId)
    
    try:
        if data:
            return data
        else:
            return Response(json.dumps({ 'type': 'error', 'message': 'Id do pedido não encontrado!' }, ensure_ascii=False, indent=4), status=404)
    except:
        return Response(json.dumps({ 'type': 'error', 'message': 'Erro ao consultar pedido!' }, ensure_ascii=False, indent=4), status=500)