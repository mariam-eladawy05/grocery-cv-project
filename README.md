# Smart Grocery Recognition & Nutrition Estimator

A computer vision project that recognizes grocery and supermarket products from images using deep learning classification and object detection models, then estimates nutrition information using the USDA FoodData Central API.

---

# Team

| Name |
|------|
| Nourallah Ghonim |
| Maram Eladawy |


Course: Computer Vision — AIN3105

---

# Project Overview

This project focuses on automatic grocery and supermarket product recognition from images.

The system combines:
- Object detection
- Image classification
- Nutrition estimation

into one complete deep learning pipeline.

The project supports:
- Grocery image classification
- Egyptian supermarket product recognition
- Randomized dataset testing
- Nutrition estimation for food products
- YOLO object localization for real-world scenes

---

# Final Pipeline

The final pipeline works as follows:

```text
Input Image
→ Product Detection (YOLOv8)
→ Product Classification (ResNet50 / MobileNetV2)
→ Food Check
→ USDA Nutrition API
→ Final Nutrition Output
```

For dataset testing:
- Full images are classified directly because dataset images are already centered.

For real-world applications:
- YOLOv8 can first localize products before classification.

---

# Models Used

| Model | Type | Task |
|------|------|------|
| YOLOv8n | Object Detection | Product localization |
| ResNet50 | Image Classification | Main grocery classifier |
| MobileNetV2 | Image Classification | Lightweight comparison model |

All models use pretrained ImageNet/COCO weights and are fine-tuned for grocery recognition tasks.

---

# Why Multiple Models Were Used

The project satisfies the requirement:

> Implement two different pretrained models and combine their outputs.

The system combines:
- YOLOv8 for localization
- ResNet50 for classification

MobileNetV2 was also added for comparison and evaluation.

---

# Datasets

## 1. Freiburg Groceries Dataset

Main grocery classification dataset.

Features:
- 25 grocery classes
- ~5000 images
- Single-product grocery images

Dataset:
https://github.com/PhilJd/freiburg_groceries_dataset

Examples of classes:
- pasta
- coffee
- milk
- rice
- cereal
- juice
- yogurt
- chips
- soda

---

## 2. Egyptian Products Dataset

Additional local supermarket products dataset used to extend the system with Egyptian brands and products.

Examples:
- Bisco Misr
- Indomie
- Heinz
- Tea products
- Chips products

This dataset improves real-world supermarket recognition.

---

# Notebook Structure

## classification.ipynb

Contains:
- Dataset loading
- Data augmentation
- MobileNetV2 training
- ResNet50 training
- Model evaluation
- Accuracy comparison
- Model saving

---

## detection.ipynb

Contains:
- YOLOv8 object detection
- Random image testing
- Bounding box visualization
- Object crop generation
- Detection explanation

---

## final_pipeline.ipynb

Contains:
- Full grocery recognition pipeline
- Random testing from both datasets
- Model loading
- Product prediction
- Nutrition API integration
- Food/non-food filtering
- Final visualization

---

# Results

## Freiburg Dataset

| Model | Validation Accuracy |
|------|------|
| MobileNetV2 | ~69% |
| ResNet50 | ~77% |

ResNet50 achieved better performance and was selected as the main classifier.

---

# Important Technical Discussion

## Why YOLO labels may appear incorrect

YOLOv8n is pretrained on the COCO dataset, not grocery-specific datasets.

Therefore:
- object localization works correctly
- class labels may sometimes be incorrect

Example:
- milk carton detected as "toothbrush"

This is expected behavior for generic pretrained YOLO models.

---

## Why full-image classification was used

Freiburg dataset images are:
- centered
- clean
- mostly single-product images

Using YOLO crops sometimes reduced classification accuracy.

Therefore:
- dataset testing uses full-image classification
- YOLO is reserved for real-world scenes and webcam usage

---

# USDA Nutrition API

The project integrates the USDA FoodData Central API to estimate nutrition information for detected food products.

Returned information may include:
- calories
- protein
- carbohydrates
- fats

Non-food products are automatically skipped.

---

# Bonus Features

- [x] Multiple pretrained models
- [x] YOLO + ResNet integrated pipeline
- [x] Egyptian dataset extension
- [x] Randomized testing pipeline
- [x] Nutrition API integration
- [x] Data augmentation
- [x] Food/non-food filtering
- [x] Dataset cleaning and improvement

---

# Setup & Installation

```bash
git clone https://github.com/yourusername/grocery-cv-project.git

cd grocery-cv-project

python -m venv grocery_env

grocery_env\Scripts\activate

pip install -r requirements.txt
```

---

# Running the Project

## Classification Notebook

```bash
jupyter notebook notebooks/classification.ipynb
```

## Detection Notebook

```bash
jupyter notebook notebooks/detection.ipynb
```

## Final Pipeline

```bash
jupyter notebook notebooks/final_pipeline.ipynb
```

---

# Project Structure

```text
grocery-cv-project/
│
├── data/
├── models/
├── notebooks/
├── results/
├── src/
│   └── nutrition_api.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# References

YOLOv8 — Ultralytics  
https://github.com/ultralytics/ultralytics

ResNet50 — He et al.  
https://arxiv.org/abs/1512.03385

MobileNetV2 — Sandler et al.  
https://arxiv.org/abs/1801.04381

Freiburg Groceries Dataset  
https://github.com/PhilJd/freiburg_groceries_dataset

USDA FoodData Central  
https://fdc.nal.usda.gov/
