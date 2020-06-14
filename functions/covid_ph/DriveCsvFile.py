import pandas as pd
import requests
from io import StringIO


class DriveCsvFile:

    def __init__(self, file_id, download_url="https://drive.google.com/" +
                                             "uc?export=download&id="):
        self.file_id = file_id
        self.download_url = download_url
        self.csv_data_frame = None
        self.get_csv_data_frame()

    def get_csv_data_frame(self):
        file_url = self.download_url + self.file_id
        url = requests.get(file_url).text
        csv_raw = StringIO(url)
        self.csv_data_frame = pd.read_csv(csv_raw)

    def update_file_id(self, file_id):
        self.file_id = file_id
        self.get_csv_data_frame()
