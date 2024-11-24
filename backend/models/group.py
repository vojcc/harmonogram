from backend.models.day import Day

class Group:
    def __init__(self, name: str):
        self.name = name
        self.days = []

    def add_day(self, day: Day):
        self.days.append(day)

    def to_dictionary(self):
        return {
            'name': self.name,
            'days': [day.to_dictionary() for day in self.days],
        }
    