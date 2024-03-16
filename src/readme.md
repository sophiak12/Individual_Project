# Readme

* The data used in the code are present in the data folder. The data in `src/audioData.csv` was not part of the coprus but put together from the data extracted using OpenSMILE which was then cleaned and preprocessed.
* The code is split into three main files. 
* `src/audioManipulations.ipynb` includes the statistical analysis done to the data and `src/statisticalAnalysis.ipynb` is a collection of the results used from `src/audioManipulations.ipynb`
* `src/models.ipynb` uses the scikit-learn library and includes all code relating to the use of machine learning.
* `src/audioCorreations.ipynb` includes all the statistical analysis & visualisations done to the audio features extracted using openSMILE.

To run the code, simply run the notebook cells in order.

## Build instructions

### Requirements
* Python version used: Python 3.8.5
* Packages: listed in `requirements.txt` 

### Build steps
`pip install -r requirements.txt` 
