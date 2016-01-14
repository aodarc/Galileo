from tkinter import *
from time import sleep
from math import sqrt, pi, sin, cos


class Element(object):
    _x = int()
    _y = int()
    _mass = float()
    _is_movable = False
    speed = 1.
    img = 'atom50x50.png'

    def __init__(self, root, mass=0.):
        self._mass = mass
        self._root = root
        self.photo = PhotoImage(file='image/'+self.img)
        self.body = Label(background='#0F2A33', image=self.photo)
        self.body.image = self.photo  # hz
        self.body.pack()

    def move(self, x=0, y=0):
        if not self._is_movable:
            return  # later add raise

        self.body.place_configure(x=x % 600, y=y % 600)
        self._root.update()
        self._x = x
        self._y = y


class Sun(Element):

    def __init__(self, root, mass=0):
        self.img = 'sun50x50.png'
        Element.__init__(self, root)
        self._x = self._root.winfo_width()/2-25
        self._y = self._root.winfo_height()/2-25
        self.body.place_configure(x=self._x, y=self._y)


def main():
    root = Tk()
    root.title(u'Сонячна система')
    root.configure(background='#0F2A33')
    root.geometry('600x600+600+200')
    root.minsize(600, 600)
    root.maxsize(1000, 1000)
    root.protocol('WM_DELETE_WINDOW', lambda: root.quit())
    root.resizable(False, False)  # розширення вікна по ширині і по висоті
    root.update()

    b = Sun(root)
    b.speed = 10.

    c = Element(root)
    c._is_movable = True
    c.speed = 2.

    radius = 190
    cs = [(275 + cos(pi*x/180) * radius, 275 + sin(pi*x/180) * radius) for x in range(360)]

    for x, y in cs*4:
        c.move(x, y)
        sleep(0.001)
    root.mainloop()

main()
