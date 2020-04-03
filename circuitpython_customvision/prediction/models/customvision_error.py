"""
An error from the custom vision service
"""


class CustomVisionError(Exception):
    """
    An error from the custom vision service
    """

    def __init__(self, message):
        super(CustomVisionError, self).__init__(message)
        self.message = message
