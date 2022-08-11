from flask import request, Response
from models.Orders.Orders import createOrder

async def CreateController():
    data = request.json

    if 'cliente' in data and 'produto' in data  and 'valor' in data :
        
        try:
            await createOrder(data['cliente'], data['produto'], data['valor'])
            return Response("{ 'type': 'success', 'message': 'Pedido criado com sucesso!' }", status=201)
        
        except:
            return Response("{ 'type': 'error', 'message': 'Erro ao criar pedido!' }", status=500)
    else:
        return Response("{ 'type': 'error', 'message': 'Formulário de criação incompleto!' }", status=400)