from backend.enums.language import Language
from backend.helpers.colors_mapper import ColorsMapper
from backend.helpers.day_name_resolver import DayNameResolver
from backend.helpers.day_name_translator import DayNameTranslator
from backend.models.day import Day
from backend.models.group import Group
from backend.models.lesson import Lesson
from backend.models.schedule import Schedule
from backend.helpers.time_converter import TimeConverter

import re

class ScheduleContentTransformer:
    EIGHT_AM_HOUR = 480
    SEVEN_PM_HOUR = 1140

    GROUP_LIST = [
        "01 IwB",
        "02 IwB",
        "03 IwB",
        "04 IwB",
        "05 IwB",
        "06 IwB",
        "07 IwB",
    ]

    @staticmethod
    def extract_lesson_and_teacher(text):
        match = re.match(r"(.+?)\s*(?:\([^)]*\))?\s*\((.+)\)$", text)

        if match:
            lesson_name = match.group(1)
            teacher = match.group(2)
            return lesson_name, teacher
        else:
            return '', ''

    @staticmethod
    def transform(rows: list):
        rows_count = 0
        filtered_rows = []
        rows_in_day = len(ScheduleContentTransformer.GROUP_LIST)

        for row in rows:
            if rows_count == rows_in_day + 1:
                rows_count = 0
            if rows_count != 0:
                filtered_rows.append(row)
            rows_count += 1

        schedule = Schedule()

        for group_name in ScheduleContentTransformer.GROUP_LIST:
            group = Group(group_name)
            schedule.add_group(group)

        rows_count = 0
        hour_in_minutes = ScheduleContentTransformer.EIGHT_AM_HOUR
        date = ''

        for row in filtered_rows:
            if hour_in_minutes == ScheduleContentTransformer.SEVEN_PM_HOUR:
                hour_in_minutes = ScheduleContentTransformer.EIGHT_AM_HOUR

            if rows_count == rows_in_day:
                rows_count = 0

            cells = row.find_all('td')

            if rows_count == 0:
                raw_date = cells[0].find('b').text.strip()
                date = raw_date.replace('.', '-')

                start_iteration_index = 2
            else:
                start_iteration_index = 1

            group = schedule.get_group_by_index(rows_count)


            day_name = DayNameResolver.get_day_name(date)
            day_name = DayNameTranslator.translate(day_name, Language.POLISH)

            day = Day(date, day_name)

            for cell in cells[start_iteration_index:]:
                if cell.text == '\xa0\xa0\xa0':
                    duration = 15
                else:
                    duration = int(cell.attrs['colspan']) * 15
                    lesson_name_abbr = cell.text.strip()
                    teacher_name = ''

                    if 'title' in cell.next.attrs:
                        lesson_and_teacher = cell.next.attrs['title']
                        lesson_name, teacher_name = ScheduleContentTransformer.extract_lesson_and_teacher(lesson_and_teacher)
                    else:
                        lesson_name = lesson_name_abbr
                        lesson_name_abbr = ''

                    color = 'gray'
                    if hasattr(cell.next, 'next'):
                        if hasattr(cell.next.next, 'attrs'):
                            color = cell.next.next.attrs['color']
                            color = ColorsMapper.map(color)

                    lesson = Lesson(
                        name = lesson_name,
                        name_abbr = lesson_name_abbr,
                        teacher_name = teacher_name,
                        start_hour = TimeConverter.minutes_to_hours(hour_in_minutes),
                        end_hour = TimeConverter.minutes_to_hours(hour_in_minutes + duration),
                        duration = duration,
                        color = color
                    )

                    day.add_lesson(lesson)
                hour_in_minutes += duration

            group.add_day(day)
            rows_count += 1
        
        return schedule