import flask

mod = flask.Blueprint('siteroot', __name__, url_prefix='')

@mod.route('/')
def home():
    return flask.render_template('siteroot/home.html')
    
