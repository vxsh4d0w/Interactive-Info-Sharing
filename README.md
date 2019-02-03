# Interactive-Info-Sharing
This is a fork of Info-Sharing script (https://github.com/CyberSaiyanIT/InfoSharing/tree/master/CONTRIB/PRODUCER/scripts) 
with an interactive menu to create, push and poll your IoC.

At first you need to solve all dependencies:

# cabby 
sudo pip install cabby

mkdir src
cd src/

# python-cybox
git clone https://github.com/CybOXProject/python-cybox.git
cd python-cybox/
sudo python setup.py install


# python-stix
git clone https://github.com/STIXProject/python-stix.git
cd python-stix
sudo python setup.py install 

# stix
sudo pip install stix #already installed with cabby. But in case of issue.....
sudo pip install stix2

# validators
sudo pip install validators


