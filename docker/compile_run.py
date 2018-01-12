#!/bin/python2.7

# Script for compiling and running Java code inside a docker container.
# This script is to be run inside the docker container (for instance,
# using "docker run"). It expects to find a file "/build.json" with the
# necessary instructions for finding the source files and storing the results.

# build.json example:
#   {
#       "src_dir": "/java_src",
#       "main_class": "HelloWorld",
#       "javac_flags": null,
#       "output_dir": "/results"
#   }

def java_compile():
    pass

def java_run():
    pass

def parse_buildjson():
    pass

if __name__ == "__main__":
    pass
