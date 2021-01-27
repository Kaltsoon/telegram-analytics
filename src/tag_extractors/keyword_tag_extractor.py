from keybert import KeyBERT
from entities.tag import Tag
from tag_extractors.tag_extractor import TagExtractor

model = KeyBERT('distilbert-base-nli-mean-tokens')


class KeywordTagExtractor(TagExtractor):
    def extract_tags(self, message):
        keywords = model.extract_keywords(
            message.text,
            keyphrase_ngram_range=(1, 1),
            stop_words=None
        )

        tags = [Tag('keyword', keyword, message.id) for keyword in keywords]

        return tags
