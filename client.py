# client.py

from master_node import MasterNode
from data_node1 import DataNode1
from data_node2 import DataNode2
from data_node3 import DataNode3

class Client:
    def __init__(self, master_node):
        self.master_node = master_node

    def upload_and_download(self, filename, content):
        try:
            upload_decision = input(f"Do you want to upload the file {filename}? (yes/no): ").lower()
            if upload_decision == 'yes':
                # Check if a new data node needs to be created
                new_data_node_decision = input("Do you want to create a new data node? (yes/no): ").lower()
                if new_data_node_decision == 'yes':
                    new_data_node_name = input("Enter the name of the new data node: ")
                    self.master_node.add_data_node(new_data_node_name)

                print(f"Uploading file: {filename}")
                self.master_node.upload_file(filename, content)
                file_info = self.master_node.download_file(filename)

                if file_info:
                    replicas = file_info['replicas']
                    print(f"File uploaded to all data nodes. It is located on these nodes: {replicas}")
                else:
                    print("Error uploading file. File metadata not found.")

                download_decision = input("Do you want to download the file? (yes/no): ").lower()
                if download_decision == 'yes':
                    content = self.download_file(filename)
                    if content:
                        print("Download successful. Content:", content)
                    else:
                        print("Error downloading file.")

                metadata_decision = input("Do you want to display file metadata? (yes/no): ").lower()
                if metadata_decision == 'yes':
                    self.display_file_metadata(filename)
            else:
                print("Upload canceled.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def download_file(self, filename):
        try:
            file_info = self.master_node.download_file(filename)
            if file_info:
                replicas = file_info['replicas']
                data_nodes = {
                    'data_node1': DataNode1(),
                    'data_node2': DataNode2(),
                    'data_node3': DataNode3(),
                }

                for replica in replicas:
                    data_node_instance = data_nodes.get(replica)
                    if data_node_instance:
                        try:
                            content = data_node_instance.retrieve_file(filename)
                            if content:
                                return content
                        except FileNotFoundError:
                            print(f"File not found in {replica}: {filename}")
                            continue
                        except Exception as e:
                            print(f"Error retrieving file from {replica}: {e}")
                            continue

                # File not found in any of the data nodes
                print(f"File not found in any data node: {filename}")
                return None
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def display_file_metadata(self, filename):
        try:
            file_info = self.master_node.download_file(filename)
            if file_info:
                print(f"Metadata for {filename}:")
                print(f"Replicas: {file_info['replicas']}")
                print(f"Size: {file_info['size']} bytes")
                # Add more metadata fields as needed
            else:
                print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        master = MasterNode()
        client = Client(master)

        # Simulate file upload and download
        client.upload_and_download("example.txt", "I am stored in all three nodes")
    except Exception as e:
        print(f"An error occurred: {e}")
