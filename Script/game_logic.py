class PongLogic:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ball = {
            'x': width / 2,
            'y': height / 2,
            'dirx': -6,
            'diry': -6,
            'r': 10,
        }
        self.bar = {
            'x': width - 30,
            'y': height / 2,
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
        if ny - b['r'] < 0 or ny + b['r'] > self.height:
            b['diry'] *= -1

        if (nx + b['r'] > bar['x'] - 5 and
                bar['y'] - bar['h'] < ny < bar['y'] + bar['h']):
            b['dirx'] *= -1
            self.count += 1

        if nx - b['r'] > self.width:
            self.game_over = True

        b['x'] += b['dirx']
        b['y'] += b['diry']

    def move_bar_to(self, y):
        bar = self.bar
        bar['y'] = y
        if bar['y'] - bar['h'] < 0:
            bar['y'] = bar['h']
        if bar['y'] + bar['h'] > self.height:
            bar['y'] = self.height - bar['h']


if __name__ == '__main__':
    # Windows上でGUIなしにロジックだけ確認するための簡易テスト
    logic = PongLogic(600, 400)
    for i in range(1000):
        logic.update()
        if logic.game_over:
            print('Game over at frame', i, 'score:', logic.count)
            break
    else:
        print('Still in play. ball:', logic.ball, 'score:', logic.count)
