import string
import random


class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        # create a registery instance
        register = VehicleRegistry()

        # generate a vehicle id of length 12

        vehicle_id = register.generate_vehicle_id(12)

        license_plate = register.generate_vehicle_license(vehicle_id)

        # Compute catalog price
        catalog_price = 0

        if brand == "Tesla Model 3":
            catalog_price = 60_000
        elif brand == "Volkswagen ID3":
            catalog_price = 35_000
        elif brand == "BMW 5":
            catalog_price = 45_000

        # compute the tax (default 5% with 2% on electric cars)

        tax_percentage = 0.05
        if brand in ["Tesla Model 3", "Volkswagen ID3"]:
            tax_percentage = 0.02

        tax = tax_percentage * catalog_price

        print("Registration complete. Vehicle information")
        print(f"Brand: {brand}")
        print(f"ID: {vehicle_id}")
        print(f"License Plate: {license_plate}")
        print(f"Payable Tax: {tax}")


if __name__ == "__main__":
    app = Application()
    app.register_vehicle("Tesla Model 3")
