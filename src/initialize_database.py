from database.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists messages;
    ''')

    cursor.execute('''
        drop table if exists tags;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table messages (
            id text primary key,
            text text,
            user_id text
        );
    ''')

    cursor.execute('''
        create table tags (
            category text,
            text text,
            message_id text,
            foreign key(message_id) references messages(id)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
