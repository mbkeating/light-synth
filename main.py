from Camera.CV2Camera import CV2Camera
from LightLocator.CVLightLocator import CVLightLocator
from LocationToNote.AScaleLocationToNote import AScaleLocationToNote
from Synth.SimpleSynth import SimpleSynth
import time

if __name__ == "__main__":
    print("Application Start")
    camera = CV2Camera()
    light_locator = CVLightLocator({'threshold': 100})
    location_to_note = AScaleLocationToNote()
    synth = SimpleSynth()
    print("Application Loaded")

    while True:
        frame = camera.get_frame()
        sources = light_locator.locate_sources(frame)
        notes = location_to_note.get_notes(sources)
        if notes:  
            synth.play(notes)
        
        time.sleep(0.1)