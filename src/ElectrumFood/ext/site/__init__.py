from ElectrumFood.ext.site.main import bp

def init_app(app):
    app.register_blueprint(bp)
