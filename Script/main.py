from scene import *


class PongGame(Scene):
    def setup(self):
        self.background_color = 'white'

        self.ball = {
            'x': self.size.w / 2,
            'y': self.size.h / 2,
            'dirx': -6,
            'diry': -6,
            'r': 10,
        }
        self.bar = {
            'x': self.size.w - 30,
            'y': self.size.h / 2,
            'h': 100,
        }
        self.count = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            return

        b = self.ball
        bar = self.bar

        nx = b['x'] + b['dirx']
        ny = b['y'] + b['diry']

        if nx - b['r'] < 0:
            b['dirx'] *= -1
        if ny - b['r'] < 0 or ny + b['r'] > self.size.h:
            b['diry'] *= -1

        if (nx + b['r'] > bar['x'] - 5 and
                bar['y'] - bar['h'] < ny < bar['y'] + bar['h']):
            b['dirx'] *= -1
            self.count += 1

        if nx - b['r'] > self.size.w:
            self.game_over = True

        b['x'] += b['dirx']
        b['y'] += b['diry']

    def draw(self):
        background(1, 1, 1)

        b = self.ball
        fill(0, 0.6, 0)
        ellipse(b['x'] - b['r'], b['y'] - b['r'], b['r'] * 2, b['r'] * 2)

        bar = self.bar
        fill(0, 0, 0)
        rect(bar['x'] - 5, bar['y'] - bar['h'], 10, bar['h'] * 2)

        fill(0, 0, 0)
        text('Score: {}'.format(self.count * 100), font_size=24,
             x=90, y=self.size.h - 30, alignment=5)

        if self.game_over:
            fill(1, 0, 0)
            text('YOU LOSE', font_size=40,
                 x=self.size.w / 2, y=self.size.h / 2, alignment=5)

    def touch_moved(self, touch):
        self.bar['y'] = touch.location.y
        if self.bar['y'] - self.bar['h'] < 0:
            self.bar['y'] = self.bar['h']
        if self.bar['y'] + self.bar['h'] > self.size.h:
            self.bar['y'] = self.size.h - self.bar['h']


run(PongGame())
