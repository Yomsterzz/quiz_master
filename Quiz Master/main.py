import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

question_box = Rect(0,0,650,150)
marquee_box = Rect(0,0,880,80)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)

score = 0
time_left = 10
question_file = "questions.txt"
marquee_msg = ""
is_game_over = False
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_msg
    screen.clear()
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "blue")
    screen.draw.filled_rect(skip_box, "green")

    for answerbox in answer_boxes:
        screen.draw.filled_rect(answerbox, "orange")
    
    marquee_msg = "Welcome to the quiz game!"
    marquee_msg = marquee_msg + " Question {} of {}".format(question_index, question_count)
    screen.draw.textbox(marquee_msg, marquee_box, color="white")
    screen.draw.textbox("SKIP", skip_box, color="white", shadow=(0.5,0.5), scolor="dim grey", angle=-90)
    screen.draw.textbox(str(time_left), timer_box, color="white", shadow=(0.5,0.5), scolor="dim grey")
    
    index = 1
    for box in answer_boxes:
        #screen.draw.textbox(questions[index].stripe(), box, color="white", shadow=(0.5,0.5), scolor="dim grey")
        index += 1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x = marquee_box.x-2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH





pgzrun.go()