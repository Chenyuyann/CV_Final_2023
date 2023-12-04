'''
实例分割训练
'''
from ultralytics import YOLO

# train
model = YOLO('/project/train/src_repo/yolov8/models/yolov8n-seg.pt')  # build from YAML and transfer weights

# Train the model
model.train(data='/project/train/src_repo/yolov8/datasets/instances-seg.yaml',  
            project = '/project/train/models', epochs=10, imgsz=1920, batch=4)