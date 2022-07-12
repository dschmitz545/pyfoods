def init_app(app):
    app.config["SECRET_KEY"] = "abacate"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///delivery.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['FLASK_ADMIN_SWATCH'] = "united"

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
