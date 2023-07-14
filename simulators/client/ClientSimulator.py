import time
from models.Client import Client

client: Client = Client('localhost', 6069)


def start():
    while True:
        client.send('responde almadicoado')
        time.sleep(3)




