from analysers.analyser import Analyser
from pypika import Query, Table, Field, Order, functions as fn
from entities.tag import Tag


def get_tag_by_row(row):
    message_id = row['message_id'] if 'message_id' in row else None

    return Tag(row['category'], row['text'], message_id)


class DatabaseAnalyser(Analyser):
    def __init__(self, connection):
        self._connection = connection

    def get_most_frequent_tags(
        self,
        category=None,
        with_category=None,
        with_text=None,
        limit=50
    ):
        cursor = self._connection.cursor()

        tags = Table('tags')

        query = Query.from_(tags).select(
            tags.category,
            tags.text,
            fn.Count(tags.text).as_('count')
        )

        if not category is None:
            query = query.where(tags.category == category)

        has_sub_query = with_category or with_text

        sub_query = Query.from_(tags).select(
            tags.message_id
        )

        if not with_category is None:
            sub_query = sub_query.where(tags.category == with_category)

        if not with_text is None:
            sub_query = sub_query.where(tags.text == with_text)

        if has_sub_query:
            query = query.where(tags.message_id.isin(sub_query))

        query = query.groupby(tags.text).orderby(
            Field('count'),
            order=Order.desc
        ).limit(limit)

        cursor.execute(str(query))

        rows = cursor.fetchall()

        return [(get_tag_by_row(row), row['count']) for row in rows]
