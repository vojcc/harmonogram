class Lesson:
    def __init__(self, name: str, name_abbr: str, teacher_name: str, start_hour: str, end_hour: str, duration: int, color: str):
        self.name = name
        self.name_abbr = name_abbr
        self.teacher_name = teacher_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.duration = duration
        self.color = color

    def to_dictionary(self) -> dict:
        return {
            'name': self.name,
            'name_abbr': self.name_abbr,
            'teacher_name': self.teacher_name,
            'start_hour': self.start_hour,
            'end_hour': self.end_hour,
            'duration': self.duration,
            'color': self.color
        }
    