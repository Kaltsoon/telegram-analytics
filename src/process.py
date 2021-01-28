import os
import click

from tag_extractors.part_tag_extractor import PartTagExtractor
from tag_extractors.keyword_tag_extractor import KeywordTagExtractor
from tag_extractors.composed_tag_extractor import ComposedTagExtractor
from tag_extractors.exercise_tag_extractor import ExerciseTagExtractor
from message_writers.database_message_writer import DatabaseMessageWriter
from message_readers.file_message_reader import FileMessageReader

from database.database_connection import get_database_connection

from initialize_database import initialize_database
from message_processor import MessageProcessor


@click.command()
@click.option('--input-file', default='input.json', help='File that contains the chat history in JSON format.')
def process(input_file):
    initialize_database()

    dirname = os.path.dirname(__file__)

    message_reader = FileMessageReader(
        os.path.join(dirname, '..', 'data', input_file)
    )

    message_writer = DatabaseMessageWriter(get_database_connection())

    tag_extractor = ComposedTagExtractor(
        PartTagExtractor(),
        ExerciseTagExtractor(),
        KeywordTagExtractor()
    )

    message_processor = MessageProcessor(
        message_reader,
        message_writer,
        tag_extractor
    )

    message_processor.process_messages()


if __name__ == '__main__':
    process()
