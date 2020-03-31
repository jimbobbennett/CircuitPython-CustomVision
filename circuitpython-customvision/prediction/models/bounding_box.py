class BoundingBox():
    """Bounding box that defines a region of an image.

    All required parameters must be populated in order to send to Azure.

    :param left: Required. Coordinate of the left boundary.
    :type left: float
    :param top: Required. Coordinate of the top boundary.
    :type top: float
    :param width: Required. Width.
    :type width: float
    :param height: Required. Height.
    :type height: float
    """

    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        self.left = left
        self.top = top
        self.width = width
        self.height = height
