import tkinter as tk
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class App():
    def __init__(self, master):
        self.master = master
        master.title("PyDownload")

        self.show_page2_button = tk.Button(master, text="About Page", command=self.show_page2)
        self.show_page2_button.pack()

        self.label = tk.Label(master, text="Enter URL:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Download", command=self.download)
        self.button.pack()

        self.download_completed_label = tk.Label(master, text="")
        self.download_completed_label.pack(side=tk.BOTTOM)

    def download(self):
        url = self.entry.get()
        filename = url.split("/")[-1]
        urllib.request.urlretrieve(url, filename)
        self.download_completed_label.configure(text="Download completed.")

    def show_page2(self):
        self.label.configure(text="About Page")
        self.entry.pack_forget()
        self.button.pack_forget()
        self.show_page2_button.pack_forget()

        root.geometry("800x400")
        self.page2_label = tk.Label(self.master, text="Hello! I am Lumauser, the creator of this downloader! This app is used for download files from a python app. This app was made using the ")
        self.page2_label.pack()
        self.page2_button = tk.Button(self.master, text="Back to Download", command=self.show_page1)
        self.page2_button.pack()

    def show_page1(self):
        self.page2_label.pack_forget()
        self.page2_button.pack_forget()

        self.label.configure(text="Enter URL:")
        self.entry.pack()
        self.button.pack()
        self.show_page2_button.pack()

root = tk.Tk()
app = App(root)
root.mainloop()

#Test file link: https://dl.dropbox.com/s/4qjdlxj7te5x060/test.txt