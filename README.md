# Vehicle Detection In Various Weather Conditions 

This project focuses on developing an object detection model using YOLOv5, with images categorized under different weather conditions (Rainy, Sunny) and times of day (Day, Night). The model is trained to detect various vehicle types and transportation modes, including cars, motorcycles, auto rickshaws, and more.

## Project Structure

The project directory is structured as follows:

- Annotation Folder: Contains the annotations for the images, categorized into subfolders based on weather conditions (Rainy, Sunny) and time of day (Day, Night).
- Train Folder: Contains the training images, organized similarly to the annotation folder.
- Val Folder: Contains the validation images, following the same organization.

## Installation

### Prerequisites
- Python 3.x
- pip for managing Python packages
- PyTorch (for running YOLOv5)
- OpenCV (for image processing)

### Setup

- Clone the repository:


  ```bash
  
  git clone https://github.com/brucewayneoptimusprime/ICDEC-2024-Challenge-Vehicle-Detection-in-Various-Weather-Conditions-VDVWC--BY-ADITYA-VS-CODE.git
  cd ICDEC-2024-Challenge-Vehicle-Detection-in-Various-Weather-Conditions-VDVWC--BY-ADITYA-VS-CODE/pythonProject1

- Install dependencies:

  ```bash
  pip install -r yolov5/requirements.txt

- Set up the dataset:
   Ensure that the images and annotations are properly placed in the Train and Val directories as per the structure mentioned above.

## Usage

### Preprocessing

- Copy Annotations:
Use the provided script to copy annotation files from the Annotation folder to the corresponding labels folder under Train and Val.

- Resize Images:
Use the provided script to resize images to the required dimensions (e.g., 416x416) and save them in the resized_train folder.

### Model Training

- Configure dataset.yaml:
Update the dataset.yaml file with paths to the training and validation images and labels.

- Train the Model:

  Run the YOLOv5 training script:
    ```bash
  python yolov5/train.py --img 416 --batch 16 --epochs 50 --data dataset.yaml --cfg yolov5s.yaml --weights yolov5s.pt --name yolo_training
    ```
## Dataset
The dataset consists of images labeled under different weather conditions (Rainy, Sunny) and times of day (Day, Night). The classes include:

- CAR
- MOTORCYCLE
- AUTO RICKSHAW
- CYCLE RICKSHAW
- SIMPLE CYCLE
- BUS
- VAN LUGGAGE CARRIER
- TRUCK
- VAN
- TAXI
- CARRIER RICKSHAW
- E-RICKSHAW
- TRAIN
- BOAT
- PEDDLE RICKSHAW
  
