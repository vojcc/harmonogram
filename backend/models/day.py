from backend.models.lesson import Lesson

class Day:
    def __init__(self, date: str, name: str):
        self.date = date
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: Lesson) -> None:
        self.lessons.append(lesson)

    def to_dictionary(self) -> dict:
        return {
            'date': self.date,
            'name': self.name,
            'lessons': [lesson.to_dictionary() for lesson in self.lessons],         
        }
    