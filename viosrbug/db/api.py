from sqlalchemy.orm import exc

from viosrbug.db import models as db_models
from viosrbug.db import session


class Connection(object):

    def __init__(self):
        self.session = session.get_session()

    def get_user(self, user_id):
        query = self.session.query(db_models.User).filter_by(user_id=user_id)
        try:
            user = query.one()
        except exc.NoResultFound:
            pass
        return user

    def list_users(self):
        query = self.session.query(db_models.User)
        users = query.all()
        return users

    def add_user(self, user):
        count = len(self.list_users())
        new_user = db_models.User(id=count+1,
                                  name=user.name,
                                  email=user.email,
                                  user_id=user.user_id)
        self.session.add(new_user)
        self.session.commit()

    def delete_user(self, user):
        pass
