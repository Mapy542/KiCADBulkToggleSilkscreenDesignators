#!/bin/sh
set -eu

rm -rf build # remove old build directory
rm -f kicad-package.zip
mkdir -p build/resources build/plugins
cp metadata.json build
cp *.py icon.png icon-hide.png build/plugins
cp -r icon-64x64.png build/resources/icon.png
cd build && zip -r ../kicad-package.zip *