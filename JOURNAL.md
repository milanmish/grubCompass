---
title: "Grub Compass"
author: "Milan Mishra"
description: "I am designing a compass that ramdomly chooses a restaurant near you and points you to it, without letting you know where you're going"
created_at: "2025-05-22"
---

# May 22nd: Researching hardware

Today, I decided upon my project and started researching the hardware I'll need. I decided that I'm going to have two components: the compass and the dock. The dock will be built on a Raspberry Pi Zero 2 W and the compass will be on an ESP32. 

![Planning](img/IMG_6064.png)

**Total time spent: 1h**


# May 23rd: Script Building

I'm still waiting on some parts, so I started learning about the Google Places and Geolocation APIs. I built the basic script that the Raspberry PI on the docking device will need to run.

![!\[Code Screenshot\](image.png)](img/image.png)

**Total time spent: 1.5hrs**

# May 23rd: PCB Design Day 1

Today, I started designing my PCB in KiCAD. A lot of the time, I was just reading datasheets to understand what parts I'll need. Most of my focus was on the power system since I want my compass to work off battery as well as USB-C

![PCB_Day1](img/image-1.png)

**Total time spent: 4hrs**

# May 28th: PCB Design Day 2

I've been working more on the PCB design and have changed some choices around how I'm going to wire my sensors. I'll still have a seperate dock/compass, but the custom PCB for the compass won't have the GPS directly wired to it (I already have an Adafruit GPS, so I can save money). I'm still deciding if I want to wire the IMU as a seperate board or build it in.

I also changed some stuff in my power system. Instead of having a USB-C input on the compass, I'm going to have it charge from the dock on a three pin connector.

![PCB_Day2](img\image-2.png)

**Total time spend: 4.5hrs**

# June 6th: PCB Design Day 3

I've taken a bit of a break but I'm finishing up my custom PCB. I want to be able to use the ESP32 for other projects in the future so I but a bunch of headers for future projects. I'm also using headers for the power supply, servo, gps, and imu. I've also started designing the compass in Fusion.

![PCB_Day3](img\image-3.png)
![PCB_3D](img\image-4.png)