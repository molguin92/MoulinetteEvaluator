#!/bin/bash
echo_stderr ()
{
    echo "$@" >&2
}


SRC_DIR="/java_src"
BUILD_DIR="/java_build"
if [ -d "$SRC_DIR" ]; then
    cd "$SRC_DIR"
    mkdir "$BUILD_DIR"
    cp *.java "$BUILD_DIR/"
    cd "$BUILD_DIR"
    javac *.java
    java Main
else
    echo_stderr "$SRC_DIR not found."
    exit -1
fi