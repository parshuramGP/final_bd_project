# master_node.py

class MasterNode:
    def __init__(self):
        self.file_metadata = {}
        self.data_nodes = ['data_node1', 'data_node2', 'data_node3']

    def upload_file(self, filename, content):
        replicas = self.data_nodes
        self.file_metadata[filename] = {'replicas': replicas, 'size': len(content)}

    def download_file(self, filename):
        if filename in self.file_metadata:
            return self.file_metadata[filename]
        else:
            return None

    def add_data_node(self, new_data_node):
        self.data_nodes.append(new_data_node)
        print(f"Data node {new_data_node} added.")
