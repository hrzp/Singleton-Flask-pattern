from app.server.controllers.user import user

def register_blueprints(app):
    app.register_blueprint(user,url_prefix='/user')