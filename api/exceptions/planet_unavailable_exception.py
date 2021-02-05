from api.exceptions.api_exception import APIException


class PlanetUnavailableException(APIException):
    def __init__(self):
        Exception.__init__(self)
        self.status_code = 400
        self.message = "Planet with given name is unavailable."
