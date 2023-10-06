#!/usr/bin/python3
"""0-lockboxes
"""

def canUnlockAll(boxes):
    """A .................

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
