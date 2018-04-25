import six
import wsme

from viosrbug import model


class User(model.Base):

    # Required field
    name = wsme.wsattr(six.text_type, mandatory=True)

    # Optional fields
    email = wsme.wsattr(six.text_type, mandatory=False)

    # Readonly field
    user_id = wsme.wsattr(six.text_type, mandatory=False)
    id = wsme.wsattr(int, mandatory=False, readonly=True)
