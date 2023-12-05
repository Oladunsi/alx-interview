#!/usr/bin/python3
"""0-lockboxes is a task that determines if N number of boxes and each
   boxes contain keys to unlock other boxes 
"""

def canUnlockAll(boxes):
    """This function determins if all the boxes can be opened with the keys
    attached to the boxes

    Args:
        boxes (lists): collection of boxes 

    Returns:
        boolean: true if all boxes can be opened else false
    """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    canOpenBoxes = [0]
    for bunchkeys in canOpenBoxes:
        for indikey in boxes[bunchkeys]:
            if indikey not in canOpenBoxes and indikey < len(boxes)
                canOpenBoxes.append(indikey)
    if len(canOpenBoxes) == len(boxes)
        return True
    return False
