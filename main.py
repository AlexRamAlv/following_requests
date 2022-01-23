"""
    Genereting a flask instance to run from the console
    by using flask run command line to create the app
"""

from app import create_app, db
import os
from flask_migrate import Migrate
from app.models import Administrator, Requester, Request

#getting flask instance genetated by the function
app = create_app(os.environ.get("config") or "default")
migrate = Migrate(app, db)

# Send the variables declerd in the dict to the flask shell in 
# order to be abel to use those classes without importing them
@app.shell_context_processor
def variables_on_shell():
    return {
        "Administrator": Administrator, 
        "Requester": Requester,
        "Request": Request,
        "db": db
    }
