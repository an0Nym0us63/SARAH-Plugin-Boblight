#!/usr/bin/env python2
from lib import Boblight
import time
import ctypes
import os
import sys

# Settings
# will/should be replaced with command line options
boblightd_IP = str(sys.argv[2])
boblightd_PORT = int(sys.argv[3])
boblightd_PRIORITY = 128
curdir =os.path.dirname(os.path.abspath(__file__))
bob = Boblight()
bob.bob_loadLibBoblight(curdir+'/libboblight-win32.0.dll', 'win32')

connected = bob.bob_connect(boblightd_IP, boblightd_PORT)

def Color(r, g, b):
    rgb = (ctypes.c_int * 3)()
    rgb[0] = r
    rgb[1] = g
    rgb[2] = b
    return rgb

def demo_RGB():
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(255, 0, 0))
    time.sleep(1)

    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(0, 255, 0))
    time.sleep(1)

    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color( 0, 0, 255))
    time.sleep(1)

def rainbow():
    for i in range(0, 127):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(0,0,127+i))
        time.sleep(0.1)
    for i in range(0, 255):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(0,i,255-i))
        time.sleep(0.1)
    for i in range(0, 255):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(i,255-i,0))
        time.sleep(0.1)
    for i in range(0, 255):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(255-i,i,i))
        time.sleep(0.1)
    for i in range(0, 255):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(i,255,255-i))
        time.sleep(0.1)
    for i in range(0, 255):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(255,255-i,i))
        time.sleep(0.1)
    for i in range(0, 127):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(255-(i*2),0,255-i))
        time.sleep(0.1)

def police():
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(0, 0, 255))
    time.sleep(0.15)
    
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(255, 255, 255))
    time.sleep(0.15)
    
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color( 255, 0, 0))
    time.sleep(0.15)

def marseillaise():
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(0, 0, 255))
    time.sleep(2)
    
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(255, 255, 255))
    time.sleep(2)
    
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color( 255, 0, 0))
    time.sleep(2)

    width = 2;
    height = 20;
    bob.bob_setscanrange(width, height)
    for r in range(7):
        bob.bob_addpixelxy(r,0,Color(0,0 ,255))
        bob.bob_addpixelxy(r,1,Color(0,0 ,255))
        bob.bob_addpixelxy(19-r,0,Color(255,0 ,0))
        bob.bob_addpixelxy(19-r,1,Color(255,0 ,0))
        bob.bob_addpixelxy(7+r,0,Color(255,255 ,255))
        bob.bob_addpixelxy(7+r,1,Color(255,255 ,255))
    bob.bob_set_priority(128)
    bob.bob_sendrgb()
    time.sleep(3)

def strobe():
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(255, 255, 255))
    time.sleep(0.06)
    
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(0, 0, 0))
    time.sleep(0.04)

def k2000():
    width = 2;
    height = 20;
    bob.bob_setscanrange(width, height)
    for x in range(20):
        bob.bob_addpixelxy(x,0,Color(255,0 ,0))
        bob.bob_addpixelxy(x,1,Color(255,0 ,0))
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(0.04)
    for x in range(19):
        bob.bob_addpixelxy(19-x,0,Color(255,0 ,0))
        bob.bob_addpixelxy(19-x,1,Color(255,0 ,0))
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(0.04)

def feu():
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(255, 204, 51))
    time.sleep(0.05)
    bob.bob_set_static_color(Color(0, 0, 0))
    bob.bob_set_static_color(Color(255, 255, 51))
    time.sleep(0.02)
    bob.bob_set_static_color(Color(0, 0, 0))
    bob.bob_set_static_color(Color(255, 204, 51))
    time.sleep(0.02)
    bob.bob_set_static_color(Color(0, 0, 0))
    bob.bob_set_static_color(Color(255, 255, 51))
    time.sleep(0.04)
    bob.bob_set_static_color(Color(0, 0, 0))

def snake():
    width = 20;
    height = 30;
    bob.bob_setscanrange(width, height)
    for x in range(30):
        bob.bob_addpixelxy(x,0,Color(255,255 ,255))
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(0.04)
    for y in range(20):
        bob.bob_addpixelxy(29,y,Color(255,255 ,255))
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(0.04)
    for x in range(30):
        bob.bob_addpixelxy(29-x,19,Color(255,255 ,255))
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(0.04)
    for y in range(20):
        bob.bob_addpixelxy(0,19-y,Color(255,255 ,255))
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(0.04)

def orage():
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(0, 0, 128))
    time.sleep(8)
    bob.bob_set_static_color(Color(0, 0, 0))
    time.sleep(0.02)
    bob.bob_set_static_color(Color(255, 255, 255))
    time.sleep(0.04)

if not connected:
    exit()
if str(sys.argv[1])=='rainbow':
    for i in range(0, 127):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Color(0,0,i))
        time.sleep(0.1)
while True:
    if str(sys.argv[1])=='police':
        police()
    elif str(sys.argv[1])=='rgb':
        demo_RGB()
    elif str(sys.argv[1])=='rainbow':
        rainbow()
    elif str(sys.argv[1])=='marseillaise':
        marseillaise()
    elif str(sys.argv[1])=='strobe':
        strobe()
    elif str(sys.argv[1])=='k2000':
        k2000()
    elif str(sys.argv[1])=='feu':
        feu()
    elif str(sys.argv[1])=='snake':
        snake()
    elif str(sys.argv[1])=='orage':
        orage()
    else :
        exit()
exit()
