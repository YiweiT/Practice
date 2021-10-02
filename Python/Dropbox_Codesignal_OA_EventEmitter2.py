'''
Event Emitter2
param:
    events: [[eventID, startTimestamp, Interval],...]
    command: [["subscription"/"unsubscription", eventId, timestamp]]
    endTimeStamp: integer

You are given the above parameters. 
You need to count the number of notifications received of every event

For example:
event = [[1, 0, 5], [2, 0, 3]]
command = [["subscription", 1, 0], ["unsubscription", 1, 20], ["subscription", 2, 7]]
endTimestamp = 20
event_1: received notices = (20 - 0) // 5 = 4
event_2: received notices = (20 - 7) // 3 = 5 (ceilling)
'''
import math
def eventEmitter2(events, command, endTimestamp):
    # event_dict: {event_id: [(startTime, endTime, interval), ...]}
    # stack: [event_id, ...]
    # we will update the startTime or endTime of the last tuple in the event_dict for the given event
    # when a sub command received, a new tuple will be added to the given event in the dict
    event_dict = {}
    stack = []
    intervals = {}
    for id, start, interval in events:
        intervals[id] = interval
    
    # print(event_dict)
    # process command
    for com, id, time in command:
        if com == 'subscription':
            # if the last item in the stack is not current id
            # it means that we need to update time of the last tuple of the given id 
            # in event_dict
            interval = intervals[id]
            if id in event_dict:
                event_dict[id].append((time, endTimestamp, interval))
            else:
                event_dict[id] = [(time, endTimestamp, interval)]
            
                
        else:
            # command is unsubscription,
            # we need to update the end time of the last tuple
            start, end, interval = event_dict[id].pop()
            
            event_dict[id].append((start, time, interval))
            
    # calculate number of notifications received for every event
    res = []
    for id in event_dict:
        cnt = 0
        for start, end, interval in event_dict[id]:
            cnt += int(math.ceil((end - start) / interval))
        res.append("{}: {}".format(id, cnt))
                
    return res
    
# main
events = [[1, 0, 5], [2, 0, 3]]
command = [["subscription", 1, 0], ["unsubscription", 1, 20], ["subscription", 2, 7]]
endTimestamp = 20
print(eventEmitter2(events, command, endTimestamp))