# import the inference-sdk
from inference_sdk import InferenceHTTPClient

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="http://detect.roboflow.com",
    api_key="###"
)

# infer on a local image
result = CLIENT.infer("YOUR_IMAGE.jpg", model_id="pepper-segmentation/1")
