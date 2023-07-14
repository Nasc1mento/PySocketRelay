from models.client.Client import Client

client: Client = Client('localhost', 8090)


client.send('hello')

