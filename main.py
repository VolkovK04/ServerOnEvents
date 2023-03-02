class Event:
    def __init__(self):
        self.subscribers = []

    def bind(self, func):
        self.subscribers.append(func)

    def unbind(self, func):
        self.subscribers.remove(func)

    def start(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber(args, kwargs)

class Client:
    def __init__(self, ip: str, name: str):
        self.ip = ip
        self.name = name

class Server:
    def __init__(self):
        self.clients = []
        self.massage_received = Event()
        self.client_connected = Event()
        self.client_disconnected = Event()

    def start(self):
        # запускаем поток на прием подключений
        pass

    def connect(self):
        client = Client()
        self.client_connected.start(client)

    def send_message(self, client: Client, message: bytes):
        # отправляем сообщение клиенту
        pass

    def receive(self):
        # ...
        message = "hello server"
        self.massage_received.start(message)
        # ...




class Game:
    def __init__(self, server: Server):




