import csv
import gspread
from gspread import utils

from .utils.conf import load_config
from .utils.credentials import load_credentials_from_json, load_credentials_from_dict


def export_csv(source=None, url=None, cell=None, credentials=None, config=None):
    """
    Export CSV file to Google sheet

    :param source: path to source CSV file
    :param url: destination Google Sheet url
    :param cell: destination Google Sheet cell (can include tab name: MySheet!A1)
    :param credentials: path to google service credentials file
    :param config: path to config file
    :return:
    """
    settings = load_config(config) if config is not None else None
    if settings is None and (source is None or url is None or credentials is None):
        raise ValueError('required parameters missed')

    if settings is not None:
        source = settings['source']
        url = settings['url']
        cell = settings.get('cell', 'A1')
        credentials = settings['credentials']
    else:
        cell = cell if cell is not None else 'A1'

    # TODO: add other types of credentials
    if isinstance(credentials, dict):
        credentials = load_credentials_from_dict(credentials)
    elif isinstance(credentials, str):
        credentials = load_credentials_from_json(credentials)
    else:
        credentials = None

    if credentials is None:
        raise ValueError('invalid credentials')

    with open(source, 'r') as fd:
        dialect = csv.Sniffer().sniff(fd.read(1024))
        fd.seek(0)
        csv_data = fd.read()

    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(url)

    if '!' in cell:
        tab_name, cell = cell.split('!')
        wks = sheet.worksheet(tab_name)
    else:
        wks = sheet.sheet1

    # clear old values
    clear_range = 'A1:{}'.format(utils.rowcol_to_a1(wks.row_count, wks.col_count))
    sheet.values_clear(clear_range)

    first_row, first_column = utils.a1_to_rowcol(cell)

    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": wks.id,
                    "rowIndex": first_row - 1,
                    "columnIndex": first_column - 1,
                },
                "data": csv_data,
                "type": 'PASTE_NORMAL',
                "delimiter": dialect.delimiter
            }
        }]
    }

    return sheet.batch_update(body)
