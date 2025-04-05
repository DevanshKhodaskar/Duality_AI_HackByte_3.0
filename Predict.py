def run_inference(image_path, model_path="best.pt", show=True):
    from ultralytics import YOLO
    import cv2

    # Load model
    model = YOLO(model_path)
    class_names = model.names  # get class names from model

    # Run inference
    results = model(image_path)

    # Show results using OpenCV
    if show:
        for r in results:
            plotted_img = r.plot()
            cv2.imshow("YOLOv8 Detection", plotted_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    return results, class_names


if __name__ == "__main__":
    image_path = "Sample img/000000000.png"
    model_path = "best.pt"
    results, class_names = run_inference(image_path, model_path, show=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = class_names.get(cls_id, f"Unknown Class {cls_id}")
            print(f"Detected: {class_name} ({conf:.2f})")

    print("Inference completed.")
