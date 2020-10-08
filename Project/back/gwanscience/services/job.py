import random 

def job_classification(eyes, mouth, nose, glabella):

    eyes_size, eyes_tail, eyes_distance = eyes
    lips_length, lips_thickness, mouth_tail = mouth
    nose_length, nose_width = nose
    glabella_distance = glabella[0]

    eyes_score = 0
    mouth_score = 0
    nose_score = 0
    glabella_score = 0
    
    if eyes_size == 1:
        eyes_size = random.randrange(0,3)
    if eyes_tail == 1:
        eyes_tail = random.randrange(0,3)
    if eyes_distance == 1:
        eyes_distance = random.randrange(0,3)
    if lips_length == 1:
        lips_length = random.randrange(0,3)
    if lips_thickness == 1:
        lips_thickness = random.randrange(0,3)
    if mouth_tail == 1:
        mouth_tail = random.randrange(0,3)
    if nose_length == 1:
        nose_length = random.randrange(0,3)
    if nose_width == 1:
        nose_width = random.randrange(0,3)
    if glabella == 1:
        glabella = random.randrange(0,3)

    if (2-eyes_size) + (2-eyes_tail) + (2-eyes_distance) >= 4:
        eyes_score = 8
    else:
        eyes_score = 0

    
    if (2-lips_length) + lips_thickness + mouth_tail >= 3:
        mouth_score = 4
    else:
        mouth_score = 0
   
    if nose_length + (2-nose_width) >= 2:
        nose_score = 2
    else:
        nose_score = 0

    if 2 - glabella_distance >= 1:
        glabella_score = 1
    else:
        glabella_score = 0

    data  = eyes_score + mouth_score + nose_score + glabella_score
    
    return data

def job_classification2(eyes, mouth, nose, glabella):

    eyes_size, eyes_tail, eyes_distance = eyes
    lips_length, lips_thickness, mouth_tail = mouth
    nose_length, nose_width = nose
    glabella_distance = glabella[0]

    eyes_score = 0
    mouth_score = 0
    nose_score = 0
    glabella_score = 0


    if (2-eyes_size) + (2-eyes_tail) + (2-eyes_distance) >= 4:
        eyes_score = 8
    else:
        eyes_score = 0
    
    if (2-lips_length) + lips_thickness + mouth_tail >= 3:
        mouth_score = 4
    else:
        mouth_score = 0
   
    if nose_length + (2-nose_width) >= 2:
        nose_score = 2
    else:
        nose_score = 0

    if 2 - glabella_distance >= 1:
        glabella_score = 1
    else:
        glabella_score = 0

    data  = eyes_score + mouth_score + nose_score + glabella_score
    
    return data