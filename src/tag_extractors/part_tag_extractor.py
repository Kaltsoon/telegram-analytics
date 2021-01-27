import re
from entities.tag import Tag
from tag_extractors.tag_extractor import TagExtractor

PART_REGEX = r'part *([0-9][a-z]?)'


def is_subpart(part):
    match = re.search('[a-z]$', part)

    return not match is None


def get_part_in_subpart(part):
    match = re.search('([0-9])', part)

    return match.groups(0)[0]


class PartTagExtractor(TagExtractor):
    def extract_tags(self, message):
        matches = re.findall(PART_REGEX, message.text.lower())

        parts = set()

        for match in matches:
            if is_subpart(match):
                part = get_part_in_subpart(match)
                parts.update([match, part])

            parts.update([match])

        return [Tag('part', part, message.id) for part in parts]
