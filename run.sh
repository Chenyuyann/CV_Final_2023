cp -r /home/data/2788/ /project/train/src_repo/
cd /project/train/src_repo/
python split.py
python mask_to_yolo.py

cd /project/train/src_repo/yolov8
python train-seg.py