# Trash Classifier and Can Detector


## Summary
This is a **machine learning** project that uses computer vision to classify images of trash and detect the color of trash cans to determine which bin to put the trash in.


If we had to describe this project in three (3) emojis, they would be: **😢👽🙏**

## Application Features
The project consists of two main components:
    A trash classifier that uses a convolutional neural network (CNN) to classify images of trash into six categories: cardboard, glass, metal, paper, plastic, and trash.
    A can detector that uses computer vision to detect the color of trash cans and determine which bin to put the trash in. The can detector currently supports three colors: blue (recycling), brown (waste), and green (food waste).



## Requirements
    Python 3.7 or higher
    TensorFlow 2.0 or higher
    Flask 1.1.1 or higher
    OpenCV 4.2.0 or higher
    NumPy 1.18.1 or higher
    Matplotlib 3.1.3 or higher
    
    
## Usage

### Step 1: Gather a Dataset of Trash Images
Gather a large dataset of images of various types of trash (e.g., plastic bottles, paper, glass, etc.). You can use publicly available datasets or create your own.

### Step 2: Preprocess the Images
Resize the images to a fixed size (e.g., 224x224 pixels) and normalize pixel values to the range of 0 to 1. Use data augmentation techniques, such as rotation, flipping, and zooming, to increase the diversity of the training dataset.

### Step 3: Train the Trash Classifier Model
Train a CNN model using TensorFlow to classify images of trash into the six categories. Use the preprocessed dataset from Step 2 to train the model.

### Step 4: Gather a Dataset of Trash Can Images
Gather a dataset of images of trash cans with different colors (e.g., blue, brown, and green). Label these images with their corresponding color.

### Step 5: Train the Can Detector Model
Train a computer vision model using OpenCV to detect the color of trash cans. Use the preprocessed dataset from Step 4 to train the model.

### Step 6: Build and Deploy the Flask App
Build a Flask app that uses the trained trash classifier and can detector models to classify images of trash and detect the color of trash cans. The app should enable the user to capture images from their webcam and display the classification results.



**To deploy the app, run the following command in your terminal:**

```python
python app.py
```
This will start the Flask app on your local machine. You can access the app by opening your web browser and navigating to http://localhost:5000.




## Notes

From this project, we realized how challenging it can be to create a trash classifier and organizer. But we definitely enjoyed the process and have learned a lot.

## Usage

    Open the Trash Classifier and Organizer web app in your browser.
    Capture or upload an image of the trash item you want to dispose of.
    Capture or upload images of the available trash cans for classification.
    The app will analyze the images and display the correct trash can for disposing of the trash item.
   Access the web interface at http://localhost:5000

## Contributing

If you'd like to contribute to this project, please feel free to create a pull request or open an issue.

## Credits

This project was developed by **Abdoul-Hanane Gbadamasi & Sybel Francois**. Special thanks to Organizers of the hackathon.

## License

Copyright **2023** **Abdoul-Hanane Gbadamasi & Sybel Francois**
This project is licensed under the MIT License. See the LICENSE file for more details.

 







