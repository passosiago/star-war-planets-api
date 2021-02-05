from api.exceptions.api_exception import APIException


class PlanetMissingFieldsException(APIException):
    def __init__(self):
        Exception.__init__(self)
        self.status_code = 400
        self.message = "name, climate or terrain field is missing."
