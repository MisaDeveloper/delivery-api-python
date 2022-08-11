from flask import request, Response
from models.Orders.Orders import createOrder
import json

async def CreateController():
    data = request.json

    if 'cliente' in data and 'produto' in data  and 'valor' in data :
        
        try:
            await createOrder(data['cliente'], data['produto'], data['valor'])
            return Response(json.dumps({ 'type': 'success', 'message': 'Pedido criado com sucesso!' }, ensure_ascii=False, indent=4), status=201)
        
        except:
            return Response(json.dumps({ 'type': 'error', 'message': 'Erro ao criar pedido!' }, ensure_ascii=False, indent=4), status=500)
    else:
        return Response(json.dumps({ 'type': 'error', 'message': 'Formulário de criação incompleto!' }, ensure_ascii=False, indent=4), status=400)