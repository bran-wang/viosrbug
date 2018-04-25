from pecan import make_app
from viosrbug import model

from viosrbug.controllers.hooks import dbhook


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)
    app_hooks = [dbhook.DBHook()]

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=app_hooks,
        **app_conf
    )
