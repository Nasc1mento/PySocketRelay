import threading

from simulators.server import ServerSimulator
from simulators.client import ClientSimulator


threading.Thread(target=ServerSimulator.start).start()
# client
threading.Thread(target=ClientSimulator.start).start()



