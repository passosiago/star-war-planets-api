from api.exceptions.api_exception import APIException


class PlanetAlreadyExistException(APIException):
    def __init__(self):
        Exception.__init__(self)
        self.status_code = 409
        self.message = "Planet already exist."
