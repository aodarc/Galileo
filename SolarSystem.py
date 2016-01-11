from tkinter import *


class Element(object):
    _x = int()
    _y = int()
    _mass = float()
    _radius = float()
    _is_movable = False
    color = 'red'

    def __init__(self, canvas, mass=0., radius=40):
        self._mass = mass
        self.radius = radius
        self.__canvas = canvas
        self.circle = canvas.create_oval(self.radius - 1, self.radius - 1, 1, 1, fill=self.color, width=0)

    def move(self, x, y):
        if not self._is_movable:
            return
        self.__canvas.move(self.circle, x, y)
        self._x = x  # self.__canvas.bbox(self.circle)[0]  # return posX posY x+PosX,y+PosY
        self._y = y  # self.__canvas.bbox(self.circle)[1]


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
    canvas = Canvas(root)
    canvas.config(background='#0F2A33')

    b = Element(canvas, radius=80)
    b._is_movable = True
    b.move(100, 100)

    canvas.pack(fill=BOTH, expand=1)
    root.mainloop()


main()
