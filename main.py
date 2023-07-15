from models import Tracker, Client

(host, port) = ('localhost', 6067)
tracker: Tracker = Tracker.Tracker(host, port)
client: Client = Client.Client('localhost', 7007)
tracker.add_client(client)
for c in tracker.get_clients():
    print(c.get_key())



