import flask, flask.views
import utils

class Upload(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('upload.html')
