class Passenger:
    def __init__(self):
        self.required_fields = ['title', 'first_name', 'last_name', 'email', 'mobile', 'address', 'city', 'state', 'country', 'passport_number', 'passport_expiry', 'child_name', 'child_birthdate']
        self.passenger_info = {}

    def add_field(self, key, value):
        self.passenger_info[key] = value

    def validate(self):
        for field in self.required_fields:
            if field not in self.passenger_info:
                return False
        return True

# Usage example
passenger = Passenger()
passenger.add_field('title', 'Mr.')
passenger.add_field('first_name', 'John')
passenger.add_field('last_name', 'Doe')
passenger.add_field('email', 'john.doe@example.com')
passenger.add_field('mobile', '123-456-7890')
passenger.add_field('address', '123 Main St')
passenger.add_field('city', 'Anytown')
passenger.add_field('state', 'CA')
passenger.add_field('country', 'USA')
passenger.add_field('passport_number', '123456789')
passenger.add_field('passport_expiry', '2025-01-01')
passenger.add_field('child_name', 'Jane Doe')
passenger.add_field('child_birthdate', '2010-05-15')

if passenger.validate():
    print("Passenger information is complete.")
else:
    print("Please provide all required passenger information.")