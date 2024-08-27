"""
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or
'name' exists in the list, or "No" - in the other case.
"""


class TVController:
    def __init__(self, channels: list[str]) -> None:
        self.channels = channels
        self.default_channel = self.channels[0]

    def first_channel(self) -> str:
        return self.channels[0]

    def last_channel(self) -> str:
        return self.channels[-1]

    def turn_channel(self, n: int) -> str:
        if 1 <= n <= len(self.channels):
            self.default_channel = self.channels[n - 1]
            return self.default_channel
        return "No"

    def next_channel(self) -> str:
        current_channel = self.channels.index(self.default_channel)
        next_channel = (current_channel + 1) % len(self.channels)
        self.default_channel = self.channels[next_channel]
        return self.default_channel

    def previous_channel(self) -> str:
        current_channel = self.channels.index(self.default_channel)
        previous_channel = (current_channel - 1) % len(self.channels)
        self.default_channel = self.channels[previous_channel]
        return self.default_channel

    def current_channel(self) -> str:
        return self.default_channel

    def is_exist(self, n) -> str:
        if isinstance(n, str):
            return "Yes" if n in self.channels else "No"
        elif isinstance(n, int):
            return "Yes" if 1 <= n <= len(self.channels) else "No"
        return "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
