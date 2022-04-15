class CustomException(Exception):  # extends Exception
    def __init__(self, desc, pack):
        self.desc = desc
        self.pack = pack


class AlreadyOccupied(CustomException):
    pass


class TooManyRequests(CustomException):
    pass


class UnknownException(CustomException):
    pass


class StickersTooMuch(CustomException):
    pass


class StickerPackInvalid(CustomException):
    """Gerado se o pacote de adesivos foi excluído pelo usuário final"""
    pass
