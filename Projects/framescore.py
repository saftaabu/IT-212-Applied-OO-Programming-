def frame_score(the_frame, next_ball_1, next_ball_2):

    # Case where frame is a strike
    if the_frame[0] == 10:
        return 10 + next_ball_1 + next_ball_2
    
    # Case where frame is a spare
    elif the_frame[0] + the_frame[1] == 10:
        return 10 + next_ball_1

    # Case where frame is an open frame
    elif the_frame[0] + the_frame[1] < 10:
        return the_frame[0] + the_frame[1]

    


    
    
