from services.html_content_extractor import HtmlContentExtractor
from services.schedule_content_transformer import ScheduleContentTransformer
from helpers.json_handler import JsonHandler

subjects = [
    {
        "name": "Informatyka w biznesie",
        "slug": "informatyka-w-biznesie",
        "url": "https://plan.ue.wroc.pl/l_pozycjaplanu1.php?se=56&gr=135/1",
    },
]

for subject in subjects:
    rows = HtmlContentExtractor.extract(subject['url'])
    schedule = ScheduleContentTransformer.transform(rows)
    schedule.set_subject(subject['name'])
    JsonHandler.load(subject['slug'], schedule)