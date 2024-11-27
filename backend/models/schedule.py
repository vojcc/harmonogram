from backend.models.group import Group

class Schedule:
    def __init__(self):
        self.groups = []
        self.subject = ''

    def add_group(self, group: Group) -> None:
        self.groups.append(group)

    def get_group_by_index(self, index: int) -> Group:
        return self.groups[index]

    def set_subject(self, subject: str) -> None:
        self.subject = subject
    
    def to_dictionary(self) -> dict:
        return {
            'subject': self.subject,
            'groups': [group.to_dictionary() for group in self.groups],
        }
    