import random

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

HANDS = ["グー", "チョキ", "パー"]


def judge(user, cpu):
    if user == cpu:
        return "あいこ！"
    wins = {
        "グー": "チョキ",
        "チョキ": "パー",
        "パー": "グー",
    }
    if wins[user] == cpu:
        return "あなたの勝ち！"
    return "あなたの負け！"


class Janken(toga.App):
    def startup(self):
        self.result_label = toga.Label(
            "手を選んでね",
            style=Pack(padding=10, font_size=18, text_align="center"),
        )

        buttons = toga.Box(
            children=[
                toga.Button(
                    hand,
                    on_press=self.play,
                    id=hand,
                    style=Pack(flex=1, padding=5),
                )
                for hand in HANDS
            ],
            style=Pack(direction=ROW, padding=10),
        )

        main_box = toga.Box(
            children=[self.result_label, buttons],
            style=Pack(direction=COLUMN, padding=10),
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def play(self, widget):
        user = widget.id
        cpu = random.choice(HANDS)
        result = judge(user, cpu)
        self.result_label.text = f"あなたは{user}。向こうは{cpu}。\n{result}"


def main():
    return Janken()
