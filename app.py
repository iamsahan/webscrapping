import tkinter as tk
from tkinter import scrolledtext
import subprocess
import json
import os

class ScrapyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrapy Desktop Application")

        self.run_button = tk.Button(root, text="Run Scrapy", command=self.run_scrapy)
        self.run_button.pack(pady=10)

        self.output_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output_area.pack(padx=10, pady=10)

    def run_scrapy(self):
        # Ensure the output file is removed before running Scrapy
        output_file = "output.json"
        if os.path.exists(output_file):
            os.remove(output_file)
        
        # Run the Scrapy spider and save output to JSON file
        process = subprocess.Popen(['scrapy', 'crawl', 'example', '-o', output_file], cwd='myproject', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if stderr:
            self.output_area.insert(tk.END, stderr.decode('utf-8'))
        else:
            with open(output_file, 'r') as f:
                data = json.load(f)
                json_output = json.dumps(data, indent=4)
                self.output_area.insert(tk.END, json_output)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrapyApp(root)
    root.mainloop()
