from tkinter import *
from tkinter.ttk import Combobox
from numpy import *
from tkinter.ttk import Progressbar
import tkinter.messagebox
from tkinter import filedialog
from moviepy.editor import *



class Edit:
    def __init__(self,root):
        self.root=root
        self.root.title("Movie Editor")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo985.ico")
        self.root.resizable(0,0)



        url=StringVar()
        froms=IntVar()
        to=IntVar()
        rotate=IntVar()
        volume=IntVar()
        width=IntVar()


        def browse():
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("Mp4 files","*.mp4"),("all files","*.*")))
            url.set(file_path)

        def create():
            try:
                if url.get()!="":
                    if froms.get()!="Select Seconds From":
                        if to.get()!="Select Seconds To":
                            if rotate.get()!="Select Rotation":
                                if volume.get()!="Select Volume":
                                    if width.get()!="Select Width":
                                        prg.start(10)
                                        video = VideoFileClip(url.get())
                                        video=video.subclip(froms.get(),to.get())
                                        video=video.rotate(rotate.get())
                                        video=video.volumex(volume.get())
                                        video.ipython_display(width=width.get())
                                        prg.stop()
                                        
                                    else:
                                        tkinter.messagebox.showerror("Eroor","Please Select Width")

                                else:
                                    tkinter.messagebox.showerror("Eroor","Please Select Volume")

                            else:
                                tkinter.messagebox.showerror("Eroor","Please Select Rotation")

                        else:
                            tkinter.messagebox.showerror("Error","Please Select Seconds To")
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Seconds from")
                else:
                    tkinter.messagebox.showerror("Error","Please Select the file of webmm or mp4")
            except Exception as e:
                print(e) 



        def on_enter1(e):
            but_browse['background']="black"
            but_browse['foreground']="cyan"
  
        def on_leave1(e):
            but_browse['background']="SystemButtonFace"
            but_browse['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
       
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_create['background']="black"
            but_create['foreground']="cyan"
       
        def on_leave3(e):
            but_create['background']="SystemButtonFace"
            but_create['foreground']="SystemButtonText"







        def clear():
            url.set("")
            volume.set("Select Volume")
            rotate.set("Select Rotation")
            width.set("Select Width")
            froms.set("Select Seconds From")
            to.set("Select Seconds To")


#===========================frame=======================================#
        
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=365,relief="ridge",bd=3,bg="#c9c5b7")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=30,relief="ridge",bd=3)
        secondframe.place(x=0,y=365)

#===========================firstframe=====================================#
        
        but_browse=Button(firstframe,text="Browse",width=19,font=('times new roman',12),cursor="hand2",command=browse)
        but_browse.place(x=150,y=10)
        but_browse.bind("<Enter>",on_enter1)
        but_browse.bind("<Leave>",on_leave1)

        ent_movie_url=Entry(firstframe,width=50,font=('times new roman',12),relief="ridge",bd=3,textvariable=url)
        ent_movie_url.place(x=40,y=50)

        lab_subclip=Label(firstframe,text="Please Select the seconds to edit",font=('times new roman',12),bg="#c9c5b7",fg="black")
        lab_subclip.place(x=150,y=80)

        from_list=list(range(1,181))
        from_combo=Combobox(firstframe,values=from_list,font=('arial',10),width=19,state="readonly",textvariable=froms)
        from_combo.set("Select Seconds From")
        from_combo.place(x=40,y=110)

        to_list=list(range(1,181))
        to_combo=Combobox(firstframe,values=to_list,font=('arial',10),width=19,state="readonly",textvariable=to)
        to_combo.set("Select Seconds To")
        to_combo.place(x=290,y=110)

        lab_rotation=Label(firstframe,text="Please Select Rotations",font=('times new roman',12),bg="#c9c5b7",fg="black")
        lab_rotation.place(x=170,y=150)

        rotation_list=[90,-90,180,-180]
        rotation_combo=Combobox(firstframe,values=rotation_list,font=('arial',10),width=18,state="readonly",textvariable=rotate)
        rotation_combo.set("Select Rotation")
        rotation_combo.place(x=170,y=180)

        lab_volume=Label(firstframe,text="Please Select Volume",font=('times new roman',12),bg="#c9c5b7",fg="black")
        lab_volume.place(x=180,y=220)

        volume_list=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,\
                       1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
        volume_combo=Combobox(firstframe,values=volume_list,font=('arial',10),width=18,state="readonly",textvariable=volume)
        volume_combo.set("Select Volume")
        volume_combo.place(x=170,y=250)

        lab_width=Label(firstframe,text="Please Select width",font=('times new roman',12),bg="#c9c5b7",fg="black")
        lab_width.place(x=180,y=280)

        width_list=list(range(100,801,5))
        width_combo=Combobox(firstframe,values=width_list,font=('arial',10),width=18,state="readonly",textvariable=width)
        width_combo.set("Select Width")
        width_combo.place(x=170,y=310)


        but_create=Button(firstframe,width=13,text="Create",font=('times new roman',12),cursor="hand2",command=create)
        but_create.place(x=10,y=200)
        but_create.bind("<Enter>",on_enter3)
        but_create.bind("<Leave>",on_leave3)

        but_clear=Button(firstframe,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=350,y=200)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)
        



#===========================secondframe====================================#
        
        prg=Progressbar(secondframe,length=486,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=0)



if __name__ == "__main__":
    root=Tk()
    app=Edit(root)
    root.mainloop()
