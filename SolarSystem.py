from tkinter import *
from time import sleep


class Element(object):
    _x = int()
    _y = int()
    _mass = float()
    _is_movable = False
    speed = 1.

    def __init__(self, root, mass=0.):
        self._mass = mass
        self.__root = root
        self.photo = PhotoImage(file='image/atom50x50.png')
        self.body = Label(background='#0F2A33', image=self.photo)
        self.body.pack()

    def move(self, x=0, y=0):
        if not self._is_movable:
            return  # later add raise
        self.body.place_configure(x=x*self.speed, y=y*self.speed)
        self.__root.update()
        self._x = x
        self._y = y


class Sun(Element):
    pass


def main():
    root = Tk()
    root.title(u'Сонячна система')
    root.configure(background='#0F2A33')
    root.geometry('600x600+600+200')
    root.minsize(600, 600)
    root.maxsize(1000, 1000)
    root.protocol('WM_DELETE_WINDOW', lambda: root.quit())
    root.resizable(False, False)  # розширення вікна по ширині і по висоті

    b = Element(root)
    b._is_movable = True

    c = Element(root)
    c._is_movable = True
    c.speed = 2

    for x in range(350):
        b.move(x, x)
        c.move(x, x)  # літає швидше, якщо (х+60, х*2)
        sleep(0.01)

    root.mainloop()

main()
