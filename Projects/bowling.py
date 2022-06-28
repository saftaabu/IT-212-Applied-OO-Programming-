from framescore import frame_score
from load_list_of_lists import load_list_of_lists

filename = input("Enter file name: ")
frames = load_list_of_lists(filename)

#Init score to 0
score = 0

#set range to 11 to account for Frame0
for i in range(1, 11):
    print(score)
    if frames[i][0]==10 and frames[i+1][0]==10:
        next_ball_1 = 10
        next_ball_2 = frames[i+2][0]
    elif frames[i][0]==10 and frames[i+1][0]<10:
        next_ball_1 = frames[i+1][0]
        next_ball_2 = frames[i+1][1]
    elif frames[i][0]+frames[i][1]==10:
        next_ball_1 = frames[i+1][0]
        next_ball_2 = 0
    else:
        next_ball_1 = 0
        next_ball_2 = 0
        
    score += frame_score(frames[i], next_ball_1, next_ball_2)
    
print("Total Score:", score)
