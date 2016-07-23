import flask
from web_site.web.siteroot.controller import mod as siteroot_module


def _build_app(config_to_use,
               template_folder='web/templates',
               static_folder='web/static'):
    app = flask.Flask(__name__,
                      template_folder=template_folder,
                      static_folder=static_folder)
    app.config.from_object(config_to_use)
    app.register_blueprint(siteroot_module)
    return app


def main():
    config = 'config.Config'
    app = _build_app(config)

    # the config in the below line is NOT the config class above
    app.run(host=app.config['DASHBOARD_HOST'],
            port=app.config['DASHBOARD_PORT'],
            debug=app.config['DEBUG'])

if __name__ == '__main__':
    main()
