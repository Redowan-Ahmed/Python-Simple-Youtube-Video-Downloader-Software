# Test Chat GPT Code of GUI

""" import tkinter as tk
from tkinterhtml import HtmlFrame

class WebsiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Embedded Website in Python GUI")

        # Create and pack the HTML frame
        self.html_frame = HtmlFrame(self.root, horizontal_scrollbar="auto", vertical_scrollbar="auto")
        self.html_frame.pack(fill="both", expand=True)

        # Load your website
        website_url = "https://redowan.mercegrower.com/"
        self.html_frame.set_content(f"<iframe src='{website_url}' width='100%' height='100%'></iframe>")

root = tk.Tk()
app = WebsiteApp(root)
root.mainloop()
"""
"""
import tkinter as tk
import webbrowser

class WebsiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Open Website in Browser")

        # Create and pack the button
        self.open_button = tk.Button(self.root, text="Open Website", command=self.open_website)
        self.open_button.pack(pady=10)

    def open_website(self):
        website_url = "https://redowan.mercegrower.com/"
        webbrowser.open_new(website_url)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteApp(root)
    root.mainloop()
"""


"""
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWebEngineView
import sys

class WebsiteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Embedded Website in Python GUI")
        self.setGeometry(100, 100, 800, 600)

        # Create a WebView component
        self.webview = QWebEngineView(self)
        self.webview.setGeometry(0, 0, 800, 600)

        # Load your website
        website_url = "https://redowan.mercegrower.com/"
        self.webview.setUrl(QUrl(website_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebsiteApp()
    window.show()
    sys.exit(app.exec_())"""



# After lot's of self debugging, The code is working but not 100% as expected and Chat GPT was Unsuccessful the entire process.

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class WebsiteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Embedded Website in Python GUI")
        self.setGeometry(100, 100, 800, 600)

        # Create a WebView component
        self.webview = QWebEngineView(self)
        self.webview.setGeometry(100, 100, 800, 600)

        # Load your website
        website_url = "https://redowan.mercegrower.com/"
        self.webview.setUrl(QUrl(website_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebsiteApp()
    window.show()
    sys.exit(app.exec_())


