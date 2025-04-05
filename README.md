# Image Prediction Project

This repository contains a machine learning model trained for image prediction. The model is deployed through a Python script and can be used to analyze images from the provided sample folder.

## Project Structure

The complete directory structure is available in `structure.txt`.

Main components:
- `Predict.py`: Script for running predictions on images
- `hackByte3.0_Parameter_Tuning.ipynb`: Notebook containing training processes and results for multiple trial models
- `HackByte3.0_best_parameter_tuned.ipynb`: Notebook containing the final model training and results
- `Final_Model.ipynb`: Notebook containing the final model training and results
- `best.pt`: The trained model weights from the final model
- `runs/`: Directory containing training runs data from parameter tuning
- `runs (1)/`: Directory containing training runs data from final model
- `runsFinal`: Directory containing training runs data from final model
- `Sample img/`: Folder containing sample images for testing
- `structure.txt`: Complete file and directory structure of the project

## Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Prediction Script

To analyze an image using the trained model:

```bash
python Predict.py
```

By default, the script will use the image path specified in the code. You can modify the `image_path` variable in `Predict.py` to test different images from the "Sample img" folder.

## Model Training

### Parameter Tuning
The notebook `hackByte3.0_Parameter_Tuning.ipynb` contains experiments with various hyperparameters and model configurations. This includes:
- Multiple model training sessions
- Hyperparameter optimization
- Performance metrics for each configuration

The training results and metrics can be found in the `runs/` directory.

### Best_parameter_Tuned
The notebook `HackByte3.0_best_parameter_tuned.ipynb` contains the training process for the best parameters for the model traniing which includes:
- Training configuration
- Evaluation metrics
- Final model selection

The final model's weights are saved as `best.pt`, and additional training artifacts can be found in the `runs (1)/` directory.

### Final Model
The notebook `Final_Model.ipynb` contains Final Trained model With Data augmentation by methords like varible saturation,noise,etc which include:
- Training configuration
- Evaluation metrics
- Final model selection


## Sample Images

The repository includes a set of sample images in the "Sample img" folder that can be used to test the model. To try different images, modify the `image_path` in `Predict.py`.

## Model Information
The notebooks `HackByte3.0_best_parameter_tuned.ipynb` and `hackByte3.0_Parameter_Tuning.ipynb` are trained using https://app.roboflow.com/sdpgnsfnsfsfgr/onodgdnsfdosifnsfsf/1
The final model was trained using https://app.roboflow.com/sdpgnsfnsfsfgr/onodgdnsfdosifnsfsfaccrusion/1. Note:Models are strictly train on Data provided in problem Statement data is just uploaded at Roboflow for just easy accessibility.

The required packages are listed in `requirements.txt`. Make sure to install them using the commands provided in the Setup section.
