from services.html_content_extractor import HtmlContentExtractor
from services.schedule_content_transformer import ScheduleContentTransformer
from helpers.json_handler import JsonHandler

rows = HtmlContentExtractor.extract()
schedule = ScheduleContentTransformer.transform(rows)

JsonHandler.load(schedule)