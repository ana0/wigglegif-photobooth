import chdk
import time
import sys
import subprocess
import gifmaker
from app import create_app

def one_shot(devices, set_id):
    '''Takes a single photo from with all connected cameras.'''

    print("Deleting photos ...")
    chdk.delete_all(devices) # Will block until complete

    print("Shooting ...")
    chdk.chdk(devices, "lua press('shoot_half'); sleep(3000); press('shoot_full'); release('shoot_full'); release('shoot_half');")
    # Wait for this to run
    time.sleep(5.0) 

    print("Downloading photos ...")
    chdk.download_all(devices, set_id) # Will block until complete

def run():

    print("Super awesome interactive session!")
    
    devices = chdk.get_devices()

    print("%d devices found." % len(devices))

    if len(devices) < 1:
        print("No devices found.  Ctrl-C to exit ...")
        raw = raw_input()
        # model()
        sys.exit(1)

    # One-time camera-config
    configured = False
    while not configured:
        print("Let's set your camera rotation. \n Are the cameras mounted horiziontally, or vertically? \n"
            "Press h for horiziontally and v for vertically")
        raw = raw_input()
        if raw == "h":
            rotation = "horizontal"
            configured = True
        elif raw == "v":
            print("Do the tripod mounts face to the left, or the right? \n Press l for left and r for right.")
            raw = raw_input()
            if raw == "l":
                rotation = "clockwise"
                configured = True
            elif raw == "r":
                rotation = "counter-clockwise"
                configured = True
            else:
                print("Hmm, that doesn't seem to be one of the options")
        else:
            print("Hmm, that doesn't seem to be one of the options")
    
    print("Initializing ...")
    chdk.chdk(devices, "luar set_record(true)")
    # Wait for the lenses to extend 
    time.sleep(3.0)

    set_id = 0
    while True:
        # print("Press <enter> to capture more images, type m<enter> to model.")
        print("Press enter to make a gif")
        raw = raw_input()
        if raw == '':
            print("Delaying ...")
            time.sleep(10.0)
            one_shot(devices, set_id)
            gifmaker.make_gifs(devices, rotation, set_id)
        else:
            print("That won't work")
        set_id = set_id + 1


if __name__ == "__main__":
    run()
