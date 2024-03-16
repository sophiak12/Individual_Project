# Readme

* The data used in the code are present in the data folder. The data in audioData.csv was not part of the coprus but put together from the data extracted using OpenSMILE which was then cleaned and preprocessed.
* The code is split into three main files. 
* audioManipulations.ipynb includes the statistical analysis done to the data and finalResults.ipynb is a collection of the results used from audioManipulations.ipynb
* model.ipynb uses the scikit-learn library and includes all code relating to the use of machine learning.
* audioCorreations.ipynb includes all the statistical analysis & visualisations done to the audio features extracted using openSMILE.

To run the code, simply run the notebook cells in order.

## Build instructions

**You must** include the instructions necessary to build and deploy this project successfully. If appropriate, also include 
instructions to run automated tests. 

### Requirements

List the all of the pre-requisites software required to set up your project (e.g. compilers, packages, libraries, OS, hardware)

For example:

* Python 3.7
* Packages: listed in `requirements.txt` 
* Tested on Windows 10

or another example:

* Requires Raspberry Pi 3 
* a Linux host machine with the `arm-none-eabi` toolchain (at least version `x.xx`) installed
* a working LuaJIT installation > 2.1.0

### Build steps

List the steps required to build software. 

Hopefully something simple like `pip install -e .` or `make` or `cd build; cmake ..`. In
some cases you may have much more involved setup required.

### Test steps

List steps needed to show your software works. This might be running a test suite, or just starting the program; but something that could be used to verify your code is working correctly.

Examples:

* Run automated tests by running `pytest`
* Start the software by running `bin/editor.exe` and opening the file `examples/example_01.bin`

