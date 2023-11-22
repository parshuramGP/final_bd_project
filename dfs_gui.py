import tkinter as tk
from tkinter import filedialog, messagebox
from client import Client
from master_node import MasterNode


class DFS_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Distributed File System Client")

        # Set background color
        self.master.configure(bg='#ececec')

        # Create and configure widgets
        self.create_widgets()

        # Initialize the client
        self.master_node = MasterNode()
        self.client = Client(self.master_node)

    def create_widgets(self):
        # Entry field for file path
        self.filename_entry = tk.Entry(self.master, width=50, font=('Arial', 14))
        self.filename_entry.pack(pady=10)

        # Browse file button
        self.browse_button = tk.Button(self.master, text="Browse File", command=self.browse_file, font=('Arial', 14))
        self.browse_button.pack(pady=10)

        # Upload file button
        self.upload_button = tk.Button(self.master, text="Upload File", command=self.upload_file, font=('Arial', 14))
        self.upload_button.pack(pady=10)

        # Download file button
        self.download_button = tk.Button(self.master, text="Download File", command=self.download_file, font=('Arial', 14))
        self.download_button.pack(pady=10)

        # Display metadata button
        self.display_metadata_button = tk.Button(self.master, text="Display Metadata", command=self.display_metadata, font=('Arial', 14))
        self.display_metadata_button.pack(pady=10)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        # Update the entry field with the selected file
        self.filename_entry.delete(0, tk.END)
        self.filename_entry.insert(0, filename)

    def upload_file(self):
        try:
            filename = self.filename_entry.get()
            with open(filename, 'r') as file:
                content = file.read()

            # Call the client's upload_and_download method
            self.client.upload_and_download(filename, content)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def download_file(self):
        try:
            filename = self.filename_entry.get()
            # Call the client's download_file method
            content = self.client.download_file(filename)

            if content:
                messagebox.showinfo("Download Successful", f"Content: {content}")
            else:
                messagebox.showerror("Error", "Error downloading file.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_metadata(self):
        try:
            filename = self.filename_entry.get()
            # Call the client's display_file_metadata method
            self.client.display_file_metadata(filename)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DFS_GUI(root)
    root.mainloop()
