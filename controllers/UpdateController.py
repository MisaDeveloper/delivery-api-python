from flask import request, Response
from models.Orders.Orders import updateOrder

async def UpdateController(orderId):
    data = request.json

    if 'cliente' in data and 'produto' in data  and 'valor' in data :
        
        try:

            if await updateOrder(orderId, data['cliente'], data['produto'], data['valor']):
                return Response("{ 'type': 'success', 'message': 'Pedido atualizado com sucesso!' }", status=201)
            else:
                return Response("{ 'type': 'error', 'message': 'Id do pedido não encontrado!' }", status=404)

        except:
            return Response("{ 'type': 'error', 'message': 'Erro ao atualizar pedido!' }", status=500)

    else:
        return Response("{ 'type': 'error', 'message': 'Formulário de edição incompleto!' }", status=400)