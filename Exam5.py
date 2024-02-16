# -*- coding: utf-8 -*-
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root=tkinter.Tk()
root.geometry("480x480")
root.wm_title("matplotlib圖片嵌入視窗")

fig=Figure(figsize=(5,4),dpi=100)

canvas=FigureCanvasTkAgg(fig)
axc=fig.add_subplot(111)
axc.plot([1,2,3,4,5])

canvas=FigureCanvasTkAgg(fig,master=root)
canvas.draw()
canvas.get_tk_widget().pack()

toolbar=NavigationToolbar2Tk(canvas,root)
toolbar.update()
canvas.get_tk_widget().pack()

def quit():
    root.quit()
    root.destroy()
    #return 0

button=tkinter.Button(master=root,text='結束',command=quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()