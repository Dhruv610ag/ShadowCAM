import cv2
from ultralytics import YOLO  # type: ignore
import numpy as np  # noqa: F401
import torch

class CustomerSegmentationWithYolo():
    def __init__(self, erode_size=5, erode_intensity=2):
        self.model = YOLO('yolov8m-seg.pt')
        self.model.eval()
        self.background_image = cv2.imread("./static/background.jpg")
        if self.background_image is None:
            raise FileNotFoundError("Background image './static/background.jpg' not found.")
        self.erode_intensity = erode_intensity
        self.erode_size = erode_size

    def generate_mask_from_result(self, results):
        for result in results:
            if result.masks is not None and result.boxes is not None:
                masks = result.masks.data
                clss = result.boxes.cls
                people_indices = torch.where(clss == 0)
                people_masks = masks[people_indices]

                if len(people_masks) == 0:
                    return None

                people_masks = torch.any(people_masks, dim=0).to(torch.uint8) * 255
                kernel = np.ones((self.erode_size, self.erode_size), np.uint8)
                eroded_mask = cv2.erode(people_masks.cpu().numpy(), kernel, iterations=self.erode_intensity)
                return eroded_mask
        return None

    def apply_blur_with_mask(self, frame, mask, blur_strength=21):
        blur_strength = (blur_strength, blur_strength)
        blurred_frame = cv2.GaussianBlur(frame, blur_strength, 0)

        mask = (mask > 0).astype(np.uint8)
        mask_3d = cv2.merge([mask, mask, mask])
        result_frame = np.where(mask_3d == 255, frame, blurred_frame)
        return result_frame

    def apply_black_background(self, frame, mask):
        black_background = np.zeros_like(frame)
        result_frame = np.where(mask[:, :, np.newaxis] == 255, frame, black_background)
        return result_frame

    def apply_custom_background(self, frame, mask):
        background_image = cv2.resize(self.background_image, (frame.shape[1], frame.shape[0]))
        result_frame = np.where(mask[:, :, np.newaxis] == 255, frame, background_image)
        return result_frame
