This is a wigglegif photobooth!  

A wigglegif is a 3D gif made from an array of cameras, much like an old school stereoscopic photo, but wiggly.  


Dependencies:

Python 2.7
numpy
pillow
At least two cameras hacked with CHDK <link here>
An installation of ptpcam that's on your path as "ptpcam"
images2gif.py


I'll elaborate on those last three since they may not be straightforward:

I got my cameras with a pre-hacked firmware, so I can't comment on any bugs you may run into with that.  However, CHDK has an awesome and active community that probably has answers for whatever you may run into.  You will have to load some files onto the SD card and press some buttons in a specific order.  That sequence is *not* "up up down down left right left right B A start."

I used this version of ptpcam <link here> 

Be warned, ptpcam may be very picky about what version of libusb you have installed.  

And I ran into the issue where gphoto (the default linux photo driver) grabs the cameras and won't let you access their full functionality over ptp.  I fixed it by writing a udev rule and removing my model of camera from the udev/hwdb.  Instructions in this thread <link here>

images2gif.py is packaged here for convenenience, but this is the original <link here>

I modified it according to this stackoverflow thread, thanks y'all <link here>

Also, I run this on Xubuntu and haven't had a chance to test on any other OS's

Window's installation instructions: Don't try


How to run:

If the above dependencies are met, you should just be able to plug in your cameras, turn them on and run:

python path/to/wigglegif/__main__.py

I understand that is a pretty significant "if".  Lost me a whole weekend.  

Feel free to email me with any questions at sarah.anne.friend@gmail.com


To do:

Test this out on other distros.  
Upload a CAD model of the tripod mount we built, also photos
Probably a diagram of how to find the camera angle based on the focal distance between cameras/subject would be good too