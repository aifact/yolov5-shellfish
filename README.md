# yolov5-shellfish

This demo is using [yolov5](https://github.com/ultralytics/yolov5) framework.
Most of the codes are copied from there in their original form and directory structure.
Two additional files are added as required to train a model.
- `models/custom_yolov5s.yaml`
- `data.yaml`

### Additional files created for deploying on Bedrock
#### Training a model
- `bedrock.hcl`: Set Bedrock configuration
- `requirements-train.txt`: Requirements for training
- `task_train.py`: Training script entry point
- `utils_s3.py`: AWS utility functions

#### Serving
- `requirements-serve.txt`: Requirements for serving
- `serve_http.py`: Serving script
- `utils_image.py`: Image utility functions

`utils_s3.py` contains some data loading functions for data stored in S3.
- This is to help in the transition from local development to AWS enviroment.
- For example, instead of `cv2.imread` to load images, replace it with `utils_s3.s3_imread`. 
- Refer to `guide_utils_s3.ipynb` for more details.

### Testing http endpoint deployment
A Streamlit app `app.py` is provided to test deployed endpoints with sample images from `test_images/`.

To run `app.py`,
- ensure that Streamlit is installed:
```
pip install streamlit
```
- run
```
streamlit run app.py
```

In the app, you will need to enter both API URL and token.
They can be retrieved from API docs of your deployed endpoint.
