class OptClass:
        def __init__(self):
                self.weights = './yolov5/runs/exp8_i2_PA+pano_yolov5x_results/weights/best_i2_PA+pano_yolov5x_results.pt'
                self.source = 'inference/images'
                self.output = 'inference/output'
                self.img_size = 640
                self.conf_thres = 0.4
                self.iou_thres = 0.5
                self.device = ''
                self.view_img = None
                self.save_txt = None
                self.classes = None
                self.agnostic_nms = None
                self.augment = None
                self.update = None

opt = OptClass()

print('opt.output=', opt.weights)