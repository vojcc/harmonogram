from datetime import datetime

class DayNameResolver:
    @staticmethod
    def get_day_name(date: str) -> str:
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%A")
