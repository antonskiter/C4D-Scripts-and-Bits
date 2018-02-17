import c4d
from c4d import documents, plugins, gui
#Welcome to the world of Python

def main():
    pass
    # define some value for the key
    valueIn = 1
    valueOut = 0
#    targetframe = 11 # specific frame
    offset = 20 # offset in frames
    
    #define FPS
    fps = float(doc.GetFps()) #Gets the doc frames
    print fps
        
    #define the time
#    keyTime = c4d.BaseTime(targetframe, fps)
    #keyTime = doc.GetTime()
    #print c4d.BaseTime.Get(doc.GetTime())
    tme = doc.GetTime()
    startTime = c4d.BaseTime(offset*-1/fps+tme.Get())
    endTime = c4d.BaseTime(offset/fps+tme.Get())
    
    keyTime = startTime
    
    # get the active object to add some keys
    activeObject = doc.GetActiveObject()
        
    if activeObject != None:
        
        #looking for tracks
        
        #track 1
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "1 Path <-> Proxy":
                break
            track = track.GetNext()
        tr1 = track
        print tr1
        
        #track 2
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "2 Path <-> Proxy":
                break
            track = track.GetNext()
        tr2 = track
        print tr2             
        
        #track 3
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "3 Path <-> Proxy":
                break
            track = track.GetNext()
        tr3 = track
        print tr3             
                
        #track 4
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "4 Path <-> Proxy":
                break
            track = track.GetNext()
        tr4 = track
        print tr4            
                
        #track 5
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "5 Path <-> Proxy":
                break
            track = track.GetNext()
        tr5 = track
        print tr5             
                
        #track 6
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "6 Path <-> Proxy":
                break
            track = track.GetNext()
        tr6 = track
        print tr6             
                
        #track 7
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "7 Path <-> Proxy":
                break
            track = track.GetNext()
        tr7 = track
        print tr7             
                
        #track 8
        track = activeObject.GetFirstCTrack()
        while track:
            if track.GetName() == "8 Path <-> Proxy":
                break
            track = track.GetNext()
        tr8 = track
        print tr8             
                
        # set keys forward
        curve = tr1.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr2.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr3.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr4.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr5.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr6.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr7.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)

        curve = tr8.GetCurve()
        added = curve.AddKey(keyTime)                            
        if added != None:
            key = added["key"]
            key.SetValue(curve,valueIn)


    keyTime = endTime
    print keyTime
    print valueOut
    
    # set keys
    curve = tr1.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr2.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr3.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr4.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr5.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr6.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr7.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)

    curve = tr8.GetCurve()
    added = curve.AddKey(keyTime)                            
    if added != None:
        key = added["key"]
        key.SetValue(curve,valueOut)


if __name__=='__main__':
    main()
    c4d.EventAdd()