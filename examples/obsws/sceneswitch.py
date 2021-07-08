from obswebsocket import obsws, requests

obs = obsws(password='T*7hnb&Pm!$gn2')
obs.connect()

while True:
    scenes = obs.call(requests.GetSceneList()).getScenes()
    
    print("Available scenes:")
    scene_names = []
    for i, scene in enumerate(scenes):
        scene_names.append(scene['name'])
        print("{}. {}".format(i, scene['name']))
    
    target_scene = int(input("Choose scene number: "))
    obs.call(requests.SetCurrentScene(scene_names[target_scene]))