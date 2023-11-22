# data_node1.py

import os

class DataNode1:
    def __init__(self):
        self.storage_folder = 'file_storage/data_node1'
        os.makedirs(self.storage_folder, exist_ok=True)

    def store_file(self, filename, content):
        file_path = os.path.join(self.storage_folder, filename)
        with open(file_path, 'w') as file:
            file.write(content)

    def retrieve_file(self, filename):
        file_path = os.path.join(self.storage_folder, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content retrieved from DataNode1: {content}")
            return content
