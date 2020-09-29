#!/bin/sh

cd rpi_ws281x/
sudo scons

cd python

sudo python3 setup.py build
sudo python3 setup.py install

cd examples
sed -i -e 's/rpi_ws281x/neopixel/g' strandtest.py

cd ..
cd ..
cd ..
