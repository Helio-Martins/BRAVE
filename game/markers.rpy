init -10 python:
    import time
    import random
    from pylsl import StreamInfo, StreamOutlet

    info1 = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
    outlet1 = StreamOutlet(info1) 

    def send_marker(str_marker):
        global outlet1
        # sends to MARKER stream
        outlet1.push_sample([str_marker]) # 1 channel
        # wait for 1 second
        #time.sleep(1)