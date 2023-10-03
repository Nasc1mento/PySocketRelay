# [PySocketRelay]

## Description
Message relayer using python socket API and Docker network
## How it works
2 Entities: **Peer(Socket server instance, Socket client instance )** and **Tracker**
![diagram](https://github.com/Nasc1mento/PySocketRelay/assets/88512599/e2be40b1-6bd8-48f6-8b4f-49d46a4b03e4)
### Peers
* Each peer have a socket server instance to receive connection and client instance to connect
* A peer root send a message and other peers in the list relay the message to the next in the list

### Tracker
* Receive a peer(socket client instance connection and peer(server, client) info message), disconnect and add to peers' list. 'List' connect the peer to the server of last peer on the list
* First retangle in the image example

### Docker Network
TODO

## Getting started
temp: 
```
  cd simulators/tracker
  export PYTHONPATH=../../:$PYTHONPATH
  python3 Tracker.py
```
```
  cd simulators/root
  export PYTHONPATH=../../:$PYTHONPATH
  python3 PeerRoot.py
```
```
  cd simulators/relay
  export PYTHONPATH=../../:$PYTHONPATH
  python3 PeerRelayer.py
```

## My Specifications
* Podman 4.3.1
* Python 3.11.2

## License
[MIT](https://github.com/Nasc1mento/PySocketRelay/blob/main/LICENSE)
