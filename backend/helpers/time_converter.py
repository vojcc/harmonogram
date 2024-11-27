class TimeConverter:
    @staticmethod
    def minutes_to_hours(minutes) -> str:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours:02}:{remaining_minutes:02}"
