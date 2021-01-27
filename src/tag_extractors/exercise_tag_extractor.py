import re
from entities.tag import Tag
from tag_extractors.tag_extractor import TagExtractor

EXERCISE_REGEX = r'(?:exercise|ex|task) *([0-9]+\.[0-9]+)'


class ExerciseTagExtractor(TagExtractor):
    def extract_tags(self, message):
        matches = re.findall(EXERCISE_REGEX, message.text.lower())

        parts = set()
        exercises = set()

        for match in matches:
            part, number = match.split('.')

            parts.update([part])
            exercises.update([match])

        exercise_tags = [Tag('exercise', exercise, message.id)
                         for exercise in exercises]

        part_tags = [Tag('part', part, message.id) for part in parts]

        return exercise_tags + part_tags
