from flask import Flask
import random
number = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def guess_number():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExanNxZXpsZzd5aXFuN3lsZThrbGtydnc3eTB0anJ3MnR0eDEyNGNzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUn3CftPBajoflzROU/giphy-downsized-large.gif'/>")


@app.route("/<int:answer>")
def check_answer(answer):
    if answer > number:
        return ('<h1>Too High!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHRkaDZ2MzFkeHkxZWJ5a3M1MXJ6bm0yN3cyN3NhN2t3a3l0OTY2YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XDql3hxeMkxUSZ0PJn/giphy.gif"/>')
    elif answer < number:
        return ('<h1>Too Low!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExajFseXhsZDVocW1kcmRmeWM2djQ5Z3hucW16d2M4bTk2NmF0MmViZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3yuzRv5CcQsaLJyho4/giphy.gif"/>')
    elif answer == number:
        return ('<h1>Correct!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXJrMnJvOHlreHByZmN4MXVianViejRpdWNhazBxcjQ1cXh0Yml5eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Fa0kYLnojYqfA1f9ay/giphy.gif"/>')


if __name__ == "__main__":
    app.run(debug=True)







