#!/usr/bin/python3
"""Determining if all boxes in a list can be opened."""

def canUnlockAll(boxes):
    '''Check if all boxes in a list can be opened.'''
    # Get the total number of boxes
    n = len(boxes)
    # keep track of boxes that have been seen
    seen_boxes = set([0])
    #keep track of boxes that have not been seen
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        # Pop a box index from the set of unseen boxes
        boxIdx = unseen_boxes.pop()
        # Skip invalid box indices
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        # Check if the box has not been seen
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    # 
    return n == len(seen_boxes)
