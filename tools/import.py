#!/bin/python

import os, sys
import shutil
import subprocess
import yaml
from yaml.loader import SafeLoader

class MetaData:
    base_url = ""
    name = ""
    version = ""
    rebuild = 1
    def __init__(self, json) -> None:
        self.base_url = json["base_url"]
        self.name = json["name"]
        self.version = json["version"]
        self.rebuild = json["rebuild"]

class Package:
    metadata: MetaData
    def __init__(self, file):
        with open(file, 'r') as stream:
            data = yaml.safe_load(stream)
            self.metadata = MetaData(data["metadata"])
    def buildPackage(self):
        subprocess.run(["dget -u {}/{}/{}_{}-{}.dsc".format(self.metadata.base_url, 
                                                         self.metadata.name,
                                                         self.metadata.name,
                                                         self.metadata.version,
                                                         self.metadata.rebuild)], 
                       cwd=os.path.abspath(sys.argv[1]), 
                       shell=True)

if __name__ == '__main__':
    package: Package = Package(sys.argv[2])
    package.buildPackage()
