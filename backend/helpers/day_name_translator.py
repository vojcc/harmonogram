from backend.enums.language import Language

class DayNameTranslator:
    day_translation = {
        Language.POLISH: {
            "Monday": "Poniedziałek",
            "Tuesday": "Wtorek",
            "Wednesday": "Środa",
            "Thursday": "Czwartek",
            "Friday": "Piątek",
            "Saturday": "Sobota",
            "Sunday": "Niedziela"
        },
    }

    @staticmethod
    def translate(day_name: str, language: Language) -> str:
        translations = DayNameTranslator.day_translation.get(language)
        if translations:
            return translations.get(day_name, day_name)
        return day_name