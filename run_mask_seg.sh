cp -r /home/data/2788/ /project/train/src_repo/
mkdir -p /project/train/src_repo/yolov8/datasets/labels/train
mkdir /project/train/src_repo/yolov8/datasets/labels/val

cd /project/train/src_repo/
python split.py
python mask_to_yolo.py
python train-seg.py
