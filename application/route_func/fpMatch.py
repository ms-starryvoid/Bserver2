import cv2
import numpy as np
def fingerprint_segment(desc1,desc2,kp1l,kp2l):
    
    #kp_s2 = np.array_split(kp2, num_segments)
    #desc_s2 = np.array_split(desc2, num_segments)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=10)
    search_params = dict(checks=50)
    
    # FLANN matcher
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(desc1, desc2, k=2)
    
    # Ratio test as per Lowe's paper
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    
    # Calculate the similarity score
    score = len(good_matches) / max(kp1l,kp2l) * 100
    return score
