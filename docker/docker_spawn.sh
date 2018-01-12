#!/bin/bash
exec docker run -v $PWD/compile_run.sh:/compile_run.sh  -v $PWD/java_src_test:/java_src:ro openjdk bash compile_run.sh