from scene import *
from game_logic import PongLogic


class PongGame(Scene):
    def setup(self):
        self.background_color = 'white'
        self.logic = PongLogic(self.size.w, self.size.h)

    def update(self):
        self.logic.update()

    def draw(self):
        background(1, 1, 1)

        b = self.logic.ball
        fill(0, 0.6, 0)
        ellipse(b['x'] - b['r'], b['y'] - b['r'], b['r'] * 2, b['r'] * 2)

        bar = self.logic.bar
        fill(0, 0, 0)
        rect(bar['x'] - 5, bar['y'] - bar['h'], 10, bar['h'] * 2)

        tint(0, 0, 0)
        text('Score: {}'.format(self.logic.count * 100), font_size=24,
             x=90, y=self.size.h - 30, alignment=5)

        if self.logic.game_over:
            tint(1, 0, 0)
            text('YOU LOSE', font_size=40,
                 x=self.size.w / 2, y=self.size.h / 2, alignment=5)

    def touch_moved(self, touch):
        self.logic.move_bar_to(touch.location.y)


run(PongGame())
