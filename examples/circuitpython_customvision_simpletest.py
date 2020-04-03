from circuitpython_customvision.prediction.custom_vision_prediction_client import CustomVisionPredictionClient

client = CustomVisionPredictionClient("api_key", "endpoint")

predictions = client.classify_image_url(
    "project_id", "published_name", "https://www.adafruit.com/includes/templates/shop2019/images/adafruit-logo.png"
)
