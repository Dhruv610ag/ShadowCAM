# 🎥 Virtual Camera Controller

A real-time **video streaming and background manipulation** app powered by **FastAPI**, **OpenCV**, **YOLOv8**, and **pyvirtualcam**.  
This tool detects people in webcam feeds and allows you to apply:
- 📷 Custom backgrounds
- 🌫️ Blur effects
- 🚫 Black backgrounds

> Perfect for building a privacy-respecting, locally running virtual camera system.

---

## 🚀 Features

- 🧠 Person segmentation with YOLOv8
- 🎛️ Real-time camera input control
- 🖼️ Background options: blur, default image, black
- 🪞 Outputs to a virtual webcam using `pyvirtualcam`
- 🌐 Web-based UI with FastAPI + HTML/CSS + JavaScript

---

## 🛠️ Tech Stack

| Component      | Tech                        |
|----------------|-----------------------------|
| Backend        | FastAPI, OpenCV, YOLOv8     |
| Frontend       | Vanilla JS, HTML, CSS       |
| Streaming      | pyvirtualcam                |
| ML Inference   | Ultralytics YOLOv8 (Seg)    |

---

## 📂 Project Structure

```
├── main.py                  # FastAPI app
├── stream_utils.py          # Streaming + segmentation logic
├── engine.py                # YOLOv8 mask and background methods
├── static/
│   ├── index.html           # Frontend UI
│   ├── style.css            # Styling for UI
│   ├── background.jpg       # Default custom background
│   └── logo_image.png       # Logo shown on UI
```

---

## 🧪 Requirements

Make sure you have Python 3.8+ installed.

Install dependencies via Conda or pip:

```bash
# Using Conda
conda create -n virtualcam python=3.9
conda activate virtualcam
pip install -r requirements.txt
```

**requirements.txt**
```text
fastapi
uvicorn
opencv-python
ultralytics
pyvirtualcam
torch
```

---

## 🖥️ Running the App

### 1. Clone the Repository

```bash
git clone https://github.com/Dhruv610ag/virtual-camera-controller.git
cd virtual-camera-controller
```

### 2. Start the FastAPI Server

```bash
python main.py
```

### 3. Open the UI

Navigate to [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📸 Sample Preview

![UI Screenshot](./static/screenshot.png) <!-- Replace with actual screenshot if available -->

---

## ✅ Usage Instructions

1. **List Devices** → Detect connected cameras
2. **Choose Camera** → Select your desired webcam
3. **Adjust FPS, Blur & Background**
4. **Start Streaming** → Begin virtual output
5. Use the output stream in apps like Zoom, OBS, Teams, etc.

---

## 🤖 YOLOv8 Model

This project uses the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) segmentation model:
```bash
pip install ultralytics
```

Make sure the model file is available (it downloads automatically on first use):
- `yolov8m-seg.pt` is loaded internally.

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Dhruv Agarwal**  
Deep Learning & Computer Vision Engineer  
GitHub: [@Dhruv610ag](https://github.com/Dhruv610ag)

---
