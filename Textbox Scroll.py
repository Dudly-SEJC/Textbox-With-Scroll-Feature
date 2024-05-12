from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#84BF04')
message = '''
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
Ten
Eleven
Twelve
Thirteen
Fourteen
Fifteen
Sixteen
Seventeen
Eighteen
Nineteen
Twenty
'''
frame = Frame(ws)
text_box = Text(frame, height=13, width=20, wrap='word')
text_box.insert('end', message)
text_box.pack(side=LEFT, expand=True)  # allows text to appear on left side of the box
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
text_box.config(yscrollcommand=sb.set)
sb.config(command=text_box.yview)  # allows for scroll movement
frame.pack(expand=True)  # sets parameters of text box based on main GUI window automatically
ws.mainloop()