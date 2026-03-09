import socket
import json
import inspect
from threading import Thread

SIZE = 1024


class RPCServer:

    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.methods = {}

    def register_method(self, function):
        self.methods[function.__name__] = function

    def register_instance(self, instance):
        for name, func in inspect.getmembers(instance, predicate=inspect.ismethod):
            if not name.startswith("_"):
                self.methods[name] = func

    def handle(self, client, address):
        print(f"Client connected: {address}")

        while True:
            try:
                data = client.recv(SIZE).decode()
                if not data:
                    break

                function_name, args, kwargs = json.loads(data)

                print(f"Request: {function_name}{tuple(args)}")

                result = self.methods[function_name](*args, **kwargs)

                client.sendall(json.dumps(result).encode())

            except Exception as e:
                client.sendall(json.dumps(str(e)).encode())

        print(f"Client disconnected: {address}")
        client.close()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.bind(self.address)
            s.listen()

            print(f"RPC Server running on {self.address}")

            while True:
                client, address = s.accept()

                Thread(target=self.handle, args=(client, address)).start()


class RPCClient:

    def __init__(self, host="localhost", port=8080):
        self.address = (host, port)
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.address)

    def disconnect(self):
        if self.sock:
            self.sock.close()

    def __getattr__(self, name):

        def execute(*args, **kwargs):
            request = json.dumps((name, args, kwargs))

            self.sock.sendall(request.encode())

            response = self.sock.recv(SIZE).decode()

            return json.loads(response)

        return execute