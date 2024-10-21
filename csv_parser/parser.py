import csv
import io

class CSVParser:
    def parse(self, file):
        parsed_rows = []

        text_stream = io.TextIOWrapper(file, encoding='utf-8')
        reader = csv.DictReader(text_stream)

        for row in reader:
            parsed_row = {
                key: (None if value in ("", "NULL") else value)
                for key, value in row.items() if key is not None
            }
            parsed_rows.append(parsed_row)

        return parsed_rows