import flask, flask.views
import utils

class Validate(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('validate.html')
