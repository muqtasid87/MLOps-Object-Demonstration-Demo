from ultralytics import YOLO

model_path = "model\\production\\best.pt"

model = YOLO(model_path)



def predict_img(img):
    global model
    model.predict(img)
    pass