import tkinter



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
LONG=None
SHORT = 5
LONG_BREAK_MIN = 20
ochered=[7,5,7,5]
timer=""
elepsetime=""

def continuetimer():
    global elepsetime
    count_D(elepsetime)

def resetpush():
    window.after_cancel(timer)
    canvasss.itemconfig(timelost, text="00:00")



def timerstart():
    count_D(int(LONG.get()))



def count_D(param):

    textmin=minforwhow=int(param/60)
    if len(str(minforwhow))==1:
        textmin="0"+str(minforwhow)
    textsec=seconds=param-(minforwhow*60)
    if len(str(textsec))==1:
        textsec="0"+str(textsec)
    canvasss.itemconfig(timelost,text=f"{textmin}:{textsec}")
    if param>0:
        global timer
        timer=window.after(1000, count_D, param-1)
        global elepsetime
        elepsetime=param


window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,background=GREEN)




canvasss=tkinter.Canvas(width=200,height=224,background=GREEN,highlightbackground=GREEN)
tomatoimg=tkinter.PhotoImage(file="tomato.png")
canvasss.create_image(102,112,image=tomatoimg)
timelost=canvasss.create_text(100,130,text="",fill="white", font=(FONT_NAME, 35, "bold"))
canvasss.grid(row=1,column=1)

resetbtn=tkinter.Button(text="Reset",background=GREEN,command=resetpush)
resetbtn.grid(row=2,column=2)
continueBTN=tkinter.Button(text="Continue", background=GREEN,command=continuetimer)
continueBTN.grid(column=1,row=4)

startbtn=tkinter.Button(text="Start",bg=GREEN,command=timerstart)
startbtn.grid(row=2,column=0)

labalTIMER=tkinter.Label(text="Timer",font=("Arial", 50,"bold"),fg=YELLOW,background=GREEN)
labalTIMER.grid(row=0,column=1)

checkboxLABEL=tkinter.Label(text="",background=YELLOW)
checkboxLABEL.grid(column=1,row=2)

LONG = tkinter.Entry(master=window)
LONG.grid(row=5,column=1,pady=10)




window.mainloop()