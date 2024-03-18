import random


class Unit:
    def __init__(self, unit_id=None, unit_code=None, unit_name='No_name', unit_capacity=10):
        if unit_id is None:
            unit_id = self.generate_unit_id()
        if unit_code is None:
            unit_code = self.generate_unit_code()
        self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {self.unit_capacity}"

    @staticmethod
    def generate_unit_id():
        all_unit = Unit.read_unit()
        unit_id = str(random.randint(1000000, 9999999))
        while unit_id in [i.unit_id for i in all_unit]:
            unit_id = str(random.randint(10000, 99999))
        return unit_id

    @staticmethod
    def generate_unit_code():
        all_unit = Unit.read_unit()
        unit_code = str(random.randint(1000000, 9999999))
        while unit_code in [i.unit_code for i in all_unit]:
            unit_code = str(random.randint(10000, 99999))
        return unit_code

    @staticmethod
    def read_unit():
        all_unit = []
        f = open('data/unit.txt')
        f_data = [i for i in f.read().split('\n') if i]
        for row in f_data:
            unit = row.split(', ')
            all_unit.append(Unit(*unit))
        f.close()
        return all_unit

    @staticmethod
    def write_unit(all_unit):
        f = open('data/unit.txt', 'w')
        for unit in all_unit:
            f.write(str(unit) + '\n')
        f.close()