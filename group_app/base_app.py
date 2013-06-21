# Group web app
# Name: Beth and Tracy

import flask
import settings

#Views
from login import Login
from main import Main
from gallery import Gallery
from videos import Videos
from tutorial import Tutorial
from upload import Upload
from validate import Validate
from posted import Posted

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


#Routes
app.add_url_rule('/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/<page>/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/gallery/',
                view_func=Gallery.as_view('gallery'),
                methods=['GET'])
app.add_url_rule('/login/',
                view_func=Login.as_view('login'),
                methods=['GET', 'POST'])
app.add_url_rule('/videos/',
                view_func=Videos.as_view('videos'),
                methods=['GET'])
app.add_url_rule('/tutorial/',
                view_func=Tutorial.as_view('tutorial'),
                methods=['GET'])
app.add_url_rule('/upload',
                view_func=Upload.as_view('upload'),
                methods=['GET'])
app.add_url_rule('/upload',
                view_func=Validate.as_view('validate'),
                methods=['GET'])
app.add_url_rule('/upload',
                view_func=Posted.as_view('posted'),
                methods=['GET'])


@app.errorhandler(404)
def page_not_found(error):
     return flask.render_template('404.html'), 404

app.debug = True
app.run()
