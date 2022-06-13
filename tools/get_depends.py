
#!/bin/python

import sys
import yaml
from yaml.loader import SafeLoader
from typing import List

class Package:
    def __init__(self, file):
        with open(file, 'r') as stream:
            data = yaml.safe_load(stream)
            if "depends" not in data:
                return
            depends = data["depends"]
            result: List[str] = []
            for depend in depends:
                if "version" in depend:
                    result.append("{}={}".format(depend["name"], depend["version"]))
                else:
                    result.append("{}".format(depend["name"]))
            for r in result:
                print(r, end=" ")

if __name__ == '__main__':
    package: Package = Package(sys.argv[1])
