import json
from backend.models.schedule import Schedule

class JsonHandler:
    @staticmethod
    def load(schedule: Schedule):
        with open("schedule.json", "w", encoding="utf-8") as json_file:
            json.dump(
                schedule.to_dictionary(), 
                json_file, 
                indent = 4, 
                ensure_ascii = False
            )
            
        print("Schedule data has been saved to 'schedule.json'")
