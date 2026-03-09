from rpc import RPCClient

client = RPCClient("localhost", 8080)

client.connect()

print(client.add(5, 6))
print(client.sub(5, 6))

client.disconnect()