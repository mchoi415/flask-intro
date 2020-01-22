"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi this is the homepage!</title>
      </head>
      <body>
      <h1>Hi this is the homepage!</h1>
          <p> Link to hello page:
          <a href="http://0.0.0.0:5000/hello">The hello page</a>
          </p>
      </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
             
            Choose a compliment:
            <select name="compliment">
                <option value="awesome">awesome</option>
                <option value="terrific">terrific</option>
                <option value="fantastic">fantastic</option>
                <option value="neato">neato</option>
                <option value="fantabulous">fantabulous</option>
                <option value="wowza">wowza</option>
                <option value="oh-so-not-meh">oh-so-not-meh</option>
                <option value="brilliant">brilliant</option>
                <option value="ducky">ducky</option>
                <option value="coolio">coolio</option>
                <option value="incredible">incredible</option>
                <option value="wonderful">wonderful</option>
                <option value="smashing">smashing</option>
                <option value="lovely">lovely</option>
                <input type="submit" value="Submit">

                </form>
        <form action="/diss"> 
         Who you wanna dish it to? <input type="text" name="person">
            Choose a diss:
            <select name="diss">
                <option value="toxic">toxic</option>
                <option value="vapid">vapid</option>
                <option value="rude">rude</option>
                <option value="stupid">stupid</option>
                <input type="submit" value="Submit">
            </form>
      
      </body>
    </html>
    """

@app.route("/diss")
def diss_person():
    """Diss person"""

    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)


@app.route("/greet")
def greet_person():
    """Get user by name."""
    print(request.args)
    player = request.args.get("person")


    #compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
