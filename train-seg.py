from ultralytics import YOLO

# train
model = YOLO('/project/train/src_repo/yolov8/models/yolov8n-seg.pt') # 官方的预训练模型
# model = YOLO('/project/train/models/train2/weights/last.pt')  # 接着上次的模型训练，分多次训练记得改！

# Train the model
model.train(data='/project/train/src_repo/yolov8/datasets/instances-seg.yaml',  
            project = '/project/train/models', epochs=150, imgsz=1080, batch=8)
