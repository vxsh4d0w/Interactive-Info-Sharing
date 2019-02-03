# Interactive-Info-Sharing
This is a fork of Info-Sharing script (https://github.com/CyberSaiyanIT/InfoSharing/tree/master/CONTRIB/PRODUCER/scripts) 
with an interactive menu to create, push and poll your IoC.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

At first you need to solve all dependencies:

```
# cabby 
sudo pip install cabby

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

```

## Running the script

Once dowloaded this package you have just to run the script as showed here below:

```
sh# python infosharing.py

```

An interactive menu will be displayed:

```
Welcome to Cyber Saiyan Info-Sharing

Please choose the option you want to run:
1. Add new IoC
2. Push IoC Stix 1.2
3. Push IoC Stix 2
4. Poll InfoSharing Server

0. Quit

```

The first option requires you to single out main details as title, description author and source file of your IoC. Here below what will be displayed:

```
Insert Title Ioc:Title Example
Insert Decription:Test Script
Insert User Identity:V
Add IoC Source File:../test.txt
Stix File generation in progress....

Writing STIX 1.2 package: package.stix
Writing STIX 2 package: package.stix2
 >>  
 
```



