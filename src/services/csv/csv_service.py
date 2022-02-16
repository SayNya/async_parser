import csv
import io

from fastapi.responses import StreamingResponse


class CSVService:

    @staticmethod
    def get_csv_response(data_list: list, headers: str = '') -> StreamingResponse:
        if not data_list:
            raise ValueError('Empty data_list')

        if not headers:
            headers = data_list[0].keys()

        stream = io.StringIO()

        writer = csv.DictWriter(stream, fieldnames=headers)
        writer.writeheader()
        for model in data_list:
            writer.writerow(model)

        response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')
        response.headers['Content-Disposition'] = 'attachment; filename=export.csv'

        return response
