# Infrared Red Green (IRG)
Processing Tools for IRG photos v1.0.0

# What does this do
This package processes images captured on full spectrum camera with yellow filter. Photographs produced in this manner have three colour channels Infrared Red and Green as opposed to regular natural colour images with Red Green and Blue channels. IRG photos are considered more asthetically appealing when processed so that the Infrared channel is mapped to the Red channel. To make way for this the Red channel is moved to the Green channel and the Green channel to the Blue. Before the channels can be rearranged any Infrared component which as leaked into the other channels is subtracted. 

# Setup
Install python from https://www.python.org/downloads/

# How to use
You can use this script from the command line `python irg.py demo.jpg`

Additionally on windows you can convert photos by simply dragging supported file(s) onto `irg.py` in your file explorer

The output files will be saved in the same location as the input. The filename will be prepended with `out-`

# Example
Input:

![demo](./docs/demo.jpg)

Output:

![demo](./docs/out-demo.jpg)

Whitebalanced in photoshop:

![demo](./docs/out-demo-balanced.jpg)

