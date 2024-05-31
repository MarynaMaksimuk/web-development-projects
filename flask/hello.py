from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center" >Hello, World!</h1>'
            '<p>This is paragraph</p>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3lxdnBtenhqM2Y5cm80M3owczZ5bHB1Z2VsazR0aXN6bXg4NWxxMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gyRWkLSQVqlPi/giphy.gif" '
            'width=400/>')


@app.route("/bye")
@make_bold
@underline
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
