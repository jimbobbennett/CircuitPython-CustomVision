from .prediction import Prediction
from .bounding_box import BoundingBox
import json

class ImagePrediction():
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
     list[~circuitpython-customvision.prediction.models.Prediction]
    """

    def __init__(self, response) -> None:

        if not isinstance(response, dict):
            response = json.loads(response)

        self.id = response['id']
        self.project = response['project']
        self.iteration = response['iteration']
        self.created = response['created']
        self.predictions = []

        for p in response['predictions']:
            b = p['boundingBox']
            bounding_box = BoundingBox(left = b['left'], 
                                       top = b['top'], 
                                       width = b['width'], 
                                       height = b['height'])
            prediction = Prediction(probability = p['probability'],
                                    tag_id = p['tagId'], 
                                    tag_name = p['tagName'], 
                                    bounding_box = bounding_box)
            self.predictions.append(prediction)