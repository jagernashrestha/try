from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_system:
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognitization system")
        #background 
        img1 = Image.open(r"C:\Users\dell\Desktop\PROJECT2\back.jpg")
        img1 = img1.resize((1500,750))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x = 0, y = 0,width = 1500, height = 750)
        
        # #purbanchal
        # img2 = Image.open(r"C:\Users\dell\Desktop\PROJECT2\Purbanchal.jpg")
        # img2 = img2.resize((120,90))
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # f_lbl = Label(self.root,image=self.photoimg2)
        # f_lbl.place(x = 40, y = 10,width = 120, height = 90)

        # # acme
        # img3 = Image.open(r"C:\Users\dell\Desktop\PROJECT2\acme.png")
        # img3 = img3.resize((120,90))
        # self.photoimg3 = ImageTk.PhotoImage(img3)
        
        # f_lbl = Label(self.root,image=self.photoimg3)
        # f_lbl.place(x = 1190, y = 10,width = 120, height = 90)
        
        # # mona
        # img4 = Image.open(r"C:\Users\dell\Desktop\PROJECT2\mona.jpg")
        # img4 = img4.resize((250,90))
        # self.photoimg4 = ImageTk.PhotoImage(img4)
        
        # f_lbl = Label(self.root,image=self.photoimg4)
        # f_lbl.place(x = 550, y = 10,width = 250, height = 90)
        
        title_lbl =Label(img1,text ="FACE RECOGINITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg ="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()