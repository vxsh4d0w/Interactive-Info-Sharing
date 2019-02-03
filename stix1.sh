#!/bin/sh
taxii-push --discovery https://infosharing.cybersaiyan.it:9000/services/discovery --dest community --username community --password changeme --content-file package.stix
