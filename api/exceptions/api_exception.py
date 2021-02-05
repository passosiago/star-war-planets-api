from json import dumps

from flask import Response


class APIException(Exception):
    def __init__(self, message: str, status_code: int):
        Exception.__init__(self)
        self.status_code = status_code
        self.message = message

    def to_response(self):
        return Response(self.message, self.status_code)
