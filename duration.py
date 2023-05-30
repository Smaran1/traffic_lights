
def traffic_duration(looping_times,range_for_green, range_for_red):    
    for _ in range(looping_times):
        green_light = reversed(range(1, range_for_green))
        red_light = reversed(range(1, range_for_red))

        
        for g in green_light:
            print(g)
            if g == 1:
                print("STOP")
           

    
        for r in red_light:
            print(r)
            if r == 1:
                print("GO")


traffic_duration(2,61,121)
