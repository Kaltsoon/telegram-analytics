from tag_extractors.tag_extractor import TagExtractor


class ComposedTagExtractor(TagExtractor):
    def __init__(self, *extractors):
        self._extractors = extractors

    def extract_tags(self, message):
        tags = []

        for extractor in self._extractors:
            tags = tags + extractor.extract_tags(message)

        return tags
