
def job_classification(eyes, mouth, nose, glabella):

    eyes_size, eyes_tail, eyes_distance = eyes
    lips_length, lips_thickness, mouth_tail = mouth
    nose_length, nose_width = nose
    glabella_distance = glabella[0]

    eyes_score = 0
    mouth_score = 0
    nose_score = 0
    glabella_score = 0

    if 0 <= eyes_size + eyes_tail + eyes_distance <=3:
        eyes_score = 8
    else:
        eyes_score = 0

    
    if 0 <= lips_length + lips_thickness + mouth_tail <= 3:
        mouth_score = 4
    else:
        mouth_score = 0
   
    if 0 <= nose_length + nose_width <= 2:
        nose_score = 2
    else:
        nose_score = 0

    if 0 <= glabella_distance < 1:
        glabella_score = 1
    else:
        glabella_score = 0

    data  = eyes_score + mouth_score + nose_score + glabella_score
    
    return data