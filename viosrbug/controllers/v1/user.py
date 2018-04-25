import logging
import uuid

from pecan import request
from pecan.rest import RestController
from wsmeext.pecan import wsexpose

from viosrbug.controllers.v1.types.user import User


LOG = logging.getLogger(__name__)


class UsersController(RestController):

    @wsexpose(User, unicode, status_code=200)
    def get(self, user_id):
        db_conn = request.db_conn
        user = db_conn.get_user(user_id)
        return User.to_wsme_model(user)

    @wsexpose(unicode, body=User, status_code=202)
    def post(self, user_req):
        user_id = str(uuid.uuid4())
        user_req.user_id = user_id
        request.db_conn.add_user(user_req)

        res = "success add user {name}".format(name=user_req.name)
        return res

    @wsexpose([User], status_code=200)
    def get_all(self):
        db_conn = request.db_conn
        users = db_conn.list_users()
        users_list = []

        for user in users:
            LOG.info(user.id)
            LOG.info(user.user_id)
            LOG.info(user.name)
            LOG.info(user.email)

            u = User.to_wsme_model(user)
            users_list.append(u)
        return users_list
