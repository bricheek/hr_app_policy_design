
class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError ('not a valid role_id')
        return role_type()

    def track(self, employees, hours):
        print('Productivity Report')
        print('=====================')
        for employee in employees:
            employee.work(hours)
        print('')
        
class ManagerRole:
    def work(self, hours):
        print(f'-screams and yells for {hours} hours.')

class SecretaryRole:
    def work(self, hours):
        print(f'-spends {hours} hours doing paperwork.')

class SalesRole:
    def work(self, hours):
        print(f'-spends {hours} hours on the phone.')

class FactoryRole:
    def work(self, hours):
        print(f'-makes gadgets for {hours} hours.')