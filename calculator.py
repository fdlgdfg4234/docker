from flask import Flask
app = Flask(__name__)

@app.route('/')
def calculator():

  while True:

        a = float(input("Введите первое число: "))
        operator = input("Введите операцию: ")
        b = float(input("Введите второе число: "))


        if operator == '+':
             c = a + b
             print(c)
             continue
        elif operator == '-':
             c = a - b
             print(c)
             continue
        elif operator == '*':
             c = a * b
             print(c)
             continue
        elif operator == '/':
             c = a / b
             print(c)
             continue

