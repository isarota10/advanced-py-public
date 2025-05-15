class LightBulb:
    def turn_off(self):
        print("Light Off...")

    def turn_on(self):
        print("Light On...")


class Server:
    def turn_off(self):
        print("Light Off...")

    def turn_on(self):
        print("Light On...")


class ElectricPowerSwitch:
    def __init__(self, device: LightBulb):
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
    l = LightBulb()
    switch = ElectricPowerSwitch(l)

    switch.press()
    switch.press()
