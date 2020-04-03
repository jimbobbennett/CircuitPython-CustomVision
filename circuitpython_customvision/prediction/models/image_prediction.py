import json
from .prediction import Prediction
from .bounding_box import BoundingBox


class ImagePrediction:
    """Result of an image prediction request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Prediction Id.
    :vartype id: str
    :ivar project: Project Id.
    :vartype project: str
    :ivar iteration: Iteration Id.
    :vartype iteration: str
    :ivar created: Date this prediction was created.
    :vartype created: datetime
    :ivar predictions: List of predictions.
    :vartype predictions:
     list[~_customvision.prediction.models.Prediction]
    """

    def __init__(self, response) -> None:

        if not isinstance(response, dict):
            response = json.loads(response)

        self.prediction_id = response["id"]
        self.project = response["project"]
        self.iteration = response["iteration"]
        self.created = response["created"]
        self.predictions = []

        for pred in response["predictions"]:
            box = pred["boundingBox"]
            bounding_box = BoundingBox(left=box["left"], top=box["top"], width=box["width"], height=box["height"])
            prediction = Prediction(
                probability=pred["probability"], tag_id=pred["tagId"], tag_name=pred["tagName"], bounding_box=bounding_box
            )
            self.predictions.append(prediction)
