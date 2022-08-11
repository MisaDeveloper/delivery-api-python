# Import Modules
from models.Connection import read, write
from datetime import datetime

#Order Methods
### Get Orders By Id Method -----------------------------------------
async def getOrdersById(orderId):
    orders = await read()

    def filter():
        for order in orders['pedidos']:
            if order != None and order['id'] == int(orderId):
                return order

    filteredOrder = filter()

    if(filteredOrder):
        return filteredOrder
    else:
        return False


### Create Method ---------------------------------------------------
async def createOrder(cliente, produto, valor):
    orders = await read()
    dataTime = datetime.now()

    dictionary = {
        "id": orders['pedidos'][len(orders['pedidos']) - 1]['id'] + 1,
        "cliente": cliente,
        "produto": produto,
        "valor": valor,
        "entregue": False,
        "estado": 'RECEIVED',
        "timestamp": dataTime.isoformat()
    }

    orders['pedidos'].append(dictionary)
    await write(orders)


### Update Method ---------------------------------------------------
async def updateOrder(orderId, cliente, produto, valor):
    orders = await read()

    def filter():
        for order in orders['pedidos']:
            if order != None and order['id'] == int(orderId):
                return order

    try:
        elementIndex = orders['pedidos'].index(filter())
    except:
        elementIndex = -1

    if elementIndex != -1:
        orders['pedidos'][elementIndex]['cliente'] = cliente
        orders['pedidos'][elementIndex]['produto'] = produto
        orders['pedidos'][elementIndex]['valor'] = valor

        await write(orders)
        return True
    else:
        return False


### Delele Method ---------------------------------------------------
async def deleteOrder(orderId):
    orders = await read()

    def filter():
        for order in orders['pedidos']:
            if order != None and order['id'] == int(orderId):
                return order

    try:
        elementIndex = orders['pedidos'].index(filter())
    except:
        elementIndex = -1

    if elementIndex != -1:
        del(orders['pedidos'][elementIndex])

        await write(orders)
        return True
    else:
        return False


### Change State Method ---------------------------------------------------
async def changeOrderStateOrder(orderId, orderState):
    orders = await read()
    orderState = orderState.upper()

    states = {
        'RECEIVED': 'RECEIVED',
        'CONFIRMED': 'CONFIRMED',
        'DISPATCHED': 'DISPATCHED',
        'DELIVERED': 'DELIVERED',
        'CANCELED': 'CANCELED'
    }

    def filter():
        for order in orders['pedidos']:
            if order != None and order['id'] == int(orderId):
                return order

    try:
        elementIndex = orders['pedidos'].index(filter())
    except:
        elementIndex = -1

    if elementIndex != -1:
        if orders['pedidos'][elementIndex]['estado'] != states['CANCELED'] and orders['pedidos'][elementIndex]['estado'] != states['DELIVERED']:
            if orderState == states['CANCELED']:
                orders['pedidos'][elementIndex]['estado'] = states['CANCELED']
                await write(orders)
                return 'allowed'

            elif orderState == states['CONFIRMED'] and orders['pedidos'][elementIndex]['estado'] == states['RECEIVED']:
                orders['pedidos'][elementIndex]['estado'] = states['CONFIRMED']
                await write(orders)
                return 'allowed'

            elif orderState == states['DISPATCHED'] and orders['pedidos'][elementIndex]['estado'] == states['CONFIRMED']:
                orders['pedidos'][elementIndex]['estado'] = states['DISPATCHED']
                await write(orders)
                return 'allowed'

            elif orderState == states['DELIVERED'] and orders['pedidos'][elementIndex]['estado'] == states['DISPATCHED']:
                orders['pedidos'][elementIndex]['estado'] = states['DELIVERED']
                orders['pedidos'][elementIndex]['entregue'] = True
                await write(orders)
                return 'allowed'

            else:
                return 'not allowed'
        else:
                return 'not allowed'
    else:
        return False