from collections import abc


class Developer:

    def __init__(self, name, maxibons_to_grab):
        self.name = name
        self.maxibons_to_grab = max(0, maxibons_to_grab)


pedro = Developer('Pedro', 3)
fran = Developer('Fran', 1)
davide = Developer('Davide', 0)
sergio = Developer('Sergio', 2)
jorge = Developer('Jorger', 1)


class KarumiHQs:

    def __init__(self, chat):
        self.chat = chat
        self.maxibon_left = 10

    def open_fridge(self, devs):
        if not isinstance(devs, abc.Iterable):
            devs = [devs]

        self._open_fridge(devs)

    def _open_fridge(self, devs):
        for dev in devs:
            self.maxibon_left -= dev.maxibons_to_grab
            if self.maxibon_left <= 2:
                self.maxibon_left += 10
                self.chat.send_message("Hi folks, I'm {}. We need more maxibons!".format(dev.name))


class ConsoleChat:

    def send_message(self, message):
        print(message)
