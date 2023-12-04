# DAAN 570 Deep Learning Group Project
## Controlling an Unmanned Aerial Vehicle (UAV) with Hand Gestures using Vision Transformers (ViT)

### Project Setup
To ensure you have all the necessary packages required to run this project run the venv_setup shell script to install required packages and start your virtual environment.
An example command to do this is:
```
./venv_setup.sh && source .venv/Scripts/activate
```
If you receive package dependency errors please ensure that you have sourced your newly installed packages. This is the second part of the command above, but can be run individually as the following:
```
source .venv/Scripts/activate
```

## Running the project
### Running the GUI (Graphical User Interface)
First dependent packages have been installed as referenced in the section [Project Setup](#project-setup). The Controller GUI creates an interactive module that removes the need for all users to have a compatible Leap Motion Controller. Future iterations of this project could allow for a live connection to a Leap Motion Controller for dynamic flight control without the GUI. To run the gui you can run the entire project with the following command from the root of the project directory:
```
python src/controller_gui.py
```
This command assumes you have a Tello drone connected and ready to receive commands evaluated by our computer vision model. If you do not have a drone, the controller can be run with an additional DRYRUN flag. This flag allows for the same model evalutations, but does not require an active Tello drone connection and simply prints the actions it would have taken to the console. An example is below:
```
DRYRUN=True python src/controller_gui.py
```

### Utility Scripts
#### Archive Flattener
The Archive Flattener script is designed to consolidate the LMC data orginally obtained from [LMC Kaggle](https://www.kaggle.com/datasets/gti-upm/leaphandgestuav). The original data is split into subjects first and then further split by gesture, images/sequence, and finally test and train data. This script consolidates this down to a flattened structure of only gesture. This way future testing training of our model can be done in unique and randomizable manners.
The script can be ran with the following command from the utils directory:
```
python archive_flattener.py
```
#### Metadata Generator
The Metadata Generator script reads through the flattened data to programmatically inspect the files we will be using to train our model. It creates a simple json file that contains some high level information such as total file count for each gesture as well as a collection and count of all present file types. This data helps illustrate the quality of data we are using, and the file size counts in particular helps show how much work will need to take place to standardize our data. The script can be ran with the following command from the utils directory:
```
python metadata_generator.py
```

### Drone Flight

#### Controller
TBD