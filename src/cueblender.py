import bpy
from bpy import context
from ._vendor.obswebsocket import obsws, requests
from threading import Thread


# import asyncio
# from simpleobsws import obsws

# Constants
clip_type = 'MULTICAM'

class CueBlender:
    def __init__(self, host="localhost", port=4444, password=None):
#        self.obshost = host
#        self.obsport = port
#        self.obspass = password
        self.prevcam = None

        self.obs = obsws(host, port, password)
        self.obs.connect()
        
    def find_active_clip(self, clips, frame):
        for clip in clips:
            if clip.frame_final_start <= frame and clip.frame_final_end > frame:
                return clip
        
#        return [clip for clip in clips if(clip.frame_final_start <= frame and clip.frame_final_end > frame)][0]

    def get_multitrack_clips(self, clips):
        multi_clips = []
        for clip in clips:
            if clip.type == clip_type:
                multi_clips.append(clip)
        return multi_clips

    def get_active_multicam(self, scenectx=context.scene):
        sequences = scenectx.sequence_editor.sequences_all
        cueclips = self.get_multitrack_clips(sequences)
        try: 
            activecam = self.find_active_clip(cueclips, scenectx.frame_current).multicam_source
        except AttributeError:
            activecam = None
        return activecam

    def set_obs_scene(self, scenename):
        return self.obs.call(requests.SetCurrentScene(scenename))
        # return self.obs.call('SetCurrentScene', {"scene-name": scenename})

    def frame_event(self, scenectx=None, arg2=None):
        if scenectx is None:
            scenectx = context.scene
        
        camid = self.get_active_multicam(scenectx)
        if camid != self.prevcam:
            print(camid)
            self.prevcam = camid
            self.set_obs_scene(f"Cam {camid}")


cueb = CueBlender(password="pyRupKELm3LQKr7")

for x in bpy.app.handlers.frame_change_pre:
    try:
        if x.__name__ == 'frame_event':
            bpy.app.handlers.frame_change_pre.remove(x)
    except: pass

def frame_event_thread(scene, args): 
    Thread(target=cueb.frame_event, args=[scene, args]).start()

bpy.app.handlers.frame_change_pre.append(frame_event_thread)
print(bpy.app.handlers.frame_change_pre)