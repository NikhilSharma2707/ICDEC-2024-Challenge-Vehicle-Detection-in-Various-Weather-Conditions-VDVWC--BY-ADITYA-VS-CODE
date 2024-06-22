import os
import shutil

# Define the paths based on your directory structure
annotation_folder = r'C:\ML Competition using pycharm\pythonProject1\Annotation'
train_folder = r'C:\ML Competition using pycharm\pythonProject1\train'
val_folder = r'C:\ML Competition using pycharm\pythonProject1\val'

# Function to copy annotations to labels folder
def copy_annotations(source_folder, dest_folder):
    # Iterate through annotation subfolders (rainy and sunny) and time of day (day and night)
    for annotation_type in ['Rainny', 'Sunny']:
        for time_of_day in ['Day', 'Night']:
            # Paths to annotation files in annotation_folder
            annotation_path = os.path.join(annotation_folder, source_folder, annotation_type, time_of_day)
            # Paths to images in dest_folder
            images_path = os.path.join(dest_folder, annotation_type, time_of_day)
            # Paths to labels folder where annotations will be copied
            labels_path = os.path.join(images_path, 'labels')

            # Create labels directory if it doesn't exist
            os.makedirs(labels_path, exist_ok=True)

            # Iterate through annotation files
            for file in os.listdir(annotation_path):
                if file.endswith('.txt'):
                    # Copy annotation file to labels directory
                    shutil.copy(os.path.join(annotation_path, file), os.path.join(labels_path, file))

# Copy annotations to train labels folder
copy_annotations('train', train_folder)

# Copy annotations to val labels folder
copy_annotations('val', val_folder)

print("Annotations copied successfully!")


import os

# Define the paths based on your directory structure
train_folder = r'C:\ML Competition using pycharm\pythonProject1\train'
val_folder = r'C:\ML Competition using pycharm\pythonProject1\val'

def load_annotations_and_images(folder):
    annotations = []
    images = []

    # Iterate through annotation subfolders (rainy and sunny) and time of day (day and night)
    for annotation_type in ['Rainny', 'Sunny']:
        for time_of_day in ['Day', 'Night']:
            # Paths to images in folder
            images_path = os.path.join(folder, annotation_type, time_of_day)
            images.extend([os.path.join(images_path, file) for file in os.listdir(images_path)
                           if file.endswith('.jpg') or file.endswith('.png')])

            # Paths to annotation files in folder
            annotation_path = os.path.join(folder, annotation_type, time_of_day, 'labels')
            annotations.extend([os.path.join(annotation_path, file) for file in os.listdir(annotation_path)
                                if file.endswith('.txt')])

    return images, annotations

# Load annotations and images from train folder
train_images, train_annotations = load_annotations_and_images(train_folder)
print(f"Number of training images: {len(train_images)}")
print(f"Number of training annotations: {len(train_annotations)}")

# Load annotations and images from validation folder
val_images, val_annotations = load_annotations_and_images(val_folder)
print(f"Number of validation images: {len(val_images)}")
print(f"Number of validation annotations: {len(val_annotations)}")


import cv2

# Path to an example image file
image_path = r'C:\ML Competition using pycharm\pythonProject1\train\Rainny\Day\rainy day (1).jpg'

# Load the image using cv2
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f'Failed to load image at: {image_path}')
else:
    # Display image shape
    print(f'Image shape: {image.shape}')  # This will print the dimensions of the image (height, width, channels)

    # Display the image (you can comment this out if you're running in a non-interactive environment)
    cv2.imshow('Image', image)
    cv2.waitKey(0)  # Wait indefinitely until a key is pressed
    cv2.destroyAllWindows()  # Close all OpenCV windows

print("Image loaded and displayed successfully!")



import cv2
import os

# Path to the folder containing training images
train_images_folder = r'C:\ML Competition using pycharm\pythonProject1\train'

# Path to the folder where resized images will be saved
resized_images_folder = r'C:\ML Competition using pycharm\pythonProject1\resized_train'

# Define the target size for resizing
target_size = (416, 416)  # Adjust this size based on your model's input size requirements

# Create the resized images folder if it doesn't exist
os.makedirs(resized_images_folder, exist_ok=True)

# Function to resize images
def resize_images(input_folder, output_folder, target_size):
    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Construct input and output paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the image
            image = cv2.imread(input_path)

            # Resize the image
            resized_image = cv2.resize(image, target_size)

            # Save the resized image
            cv2.imwrite(output_path, resized_image)

            # Print status
            print(f"Resized: {filename}")

# Resize images in the training folder
resize_images(train_images_folder, resized_images_folder, target_size)

print("Images resized successfully!")
