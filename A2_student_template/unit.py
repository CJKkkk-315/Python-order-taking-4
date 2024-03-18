class Unit:
    def __init__(self, unit_id=0, unit_code='', unit_name='', unit_capacity=0):
        if unit_id:
            self.unit_id = unit_id
        else:
            self.unit_id = self.generate_unit_id()
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {self.unit_capacity}"

    def generate_unit_id(self) -> int:
        with open('data/unit.txt', 'r') as file:
            lst = []
            for line in file:
                line = line.rstrip('\n')
                if line:
                    lst.append(int(line.split(', ')[0]))
            if lst:
                return max(lst) + 1
            else:
                return 1000000
