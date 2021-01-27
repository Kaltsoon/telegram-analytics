from progress.bar import IncrementalBar
from entities.message import Message


class NopBar:
    def __init__(self, message, max):
        pass

    def next(self):
        pass

    def finish(self):
        pass


class MessageProcessor:
    def __init__(self, reader, writer, tag_extractor, verbose=True):
        self._reader = reader
        self._writer = writer
        self._tag_extractor = tag_extractor
        self._verbose = verbose

    def process_messages(self):
        self._log('Reading messages')

        messages = self._reader.read_messages()

        process_progress = self._create_progress_bar(
            'Processing messages',
            max=len(messages)
        )

        processed_messages = []

        for message in messages:
            tags = self._tag_extractor.extract_tags(message)
            message = Message(message.id, message.text, message.user_id, tags)
            processed_messages.append(message)
            process_progress.next()

        process_progress.finish()

        self._log('Writing messages')

        self._writer.write_messages(processed_messages)

        self._log('Done!')

    def _log(self, message):
        if self._verbose:
            print(message)

    def _create_progress_bar(self, message, max):
        if self._verbose:
            return IncrementalBar(message, max=max)
        else:
            return NopBar(message, max=max)
