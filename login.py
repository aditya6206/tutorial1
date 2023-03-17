from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\CODING\python\Image\mountains-under-mist-morning-amazing-260nw-1725825019")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,rewidth=1,reheight=1)




        if __name__=="__main__":
            root=Tk()
            app=Login_window(root)

 
