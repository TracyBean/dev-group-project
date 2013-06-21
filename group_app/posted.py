import flask, flask.views
import utils

class Posted(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('posted.html')
