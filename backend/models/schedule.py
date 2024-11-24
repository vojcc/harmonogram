from backend.models.group import Group

class Schedule:
    def __init__(self):
        self.groups = []

    def add_group(self, group: Group):
        self.groups.append(group)

    def get_group_by_index(self, index: int):
        return self.groups[index]
    
    def to_dictionary(self):
        return {
            'groups': [group.to_dictionary() for group in self.groups],
        }
    