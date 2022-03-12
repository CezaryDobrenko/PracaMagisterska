class AuthenticationError(Exception):
    pass


class UnableToAddNewElement(Exception):
    pass


class UserNotExist(Exception):
    pass


class UserNotMaching(Exception):
    pass


class TeamMemberAlreadyExist(Exception):
    pass


class PermissionDenied(Exception):
    def __init__(self):
        super().__init__("You dont have permission to modify this object")


class NotFoundException(Exception):
    pass


class NotNegativeValueException(Exception):
    pass


class AlreadyExist(Exception):
    pass


class WrongStatusException(Exception):
    pass
