"""Prediction result.
"""

from .bounding_box import BoundingBox


class Prediction:
    """Prediction result.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar probability: Probability of the tag.
    :vartype probability: float
    :ivar tag_id: Id of the predicted tag.
    :vartype tag_id: str
    :ivar tag_name: Name of the predicted tag.
    :vartype tag_name: str
    :ivar bounding_box: Bounding box of the prediction.
    :vartype bounding_box:
     ~circuitpython_customvision.prediction.models.BoundingBox
    """

    def __init__(self, probability: float, tag_id: str, tag_name: str, bounding_box: BoundingBox) -> None:
        self.probability = probability
        self.tag_id = tag_id
        self.tag_name = tag_name
        self.bounding_box = bounding_box
