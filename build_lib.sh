#!/bin/sh

echo "run as root"

cd rpi_ws281x/
scons

cd python

python3 setup.py build
python3 setup.py install

cd examples
sed -i -e 's/rpi_ws281x/neopixel/g' strandtest.py

cd ..
cd ..
cd ..
