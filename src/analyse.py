import click
from tabulate import tabulate
from database.database_connection import get_database_connection
from analysers.database_analyser import DatabaseAnalyser

connection = get_database_connection()

analyser = DatabaseAnalyser(connection)


@click.group()
def analyse():
    pass


@analyse.command('most-frequent-tags', help="List most frequent tags in the messages.")
@click.option('--category', default=None, help="Only list tags in the given category.")
@click.option('--with-category', default=None, help="Only list tags which are also present in a message with a tag with the given category.")
@click.option('--with-text', default=None, help="Only list tags which are also present in a message with a tag with the given text.")
@click.option('--limit', default=50, help="Limit the numbers of tags.")
def most_frequent_tags(category, with_category, with_text, limit):
    tags_with_counts = analyser.get_most_frequent_tags(
        category,
        with_category,
        with_text,
        limit,
    )

    table = [[t[0].category, t[0].text, t[1]] for t in tags_with_counts]

    print(tabulate(table, headers=['Category', 'Text', 'Count']))


if __name__ == '__main__':
    analyse()
