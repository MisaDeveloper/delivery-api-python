from base64 import encode
from codecs import utf_16_be_decode
from flask import request, Response
from models.Orders.Orders import updateOrder
import json

async def UpdateController(orderId):
    data = request.json

    if 'cliente' in data and 'produto' in data  and 'valor' in data :
        
        try:

            if await updateOrder(orderId, data['cliente'], data['produto'], data['valor']):
                return Response(json.dumps({ 'type': 'success', 'message': 'Pedido atualizado com sucesso!' }, ensure_ascii=False, indent=4), status=201)
            else:
                return Response(json.dumps({ 'type': 'error', 'message': 'Id do pedido não encontrado!' }, ensure_ascii=False, indent=4), status=404)

        except:
            return Response(json.dumps({ 'type': 'error', 'message': 'Erro ao atualizar pedido!' }, ensure_ascii=False, indent=4), status=500)

    else:
        return Response(json.dumps({ 'type': 'error', 'message': 'Formulário de edição incompleto!' }, ensure_ascii=False, indent=4), status=400)