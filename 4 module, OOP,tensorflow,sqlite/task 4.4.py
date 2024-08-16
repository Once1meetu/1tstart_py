from imageai.Detection import ObjectDetection
import os

exec_path = os.getcwd()

detection = ObjectDetection()
detection.setModelTypeAsRetinaNet()
detection.setModelPath(os.path.join(exec_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detection.loadModel()

list = detection.detectObjectsFromImage(input_image=(os.path.join(exec_path, "red_square.jpg")),
                                        output_image_path=(os.path.join(exec_path, "result4.jpg")))
count=0
for i in list:
    if i['name']=='person':
        count+=1
print("На картинке изображено ",count, "человека")