#!/bin/bash


echo "Installing dependencies for s2geometry"
sudo apt-get install libgflags-dev libgoogle-glog-dev libgtest-dev libssl-dev
sudo apt-get install swig
sudo apt-get install cmake

echo "Cloning latest repository for s2geometry"
git clone https://github.com/google/s2geometry.git


echo "Buiding s2geometry"
cd s2geometry
mkdir build
cd build
cmake -DWITH_GFLAGS=ON  -DPYTHON_EXECUTABLE=/usr/bin/python3 -WITH_GTEST=ON -DGTEST_ROOT=/usr/src/gtest ..
make

echo "Copying the executables to project S2lib directory"
cp python/pywraps2.py ../../../app/main/utils/S2Lib/pywraps2.py
cp python/_pywraps2.so ../../../app/main/utils/S2Lib/_pywraps2.so
cd ..
cd ..
cd ..

source venvtaxiapi/bin/activate/
cd ..
echo "run API server again by typing python runserver.py"
