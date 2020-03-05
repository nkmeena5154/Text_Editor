from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from time import sleep
#from gtts import gTTS
#import os
import speech_recognition as nk

root=Tk()





class editor:
    pwd="no_file"
    def open_file(self):
        return_open=filedialog.askopenfile(initialdir="/",title="select file to open",filetypes=(("text files","*.txt"),("all files","*.*")))
        if return_open!=None:
            self.textarea.delete(1.0,END)
        for line in return_open:
            self.textarea.insert(END,line)
            self.pwd=return_open.name
        return_open.close()
    def save_as_file(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        txtsave=self.textarea.get(1.0,END)
        self.pwd=f.name
        f.write(txtsave)
        f.close
    def save(self):
        if self.pwd=="no_file":
            self.save_as_file()
        else:
            f=open(self.pwd,"w+")
            f.write(self.textarea.get(1.0,END))
            f.close()

    def new_file(self):
        self.textarea.delete(1.0,END)
        self.pwd="no_file"
    def copy_text(self):
        self.textarea.clipboard_clear()
        self.textarea.clipboard_append(self.textarea.selection_get())
    def cut_text(self):
        self.copy_text()
        self.textarea.delete("self.first","self.last")
    def paste_text(self):
        self.textarea.insert(INSERT,self.textarea.clipboard_get())
    def delete_text(self):
         self.textarea.delete(1.0,END)
    def colors_view(self):
        clr=colorchooser.askcolor(title="select color")
        #self.configure(root,background=clr[1])

     #advance tech function definition
    def speech(self):
        mk = nk.Recognizer()
        with nk.Microphone() as txt:
            print("hey, user speak to typing")
            audio = mk.listen(txt)

        try:
            text=mk.recognize_google(audio)
            #self.textarea.writelines(text)
            print(text)
        finally:
            print("thank you for using microphone")


        for line in text:
            self.textarea.insert(END, line)



        """with open('last.txt', 'r') as nkmeena:
            for i in nkmeena:
                text = text + i

        speech = gTTS(text, 'en')
        speech.save("m33.mp3")
        os.system("m33.mp3")
"""
    def zoomin(textarea):
        root.state('zoomed')

 #   def zoomout(textarea):
  #      root.attributes('-zoomed')


















    def __init__(self,rootpass):
        scroll = Scrollbar(root)
        scroll.pack(side=RIGHT, fill=Y)
        self.rootpass=rootpass
        rootpass.title("Means_editor")
        self.textarea=Text(rootpass,yscrollcommand=scroll.set)


        self.textarea.pack(fill=BOTH,expand=1)
        scroll.config(command=self.textarea.yview)

        #creating a menu
        self.main_menu=Menu()
        self.rootpass.config(menu=self.main_menu)
        #creating a file menu
        self.file_menu=Menu(self.main_menu)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        # creating a new tab
        self.file_menu.add_command(label="New", command=self.new_file)
                 #creating a "open" tab inside the file tab
        #self.open_menu=Menu(self.file_menu)
        self.file_menu.add_command(labe="Open",command=self.open_file)
        self.file_menu.add_separator()
                #creating a save tab
        self.file_menu.add_command(label="Save",command=self.save)
                  #creating a tab of "save as" inside the file menu

        self.file_menu.add_command(label="Save as",command=self.save_as_file)
        self.file_menu.add_separator()

                 #creating a exit tab
        self.file_menu.add_command(label="Exit", command=rootpass.quit)



        #creating edit menu
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="cut",command=self.cut_text)
        self.edit_menu.add_command(label="copy",command=self.copy_text)
        self.edit_menu.add_command(label="paste", command=self.paste_text)
        self.edit_menu.add_command(label="delete",command=self.delete_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Redo",command=self.textarea.edit_redo)
        self.edit_menu.add_command(label="Undo",command=self.textarea.edit_undo)


       #creating the view tab
        self.view_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(labe="View",menu=self.view_menu)
        #zoom menu inside the view menu
        self.zoom_menu= Menu(self.view_menu)
        self.view_menu.add_command(label="colors", command=self.colors_view)

        self.view_menu.add_cascade(label="Zoom", menu=self.zoom_menu)
        # next two lines inside the zoom menu
        self.zoom_menu.add_command(label="Zoom_in",command=self.zoomin)
        self.zoom_menu.add_command(label="Zoom_out")

        #creating a help menu
        self.help_menu=Menu(self.main_menu)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="View Help")
        #creating a advance tab
        self.advance_menu=Menu(self.main_menu)
        self.main_menu.add_cascade(label="Advance_Tech", menu=self.advance_menu)
        self.advance_menu.add_command(label="speech_recognizer", command=self.speech)



tt=editor(root)



root.mainloop()