from pecan.rest import RestController
from wsmeext.pecan import wsexpose


class BugController(RestController):

    @wsexpose(unicode, status_code=200)
    def get(self):
        return "hello world"
