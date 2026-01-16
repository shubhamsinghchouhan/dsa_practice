from enum import Enum
from datetime import datetime, timedelta


# 1. गाड़ी और स्पॉट के प्रकार के लिए Enums
class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


# 2. Vehicle (Base Class)
class Vehicle:
    def __init__(self, plate_num, v_type):
        self.plate_num = plate_num
        self.v_type = v_type


class Car(Vehicle):
    def __init__(self, plate_num):
        super().__init__(plate_num, VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self, plate_num):
        super().__init__(plate_num, VehicleType.BIKE)


# 3. Parking Spot Class
class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_free = True
        self.parked_vehicle = None

    def assign_vehicle(self, vehicle):
        self.is_free = False
        self.parked_vehicle = vehicle

    def remove_vehicle(self):
        self.is_free = True
        self.parked_vehicle = None


# 4. Ticket Class
class Ticket:
    def __init__(self, vehicle, spot):
        self.ticket_id = f"TIC-{datetime.now().strftime('%M%S')}"
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now() - timedelta(hours=2)  # टेस्ट के लिए 2 घंटे पहले का समय


# 5. Parking Lot (Main Controller - Singleton Pattern logic)
class ParkingLot:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance.spots = [
                ParkingSpot("A1", VehicleType.BIKE),
                ParkingSpot("B1", VehicleType.CAR),
                ParkingSpot("C1", VehicleType.TRUCK)
            ]
        return cls._instance

    def entry(self, vehicle):
        for spot in self.spots:
            if spot.is_free and spot.spot_type == vehicle.v_type:
                spot.assign_vehicle(vehicle)
                ticket = Ticket(vehicle, spot)
                print(
                    f"✅ Entry: {vehicle.v_type.name} ({vehicle.plate_num}) parked at {spot.spot_id}. Ticket ID: {ticket.ticket_id}")
                return ticket
        print(f"❌ Error: No free spot for {vehicle.v_type.name}")
        return None

    def exit(self, ticket):
        # Hourly Rate Logic (Strategy)
        duration = datetime.now() - ticket.entry_time
        hours = max(1, round(duration.total_seconds() / 3600))
        rate = 20 if ticket.vehicle.v_type == VehicleType.CAR else 10
        amount = hours * rate

        # Spot खाली करना
        ticket.spot.remove_vehicle()
        print(f"🏁 Exit: {ticket.vehicle.plate_num} stayed for {hours} hours. Total Bill: ₹{amount}")
        print(f"✨ Spot {ticket.spot.spot_id} is now free.")


# --- कोड को रन करने के लिए (Main Execution) ---

if __name__ == "__main__":
    my_parking_lot = ParkingLot()

    # 1. एक कार अंदर आई
    my_car = Car("MP-09-AB-1234")
    my_ticket = my_parking_lot.entry(my_car)

    print("-" * 30)

    # 2. गाड़ी बाहर निकली
    if my_ticket:
        my_parking_lot.exit(my_ticket)

    print("-" * 30)

    # 3. एक और गाड़ी के लिए चेक करना (Bike)
    my_bike = Bike("MP-09-XY-9999")
    bike_ticket = my_parking_lot.entry(my_bike)