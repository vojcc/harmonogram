import json
from backend.models.schedule import Schedule

class JsonHandler:
    @staticmethod
    def load(filename: str, schedule: Schedule) -> None:
        with open(f"../data/{filename}.json", "w", encoding="utf-8") as json_file:
            json.dump(
                schedule.to_dictionary(),
                json_file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Schedule data has been saved to data/{filename}.json")
