from oauth2client.service_account import ServiceAccountCredentials


def load_credentials_from_json(credentials):
    """
    Load Google Service Account key file from json

    :param credentials: path to json key file
    :return: credential object
    """
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    return credentials
