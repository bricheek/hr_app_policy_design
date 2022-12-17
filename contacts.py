from representations import AsDictionaryMixin

class AddressBook:
    def __init__(self):
        self._employee_addresses= {
            1 : Address('123 Main St', 'Dover', 'NH', '03820'),
            2 : Address('45 Sandpiper Dr', 'Dover', 'NH', '03820', 'Apt 3'),
            3 : Address('500 Anywhere St', 'Manchester', 'NH', '03301'),
            4 : Address('4 Park Ave', 'New York', 'NY', '01101'),
            5 : Address('209 Midwood Pl', 'Westfield', 'NJ', '07090'),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address

class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2 = ''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

    