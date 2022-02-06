import io

import pandas as pd
from fastapi.responses import StreamingResponse


class Weather:
    def __init__(self, path):
        self.path = path

    async def get_csv(self):
        stream = io.StringIO()
        with open(self.path, encoding='UTF8') as csvfile:
            for line in csvfile:
                stream.write(line)

        response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')

        return response

    async def get_json(self):
        stream = io.StringIO()

        csv_file = pd.DataFrame(pd.read_csv(self.path, sep=";", header=0, index_col=False))
        csv_file.to_json(stream, orient="records", date_format="epoch", double_precision=10,
                         force_ascii=True, date_unit="ms", default_handler=None)
        response = StreamingResponse(iter([stream.getvalue()]), media_type='text/json')
        return response

# преорбазование
# repositori
