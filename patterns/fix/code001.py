import string
import random

from dataclasses import dataclass


@dataclass
class VehicleBrand:
    name: str
    catalog_price: float
    electric: bool

    @property
    def payable_tax(self):
        if self.electric:
            return self.catalog_price * 0.02
        else:
            return self.catalog_price * 0.05

    def show(self):
        print(f"Brand: {self.name}")
        print(f"Payable Tax: {self.payable_tax}")


@dataclass
class Vehicle:
    id: str
    license_plate: str
    brand: VehicleBrand

    def show(self):
        print(f"ID: {self.id}")
        print(f"License Plate: {self.license_plate}")

        self.brand.show()


class VehicleRegistry:
    vehicle_catalog = {
        "Tesla Model 3": {
            "catalog_price": 60_000,
            "electric": True,
            "name": "Tesla Model 3",
        },
        "BMW 5": {"catalog_price": 45_000, "electric": False, "name": "BMW 5"},
        "Volkswagen ID3": {
            "catalog_price": 35_000,
            "electric": True,
            "name": "Volkswagen ID3",
        },
        "Tesla Model Y": {
            "catalog_price": 62_000,
            "electric": True,
            "name": "Tesla Model Y",
        },
    }

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: str) -> Vehicle:
        # generate a vehicle id of length 12

        vehicle_id = self.generate_vehicle_id(12)

        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(
            id=vehicle_id,
            license_plate=license_plate,
            brand=VehicleBrand(**self.vehicle_catalog.get(brand)),
        )


class Application:
    def register_vehicle(self, brand: str):
        # create a registery instance
        register = VehicleRegistry()

        v = register.create_vehicle(brand)

        return v


if __name__ == "__main__":
    app = Application()
    v = app.register_vehicle("Tesla Model Y")

    print("Registration complete. Vehicle information")

    v.show()
