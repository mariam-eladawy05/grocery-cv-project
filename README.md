# Smart Grocery Recognition & Calorie Estimator

A computer vision project that detects grocery items in images and estimates their calorie content using an ensemble of two deep learning models.

---

## Team

| Name | 
|------|
| Maram Eladawy | 
| Nourallah Ghonim | 

Course: Computer Vision — [Course Code]  
Submission date: [Date]

---

## Project overview

This project tackles the problem of automatic food recognition and nutritional estimation from a single image. Given a photo of grocery items or a meal, the system:

1. Detects and localizes each item using YOLOv8 (object detection)
2. Classifies each item with higher precision using EfficientNet-B0 (image classification)
3. Fuses both model outputs using a weighted ensemble
4. Estimates calorie content per item using the USDA FoodData Central database

---

## Demo

![Demo screenshot](results/demo_screenshot.png)

---

## Models

| Model | Type | Base | Task |
|-------|------|------|------|
| YOLOv8n | Object detection | COCO pretrained | Localize & label grocery items |
| EfficientNet-B0 | Image classification | ImageNet pretrained | Fine-grained food classification |

Both models are fine-tuned on the Freiburg Groceries Dataset with custom annotated images added.

---

## Results

| Model | Metric | Score |
|-------|--------|-------|
| YOLOv8 (solo) | mAP50 | xx.x% |
| EfficientNet (solo) | Top-1 accuracy | xx.x% |
| Ensemble (fused) | Top-1 accuracy | xx.x% |

---

## Dataset

- **Base dataset**: [Freiburg Groceries Dataset](https://github.com/PhilJd/freiburg_groceries_dataset) — 25 classes, ~5000 images
- **Custom annotations**: xx images annotated manually using Roboflow
- **Augmentations**: horizontal flip, brightness/contrast shift, mosaic

### Classes

```
apple, banana, bread, butter, carrot, cheese, chicken, chocolate,
coffee, egg, fish, grape, juice, milk, mushroom, onion, orange,
pasta, potato, rice, soda, tomato, water, yogurt, ... (25 total)
```

---

## Project structure

```
grocery_project/
│
├── data/
│   ├── raw/                        # Original downloaded dataset
│   └── annotated/
│       ├── images/
│       │   ├── train/
│       │   ├── val/
│       │   └── test/
│       └── labels/
│           ├── train/
│           ├── val/
│           └── test/
│
├── models/                         # Saved model weights
│   ├── yolov8_best.pt
│   └── efficientnet_best.pth
│
├── notebooks/                      # Jupyter exploration notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_yolo_training.ipynb
│   └── 03_efficientnet_training.ipynb
│
├── src/
│   ├── train_yolo.py               # YOLOv8 training script
│   ├── train_efficientnet.py       # EfficientNet training script
│   ├── fusion.py                   # Ensemble fusion logic
│   ├── calorie_lookup.py           # USDA API integration
│   └── evaluate.py                 # Evaluation & metrics
│
├── app/
│   └── app.py                      # Gradio demo app
│
├── results/                        # Plots, metrics, sample predictions
│
├── data.yaml                       # YOLOv8 dataset config
├── requirements.txt
└── README.md
```

---

## Setup & installation

```bash
# Clone the repo
git clone https://github.com/yourusername/grocery_project.git
cd grocery_project

# Create virtual environment
python -m venv grocery_env
grocery_env\Scripts\activate       # Windows
source grocery_env/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## How to run

### Train YOLOv8
```bash
python src/train_yolo.py
```

### Train EfficientNet
```bash
python src/train_efficientnet.py
```

### Run the demo app
```bash
python app/app.py
```

Then open your browser at `http://localhost:7860`

---

## Bonus contributions

- [x] Custom data annotation (xx images labeled via Roboflow)
- [x] Dataset augmentation (flip, brightness, mosaic)
- [ ] Third model — depth/portion size estimation (MiDaS)

---

## References

- Jocher, G. et al. (2023). YOLOv8. Ultralytics. https://github.com/ultralytics/ultralytics
- Tan, M. & Le, Q. (2019). EfficientNet: Rethinking Model Scaling for CNNs. ICML.
- Philipp Jund et al. Freiburg Groceries Dataset. https://github.com/PhilJd/freiburg_groceries_dataset
- USDA FoodData Central. https://fdc.nal.usda.gov/
