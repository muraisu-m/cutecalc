# 電卓 Level0

import sys
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

# メイン関数
def main():
    root = tk.Tk()
    root.configure(bg="#f7f8fa")
    root.title("calc")
    den = Dentaku(root)
    root.mainloop()

# 電卓クラス
class Dentaku():
    # 作成
    def __init__(self, root):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TButton",
            font=("JK Maru Gothic", 18),
            padding=10
        )

        self.tf = tk.Frame(root,bg="#ebd9f1")    # トップレベルのフレーム
        self.tf.grid(column = 0, row = 0)
        self.value = 0
        self.op = None
        self.new_input = True
 


        # ボタンを配置
        ButtonDef = (
        #     行 列 ラベル 関数
            (4, 0, "0", self.numinput),
            (3, 0, "1", self.numinput),
            (3, 1, "2", self.numinput),
            (3, 2, "3", self.numinput),
            (2, 0, "4", self.numinput),
            (2, 1, "5", self.numinput),
            (2, 2, "6", self.numinput),
            (1, 0, "7", self.numinput),
            (1, 1, "8", self.numinput),
            (1, 2, "9", self.numinput),
            (4, 1, "*", self.mul),
            (4, 2, "/", self.div),
            (1, 3, "-", self.sub),
            (2, 3, "+", self.add),
            (3, 3, "=", self.equal),
            (4, 3, "C", self.clear))

        root.option_add('*Button.font', 'Meiryo 28')

        for r, c, label, func in ButtonDef:
            Button = ctk.CTkButton(
                self.tf, 
                text = label,
                corner_radius=18,
                width=60,
                height=60,
                fg_color="#fcf7fb",
                text_color="#222222",
                hover_color="#f7c6e6",
                command=lambda f=func, t=label: f(t)
            )

            Button.grid(column = c, row = r, sticky = tk.N +tk.E + tk.S + tk.W)

        # 数字が表示される「エントリー」
        root.option_add('*Entry.font', 'Meiryo 20')
        self.NumBox = tk.Entry(
            self.tf, 
            justify="right",
            bd=1,
            bg="#fcf7fb",
            fg="#222222"
           )
        self.NumBox.insert(tk.END, "0")
        self.NumBox.grid(
            column = 0, columnspan = 4, row = 0
            )

    # ボタン毎の動作を定義（イベントドライバ群）
    def numinput(self, num):            # 数字キー

        if self.new_input:
            self.NumBox.delete(0,tk.END)
            self.NumBox.insert(tk.END,num)
            self.new_input = False
        else:
            if self.NumBox.get() == "0":
                self.NumBox.delete(0, tk.END)
            self.NumBox.insert(tk.END, num)

    def calc(self):
        current = float(self.NumBox.get())

        if self.op == "+":
            self.value += current
        elif self.op == "-":
            self.value -= current
        elif self.op == "*":
            self.value *= current
        elif self.op == "/":
            if current != 0:
                self.value /= current
            else:
                self.NumBox.delete(0, tk.END)
                self.NumBox.insert(tk.END, "Error")
                self.value = 0
                self.op = None
                return

        else:
            self.value = current

        if self.value.is_integer():
            display = str(int(self.value))
        else:
            display = str(self.value)

        self.NumBox.delete(0, tk.END)
        self.NumBox.insert(tk.END, display)

    def add(self, _=None):
        self.calc()
        self.op = "+"
        self.new_input = True

    def sub(self, _=None):
        self.calc()
        self.op = "-"
        self.new_input = True

    def mul(self, _=None):
        self.calc()
        self.op = "*"
        self.new_input = True

    def div(self, _=None):
        self.calc()
        self.op = "/"
        self.new_input = True
    def equal(self, _=None):
        self.calc()
        self.op = None
        self.new_input = True
    def clear(self, _=None):
        self.value = 0
        self.op = None
        self.new_input = True
        self.NumBox.delete(0, tk.END)
        self.NumBox.insert(tk.END, "0")

if __name__ == '__main__':
    main()