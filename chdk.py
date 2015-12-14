import subprocess
import threading

def get_devices():
    '''Returns a list of (bus,device) tuples that can be used to uniquely
    identify a connected camera.'''
    output = subprocess.check_output(['ptpcam', '-l'])

    cameras = []
    in_list = False
    for line in output.strip().split("\n"):
        fields = line.split("\t")
        if fields[0] == 'bus/dev':
            # We're now in the camera list portion
            in_list = True
            continue
        if in_list: 
            (bus_string, dev_string) = fields[0].split("/")
            bus = int(bus_string)
            dev = int(dev_string)
            cameras = cameras + [(bus, dev)]

    # print cameras
    return cameras

def ptpcam(devices, args):
    '''Runs ptpcam with the given args for the given devices.
    Runs each call in its own thread, and then waits for the threads
    to complete before returning.
    Devices is a list of (bus, dev) pairs.
    Args is a list of arguments, e.g. ['-D']'''
            
    threads = [] 
    for (bus, dev) in devices:
        thread = threading.Thread(
            target=subprocess.call, 
            args=(['ptpcam', '--bus=%d' % bus, '--dev=%d' % dev] + args,),
            kwargs={"stdout": subprocess.PIPE}
        )
        threads = threads + [thread]

    # Start!
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    # TODO: a reasonable timeout that indicates an error
    for thread in threads:
        thread.join()

def chdk(devices, command):
    '''Runs ptpcam in CHDK mode with the given command for the given devices.
    Devices is a list of (bus, dev) pairs.
    command is a CHDK command, e.g. "luar shoot()"'''

    ptpcam(devices, ['--chdk=%s' % command]) # No quotes on command

def delete_all(devices):
    '''Delete all photos on the camera.
    Devices is a list of (bus, dev) pairs that the command should be sent to.'''
    for device in devices:
        print "Deleting from %d-%d" % (device[0], device[1])
        ptpcam([device], ['-D']) 

def download_all(devices, set_id=0):
    '''Download all photos on the camera.
    Devices is a list of (bus, dev) pairs that the command should be sent to.'''
    for device in devices:
        print "Downloading from %d-%d" % (device[0], device[1])
        ptpcam([device], ['-G'])
        subprocess.call("mv IMG_*.JPG %d-%d-%d.JPG" % (set_id, device[0], device[1]), shell=True)

# get_devices()