from abc import ABC, abstractmethod


class AbstractElectricDevice(ABC):
    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass


class LightBulb(AbstractElectricDevice):
    def turn_off(self):
        print("Light Off...")

    def turn_on(self):
        print("Light On...")


class Server(AbstractElectricDevice):
    def turn_off(self):
        print("Light Off...")

    def turn_on(self):
        print("Light On...")


class WashingMachine(AbstractElectricDevice): ...


class ElectricPowerSwitch:
    def __init__(self, device: AbstractElectricDevice):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True


if __name__ == "__main__":
    l1 = LightBulb()

    switch = ElectricPowerSwitch(l1)

    switch.press()
    switch.press()

    l2 = Server()

    switch = ElectricPowerSwitch(l2)

    switch.press()
    switch.press()

    l3 = WashingMachine()

    switch = ElectricPowerSwitch(l3)

    switch.press()
    switch.press()
