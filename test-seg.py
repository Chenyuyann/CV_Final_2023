from ultralytics import YOLO

model = YOLO("/project/train/models/train/weights/best.pt")
results = model.predict(source="datasets/images/val", save=False)
results.save("/project/train/result-graphs")