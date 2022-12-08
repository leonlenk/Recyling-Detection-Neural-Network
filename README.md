# Recyling-Detection-Nueral-Network
 
##Credits: 
The Sandia High School 2021 Stem Challenge Team 

##The Problem:
In America most recycling is thrown away and even when people do recycle often the rules are opaque which leads to trash getting thrown in with actual recyclable goods. When trash (particularly things like pizza boxes and plastic bags) get thrown in with recycling they need to be manually picked out by dozens of workers because it can clog up and damage recycling machines, additionally trash in recycling can often pollute other materials thus forcing large batches of otherwise recyclable material to be thrown out. Furthermore modern sorting methods can lead to inefficiencies and prevent recycling from being recycled –for example crumpled aluminum cans are often sorted incorrectly. All of this together has stunted the growth of recycling in America and keeps the vital industry difficult and often unprofitable. 

##Our Solution:
We created a program (in python) that downgrades images to monochrome and resizes them to 64x64 pixels which it feeds through a pytorch convolutional neural network and outputs whether it thinks it sees trash or recycling with 86% accuracy (the model only achieves this accuracy in a clean background environment due to limitations in time and computational power). This is intended to be implemented on low quality cameras in recycling cans which will redirect trash and only let through recycling, alleviating some of the responsibility of the consumer and reducing the manpower necessary at a recycling plant. Granted that due to not 100% accuracy humans would be needed somewhere down the line to make the ultimate decision on what is recycling, but this is a start.

