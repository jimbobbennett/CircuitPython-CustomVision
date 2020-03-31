class CustomVisionError(Exception):
    """
    An error from the custom vision service
    """
    def __init__(self, message):
        self.message = message