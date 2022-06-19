class ContactException(Exception):
    ...


class ContactNotFoundError(ContactException):
    def __init__(self):
        self.status_code = 404
        self.detail = "ContactSchema Info Not Found"


class ContactAlreadyExistError(ContactException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Contact  Already Exists"
