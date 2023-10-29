
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # creating a button 
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=0, column=0, padx=(10, 10) , pady=(10, 10))

        
        # creating a button 
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn.grid(row= 0, column= 1, padx=(20, 20) , pady=(20, 20))


        self.txt = tk.Entry(self.master,text='')
        self.txt.grid(row=1, column=0, rowspan=3, columnspan=7, padx=(30,40), pady=(0,0), sticky=N+E+W)
 



        



    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        htmlText = ""
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")








        



        








        

        
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
