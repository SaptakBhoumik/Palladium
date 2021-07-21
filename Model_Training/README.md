## Getting Started
Clone this repository<br>
```git clone https://github.com/SaptakBhoumik/Palladium.git```

Cd to this directory<br>
```cd Palladium/Model_Training```

After that run the following command to install required dependencies<br>
```pip3 install -r requirements.txt```

## Training the model to predict lung disease using x ray
Download the dataset from https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia and extract it in this folder  <br>

Start the training using the following command<br>
```python3 training_lung_disease_detection_model_xray.py```

## Training the model to predict lung disease using ct scan
Download the dataset from https://www.kaggle.com/azaemon/preprocessed-ct-scans-for-covid19 and extract it in this folder. After that create two folders named train and test within the archive folder. After that create two folders named COVID19 and NORMAL in both train and test directory. Now the your final task is to move half of the images from the ./Original CT Scans/nCT folder to ./train/NORMAL folder and the other half to ./test/NORMAL and then move half of the images from the ./Original CT Scans/pCT folder to ./train/COVID19 folder and the other half to ./test/COVID19 <br>

Start the training using the following command<br>
```python3 training_lung_disease_detection_ctscan.py```
