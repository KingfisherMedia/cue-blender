import bpy
from bpy import context

# Constants
clip_type = 'MULTICAM'

def find_active_clip(clips, frame):
    for clip in clips:
        if clip.frame_final_start <= frame and clip.frame_final_end > frame:
            return clip

def get_multitrack_clips(clips):
    multi_clips = []
    for clip in clips_raw:
        if clip.type == clip_type:
            multi_clips.append(clip)
    return multi_clips

def frame_event(scene, data):
    clips_raw = context.sequences
    

    print(find_active_clip(kbcue_clips, context.scene.frame_current).multicam_source)
    
bpy.app.handlers.frame_change_pre.append(frame_event)
