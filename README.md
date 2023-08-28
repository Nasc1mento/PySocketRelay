# [PySocketRelay]

## Description
Message relayer using python socket API and Docker network
## How it works
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

### Peers
* Each peer have a socket server instance to receive connection and client instance to connect
* A peer root send a message and other peers in the list relay the message to the next in the list
![diagram](https://github.com/Nasc1mento/PySocketRelay/assets/88512599/e2be40b1-6bd8-48f6-8b4f-49d46a4b03e4)

### Tracker
TODO

### Docker Network
TODO

## Getting started
TODO

## My Specifications
* Podman 4.3.1
* Python 3.11.2

## License
[MIT](https://github.com/Nasc1mento/PySocketRelay/blob/main/LICENSE)
