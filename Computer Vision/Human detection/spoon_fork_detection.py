import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from glob import glob
import sys
import sklearn.metrics as metrics
from PIL import Image
import cv2

MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
model_path = "./"
PATH_TO_CKPT = model_path + MODEL_NAME + '/frozen_inference_graph.pb'

def load_graph():
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.compat.v2.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    return detection_graph


def select_boxes(boxes, classes, scores, score_threshold=0, target_class=[44, 47, 48, 50]):
    sq_scores = np.squeeze(scores)
    sq_classes = np.squeeze(classes)
    sq_boxes = np.squeeze(boxes)
    sel_ids = []
    targets = []
    for target in target_class:
        sel_ids.append(np.logical_and(sq_classes == target, sq_scores > score_threshold))
        targets.append(sq_classes[np.logical_and(sq_classes == target, sq_scores > score_threshold)])
    return [sq_boxes[sel_id] for sel_id in sel_ids], targets


class TLClassifier(object):
    def __init__(self):

        self.detection_graph = load_graph()
        self.extract_graph_components()
        self.sess = tf.compat.v1.Session(graph=self.detection_graph)

        dummy_image = np.zeros((100, 100, 3))
        self.detect_multi_object(dummy_image,0.1)
        self.traffic_light_box = None
        self.classified_index = 0

    def extract_graph_components(self):
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')

        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
    
    def detect_multi_object(self, image_np, score_threshold):

        image_np_expanded = np.expand_dims(image_np, axis=0)
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})

        sel_boxes, targets = select_boxes(boxes=boxes, classes=classes, scores=scores,
                                 score_threshold=score_threshold)


        return sel_boxes, targets

tlc=TLClassifier()

def get_annots(image_np, sel_box):
    annots_temp = []
    im_height, im_width, _ = image_np.shape
    (left, right, top, bottom) = (sel_box[1] * im_width, sel_box[3] * im_width,
                                  sel_box[0] * im_height, sel_box[2] * im_height)
    annots_temp.extend((left, top,right,  bottom))
    
    return annots_temp

def crop_roi_image(image_np, sel_box):
    im_height, im_width, _ = image_np.shape
    (left, right, top, bottom) = (sel_box[1] * im_width, sel_box[3] * im_width,
                                  sel_box[0] * im_height, sel_box[2] * im_height)
    cropped_image = image_np[int(top):int(bottom), int(left):int(right), :]
    return cropped_image

def final_detection(image_np, frame):
    boxes, anno_classes = tlc.detect_multi_object(image_np, score_threshold=0.2)
    annotations = []
    action = ''
    objects = {48 : 'fork', 50 : 'spoon', 44: 'bottle', 47: 'cup'}
    for box in boxes:
        for b in box:
            temp_annots = get_annots(image_np, b)
            annotations.append(temp_annots)

    color_space = [(0,255,0),(255,0,0),(255,0,0)]

    for anno in annotations:
        in_frame = ''
        
        anno_left = int(anno[0])
        anno_top = int(anno[1])
        anno_right = int(anno[2])
        anno_bot = int(anno[3])
        for x in anno_classes:
            if len(x) > 0:
                in_frame = int(x[0])
                print("\tClass: '{}' at [{},{},{},{}]".format(objects[in_frame], anno_left, anno_top, anno_right, anno_bot))
                if objects[in_frame].lower() == 'spoon' or objects[in_frame].lower() == 'fork':
                    action = "eat"
                elif objects[in_frame].lower() == 'cup' or objects[in_frame].lower() == 'bottle':
                    action = 'drink'
        color_class = color_space[0]
        cv2.rectangle(frame, (anno_left, anno_top), (anno_right, anno_bot), color_class, 5)
    return frame, action

# cap = cv2.VideoCapture(0)
# if cap.isOpened():
#     while True:
#         ret, frame = cap.read()
#         image_np = np.asarray(frame)  
#         frame = final_detection(image_np, frame)
#         cv2.imshow('Detect', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
