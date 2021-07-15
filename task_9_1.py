import tkinter


class TrafficLight(tkinter.Tk):
    __color = ['красный', 'желтый', 'зеленый']

    def __init__(self):
        self.color = TrafficLight.__color[0]
        super().__init__()
        self.title('Traffic Light')
        self.geometry('230x290')
        self.canvas = tkinter.Canvas(self, width=100, height=280, bg='#303030')
        self.red = self.canvas.create_oval(10, 10, 90, 90, fill='#5E2129')
        self.yellow = self.canvas.create_oval(10, 100, 90, 180, fill='#916300')
        self.green = self.canvas.create_oval(10, 190, 90, 270, fill='#002f1f')
        self.canvas.pack()
        self.update()
        self.after(500, self.running)

    def running(self):
        if self.color == TrafficLight.__color[0]:
            self.canvas.itemconfigure(self.green, fill='#002f1f')
            self.canvas.itemconfigure(self.red, fill='#FF0000')
            self.color = TrafficLight.__color[1]
            self.after(7000, self.running)
        elif self.color == TrafficLight.__color[1]:
            self.canvas.itemconfigure(self.red, fill='#5E2129')
            self.canvas.itemconfigure(self.yellow, fill='#fff600')
            self.color = TrafficLight.__color[2]
            self.after(2000, self.running)
        else:
            self.canvas.itemconfigure(self.yellow, fill='#916300')
            self.canvas.itemconfigure(self.green, fill='#66ff00')
            self.color = TrafficLight.__color[0]
            self.after(7000, self.running)


turn_on_traffic_light = TrafficLight()
turn_on_traffic_light.mainloop()
