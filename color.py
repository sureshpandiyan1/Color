from tkinter import *

welcs = Tk()

cnts, anim_gifs = 5, [PhotoImage(file='./images/color.gif',format = 'gif -index %i' %(i)) for i in range(5)]

def color_center(z,w,h):
    x, y = round(z.winfo_screenwidth() - 425), round(z.winfo_screenheight() - 205)
    z.geometry('{}x{}+{}+{}'.format(w,h,round(x / 2),round(y / 2.2)))

def color_animation_runs(cnn):
    try:
        cnn += 1
        cnn = 0 if cnn == cnts else cnn
        label.configure(image=anim_gifs[cnn])
        welcs.after(100, color_animation_runs,cnn)
    except: 
        pass


welcs.overrideredirect(1)
color_center(welcs,423,203)
label = Label(welcs)
label.pack()

welcs.after(200, color_animation_runs, 0)
welcs.after(3000, welcs.destroy)
welcs.mainloop()


app = Tk()
app.geometry(("212x230"))
color_center(app,"212","230")
app.wm_resizable(0,0)
app.title("Color")
v2 = DoubleVar()
v1 = DoubleVar()
v3 = DoubleVar()

zx = []


def nothing(x):
        pass


clrs = []
plm = []
def slids(e):
    app.config(background="#%02x%02x%02x" % (s.get(),j.get(),c.get()), width=100, height=50)
    with open("colors.txt","w") as pol:
        print("#%02x%02x%02x" % (s.get(),j.get(),c.get()),file=pol)

app.iconbitmap("./images/color.ico")

j = Scale(app, variable=v2, from_=0, to=255, orient=HORIZONTAL, length=206, command=slids, background="#fff")
j.pack(anchor = CENTER, side="bottom",padx=10,pady=20)
j.place(relx = 0.50,rely = 0.57,anchor =CENTER, height=40)

s = Scale(app, variable=v1, from_=0, to=255, orient=HORIZONTAL, length=206, command=slids, background="#fff")
s.pack(anchor = CENTER, side="bottom",padx=10,pady=20)
s.place(relx = 0.50,rely = 0.4,anchor =CENTER, height=40)


c = Scale(app, variable=v3, from_=0, to=255, orient=HORIZONTAL, length=206, command=slids, background="#fff")
c.pack(anchor = CENTER, side="bottom",padx=10,pady=20)
c.place(relx = 0.50,rely = 0.7445,anchor =CENTER, height=40)



def sszz():
    with open("colors.txt","r") as m:
        app.clipboard_clear()
        app.clipboard_append(m.read().strip())



Button(app, text="copy me!!", command=sszz, width=200, background="#000", \
    foreground="#fff", font=("segoi ui", 14), cursor="hand2").pack(side="bottom")




app.mainloop()