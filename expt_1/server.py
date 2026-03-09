from rpc import RPCServer

def add(a, b):
    return a + b


def sub(a, b):
    return a - b

server = RPCServer()
server.register_method(add)
server.register_method(sub)

server.run()