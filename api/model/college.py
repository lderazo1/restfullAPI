class College:
    def __init__(self, id, name, area):
        self.id = id
        self.name = name
        self.area = area

    # Setter methods
    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_area(self, area):
        self.area = area

    # Getter methods
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area
