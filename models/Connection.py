from encodings.utf_8 import encode
import json

fileName = 'pedidos.json'

async def read():
    with open(fileName, 'r', encoding = 'utf-8') as orders:
        data = json.load(orders)
    return data

async def write(data):
    with open(fileName, 'w', encoding = 'utf-8') as orders:
        orders.write(json.dumps(data, indent=4, ensure_ascii=False))