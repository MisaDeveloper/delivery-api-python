from flask import request, Response
from models.Orders.Orders import getOrdersById

async def GetOrderController(orderId):

    data = await getOrdersById(orderId)
    
    try:
        if data:
            return data
        else:
            return Response("{ 'type': 'error', 'message': 'Id do pedido não encontrado!' }", status=404)
    except:
        return Response("{ 'type': 'error', 'message': 'Erro ao consultar pedido!' }", status=500)