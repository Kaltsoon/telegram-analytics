# Telegram Analytics

Command line tool for analysing messages in a Telegram chat. Originally implemented for analysing messages in the [Full Stack Open](https://fullstackopen.com/) course's Telegram channel.

## What does it do?

The tool works in two steps:

1. **Process messages**. This step reads the messages from a JSON file and extracts "tags" from the messages. Tag is anything with a category and text, for example `(keyword, algorithm)`. Tag extranction is handled by the [tag extractors](./src/tag_extractors). Once the tags have been extracted, messages and tags are saved into a SQLite database.

2. **Analyse messages**. This step analyses the messages. You can for example list most frequent tags in the messages.

## Requirements

[Poetry](https://python-poetry.org/) and Python version `>= 3.9`.

## How to use?

1. Install dependencies by running `poetry install`.

2. Export chat history as JSON from Telegram and store the JSON file into the `data` directory.

3. Process messages by running `poetry run python src/process.py --input-file <filename>` where `<filename>` is the name of the export file in the `data` directory.

4. Analyse messages. Check available commands by running `poetry run python src/analyse.py --help`.
