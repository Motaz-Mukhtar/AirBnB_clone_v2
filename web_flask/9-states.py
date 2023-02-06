#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ List all State objects """
    states = storage.all("State")
    return render_template("9-states.html", states=states)

@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """ list City objects liked to the State """
    state = storage.all("State").values()
    for i in state:
        if i.id == id:
            state = i
            break
        state = 0
    return render_template("9-states.html", state=state)

@app.teardown_appcontext
def teardown(se):
    """ remove the currnet Session  """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000", debug=1)
