import io
from typing import Callable

from fastapi.responses import StreamingResponse


class CSVService:

    @staticmethod
    def convert_data_to_csv_response(data_list: list, headers: str, line_writer: Callable) -> StreamingResponse:
        stream = io.StringIO()

        stream.write(headers)

        for model in data_list:
            line = line_writer(model)
            stream.write(line)

        response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')
        response.headers['Content-Disposition'] = 'attachment; filename=export.csv'

        return response
