# Colorizer - Image Colorization using Deep Learning

This project provides a web-based tool to automatically colorize black-and-white (grayscale) images using a pretrained deep learning model.

## 🌈 Features

- Upload grayscale images and get a colorized version.
- Uses OpenCV with pretrained Caffe model.
- Simple web interface with HTML frontend.
- Fast and lightweight.

## 🗂️ Project Structure

```
Colorizer-master/
├── app.py                        # Python backend using Flask
├── index.html                   # Frontend UI
├── models/                      # Pretrained deep learning models
│   ├── colorization_release_v2.caffemodel
│   ├── models_colorization_deploy_v2.prototxt
│   └── pts_in_hull.npy
├── Input_images/                # Sample input grayscale images
├── Result_images/               # Output colorized images
```

## ⚙️ Requirements

- Python 3.x
- OpenCV
- Flask
- NumPy

Install dependencies:
```bash
pip install opencv-python flask numpy
```

## 🚀 How to Run

```bash
python app.py
```

Then open your browser at:  
```
http://localhost:5000
```

Upload a grayscale image and view the colorized output.

## 📁 Sample Inputs & Outputs

- `Input_images/`: Contains example grayscale images.
- `Result_images/`: Stores the generated colorized images.

## 📜 License

This project is under the MIT License.
