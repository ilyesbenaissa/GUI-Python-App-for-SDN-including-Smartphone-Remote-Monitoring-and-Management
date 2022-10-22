# Python-API-Implementation-on-SDN-with-Smartphone-Accessibility
To make a good understanding of the Software-Defined Network, we made this project and divided it into three dependent sections, starting by building network topology and setting the configuration for each device in the campus topology then by writing the Python API scripts and adding a GUI with Python's Tkinter to clarify the possibility of development on  network automation field. For a real use case of campus network control, we will end up using Ngrok  to grant external smartphone access for our network automation and management from anywhere  in the world through the internet.


### General Project Experiment Flow Chart
![Capture](https://user-images.githubusercontent.com/115791314/197318480-6731f4f1-d105-4519-8f59-7a056a64b742.PNG)

### Features
- Real case campus network typology set on Packet Tracer .
- Cross-platform: Possibility to run the GUI App from Python file "main.py".
- Open-source : it is free and you can add many network management scripts to the code.
- Simple, Friednly Use with ease of a DNA Center approach.
- Smartphone accessibility to Campus Network-Controller through forwarded HTTP port.

### Requirements
Install the following softwares from official website
- Cisco Packet Tracer Version 8.0 or above
- Python version 3.7 or above
- Ngrok latest version

### Libraries
Install required libraries using **pip** as follows:
- `$ pip install requests`
- `$ pip install prettytable`

### Notes:
 First you need to run Packet Tracer and allow External Network Access from **Menu > Preferences > Miscellaneous** then run **main.py** Python file to show the GUI window.
 Connect to Network Controller using the forwarded URL from Ngrok.
If you are not familiar with Ngrok its highly recommended to read the documentation through their official website: https://ngrok.com/docs



