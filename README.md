# ClosingPrices <br />
# Demo: https://youtu.be/dL5xT6uxCWs
Using artificial recurrent neural network, LSTM, to predict closing prices <br />


### Brief Overview:

#### Here you will find two major jupyter notebooks:
- datapredict.ipynb  <br />
- datapredict_gru.ipynb <br />

These files are where models are developed and tested. The first uses LSTM and the second uses GRU with several convolutions.  <br />

#### You will also find two major Python files:
- datapredict.py  <br /> 
- datapredictui.py  <br />

These files are where the UI and it's associated code are stored. Code that is developed and tested in the Jupyter notebook(s) is/are ported over to 'datapredict.py' for use.  <br />

### Announcements:
Initial version to be released soon (basic functionality)

Notes: In order to run, you must execute the updates seen under the imported libraries and restart runtime: <br />
!pip install --upgrade pandas-datareader <br />
!pip install --upgrade pandas <br />

Once restarted, you can run all

For the Python Module: <br />
Must have tensorflow installed: <br />
pip install tensorflow <br />

(Note, tensorflow may have trouble donwloading on certain machines due to LongPath errors, this can be updated in registry) <br />

Todo: <br />
Better plotting <br />
Improved error handling (Before release) <br />

Note: Using python 3.10 <br />
Also note: must have PyQt5, qt-material to run ui <br />
