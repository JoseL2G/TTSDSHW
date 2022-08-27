# Joseluis G.,CIS 345, 10:30 T Th, Project Final
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from difflib import get_close_matches
import random
import json

# Global list is used to store all Question objects from question pool
question_master_list = []
# Global Game list used when playing quiz game, stores 3 random questions from question pool
game_list = []
# Counter used for game questions as index
game_counter = 0
# Point earned
points_earned = 0
# Points total
points_total = 0

class Question:
    """Question class: contruct a question object with question id, question text, correct answer, incorrect feedback
    correct feedback, points, choice_list"""

    def __init__(self, question_id, question_text, correct_ans, incorrect_msg, correct_msg, points, choices):
        self.__question_id = question_id
        self.__question_text = question_text
        self.__correct_answer = correct_ans
        self.__incorrect_message = incorrect_msg
        self.__correct_message = correct_msg
        self.__points = points
        self.__choices = choices  # Choices is a list of options from question pool

    # Property takes id, removes leading zeros, converts back to string with out any zeros
    @property
    def question_id(self):
        question_id_num = self.__question_id
        question_id_num = int(question_id_num)
        question_id_num = str(question_id_num)
        return question_id_num

    # setter is typically automated to protect integrity of json list and functionality of program,
    @question_id.setter
    def question_id(self, number=0):
        id_setter = str(number)
        self.__question_id = id_setter

    # capitalized first letter for grammar purposes
    @property
    def question_text(self):
        text = self.__question_text
        return text.capitalize()

    # Setter is used in editing/adding question, stips edges of blank spaces
    @question_text.setter
    def question_text(self, q_text=''):
        new_text = q_text.strip()
        self.__question_text = new_text

    # Correct answer property to distinguish from choices
    @property
    def correct_choice(self):
        return self.__correct_answer

    # setter capitalizes and strips the correct answer, assigns to appropriate
    @correct_choice.setter
    def correct_choice(self, c_choice=''):
        ans = c_choice.capitalize().strip()
        self.__correct_answer = ans

    # Incorrect message setter and properties
    @property
    def wrong_message(self):
        return self.__incorrect_message

    # Setter capitalizes and strips blank spaces, used in editing/creation
    @wrong_message.setter
    def wrong_message(self, w_msg=''):
        msg = w_msg.capitalize().strip()
        self.__incorrect_message = msg

    # Correct message property and setter
    @property
    def correct_message(self):
        return self.__correct_message

    # Setter capitalizes and strips blank spaces, used in editing/creation
    @correct_message.setter
    def correct_message(self, c_msg=''):
        msg = c_msg.capitalize().strip()
        self.__correct_message = msg

    # Points property and setter
    # Takes class string points, converts to string, returns integer
    @property
    def point_value(self):
        points = int(self.__points)
        return points

    # setter takes value and ensures it is converted to string
    @point_value.setter
    def point_value(self, p_value=''):
        points = str(p_value)
        self.__points = p_value

    # Choices properties, choices is a list of wrong options
    @property
    def choice_list(self):
        return self.__choices

    # Setter will take 3 text objects, any which one cannot be the same as the answer
    @choice_list.setter
    def choice_list(self, c_list=None):
        choices = c_list
        self.__choices = choices

    # formatter for when printing question text
    # need to change string format to use properties instead of instance variables
    def __str__(self):
        dictionary_entry = {str(self.__question_id): {'text': self.__question_text, 'answer': self.__correct_answer,
                                                      'wrong': self.__incorrect_message, 'correct': self.__correct_message,
                                                      'choices': self.__choices}}
        return f'{dictionary_entry}'


    '''def randomize_order(self, question_list=[]):
        pass'''


# Uses unique names for: quiz game, edit, go back, delete, create, next,
# Handler primarily used for new frames,
def event_handler(direction, frame, master_win, new_list=None, choice=None, disable_button=None, feedback_box=None):
    global question_master_list, game_counter, game_list, points_earned, points_total
    print(type(direction), direction)

    # Structures similar to "switch" case
    # First if statement checks if counter reached limit, if it does, the game ends and results are shown on new frame

    # main menu frame
    if direction.casefold() == 'quiz':
        frame.grid_forget()
        get_quiz_questions()
        quiz_game(master_win)

    # main menu frame
    if direction.casefold() == 'edit':
        frame.grid_forget()
        edit_questions(master_win)

    # Edit Frame
    if direction.casefold() == 'new':
        frame.grid_forget()
        new_question(master_win)

    # Edit Sub Frame
    if direction.casefold() == 'create':
        new_question_list = []

        for i in range(0, 5):
            text_get = new_list[i].get()
            new_question_list.append(text_get)
        print(new_question_list)

        choices_list = (new_list[5].get(), new_list[6].get(), new_list[7].get())
        print(choices_list)
        q = None

        # Creates Question object and appends object to master list
        # list index meanings: 0 = text, 1 = correct choice, 2=correct msg, 3=wrong msg, 4=point value, list = options
        q = Question(len(question_master_list) + 1, new_question_list[0], new_question_list[1], new_question_list[2],
                     new_question_list[3], new_question_list[4], choices_list)

        question_master_list.append(q)
        messagebox.showinfo(title='New Question', message='New question created successfully!')
        frame.grid_forget()
        frame.destroy()
        new_question(master_win)

    # Submit is used with quiz_game frame when user decides on answer
    if direction.casefold() == 'submit':
        print(type(choice), choice)
        disable_button.config(state=DISABLED)

        if choice == game_list[game_counter].correct_choice:
            feedback_box.config(text=game_list[game_counter].correct_message)
            points_earned += game_list[game_counter].point_value
        else:
            feedback_box.config(text=game_list[game_counter].wrong_message)
            # w_msg = Label(frame, text=game_list[0].wrong_message).grid(row=7, column=0)
        next_button = Button(frame, text='Next Question', command=lambda: event_handler('game_next', frame, master_win,
                                                                                        disable_button=next_button,
                                                                                        feedback_box=feedback_box))
        points_total += game_list[game_counter].point_value
        next_button.grid(row=6, column=3, pady=2)

    # Next button for the quiz game, configs entry boxes to details of next question in game_list
    if direction.casefold() == 'game_next':
        if game_counter == 2:
            frame.grid_forget()
            game_counter = 0
            end_game(master_win)
        else:
            game_counter += 1
            disable_button.grid_forget()
            feedback_box.config(text='No Answer')
            generate_next_question(frame, master_win)

    # Search button event, located on "Edit" Frame, brings up search frame in master window
    if direction.casefold() == 'search':
        frame.grid_forget()
        search_questions(master_win)

    # Edit/delete frame
    if direction.casefold() == 'edit/del':
        frame.grid_forget()
        edit_del(master_win)

    # Single_search, sub event of edit/del
    if direction.casefold() == 'single_search':
        try:
            string_list = new_list
            q_id = choice.get()
            q_id = int(q_id) - 1

            focus_question = question_master_list[q_id]
        except IndexError:
            messagebox.showinfo(title='Error!', message='Entry not valid/not found! Please try another ID')
        except ValueError:
            messagebox.showinfo(title='Error!', message='Entry is not an appropriate ID! please enter valid format'
                                                        '\ne.i: (1) or (0001)')
        except:
            print('error has occured')
            sys.exc_info()[0]

        try:
            # text_string
            string_list[0].set(focus_question.question_text)
            string_list[1].set(focus_question.correct_choice)
            string_list[2].set(focus_question.wrong_message)
            string_list[3].set(focus_question.correct_message)
            string_list[4].set(focus_question.point_value)

            # Getting list of wrong answers
            wrong_list = focus_question.choice_list
            string_list[5].set(wrong_list[0])
            string_list[6].set(wrong_list[1])
            string_list[7].set(wrong_list[2])
        except UnboundLocalError:
            print('Unbound error: passing')
            pass

    #change_question, sub event of edit/del menu
    if direction.casefold() == 'change_question':
        try:
            string_list = new_list
            q_id = choice.get()
            q_id = int(q_id) - 1
            focus_question = question_master_list[q_id]
        except IndexError:
            messagebox.showinfo(title='Error!', message='Entry not valid/not found! Please try another ID')
        except ValueError:
            messagebox.showinfo(title='Error!', message='Entry is not an appropriate ID! please enter valid format'
                                                        '\ne.i: (1) or (0001)')
        try:
            # text_string
            focus_question.question_text = string_list[0].get()
            focus_question.correct_choice = string_list[1].get()
            focus_question.wrong_message = string_list[2].get()
            focus_question.correct_message = string_list[3].get()
            focus_question.point_value = string_list[4].get()

            # Getting list of wrong answers
            wrong_list = (string_list[5].get(), string_list[6].get(), string_list[7].get())
            focus_question.choice_list = wrong_list
            print('question changed')
            save_questions()
        except UnboundLocalError:
            print('Unbound error: passing')
            pass

    # Generates Listbox and grids it on frame "search_frame"
    # Generates questions from question_pool 'text' sub keys, modifies to have simplier {ID:Text} structure to search
    # Cutoff is at 20% match and shows top 5
    # 20% match still brings some unrelated results, but it does bring intended result
    if direction.casefold() == 'show_results':
        search_text = choice.get()
        print(search_text)
        question_list = load_questions()
        simplified_question_list = {}
        listbox_items = {}

        for k in question_list:
            print(k)
            simplified_question_list[k] = question_list[k]['text']

        print(simplified_question_list)
        search_results = get_close_matches(search_text, simplified_question_list.values(), n=5, cutoff=0.1)
        print(search_results)

        # No results error pops up
        if len(search_results) == 0:
            messagebox.showinfo(title='Error', message='No results found!')

        result_list_box = Listbox(frame, width=60)
        result_list_box.grid(row=3, column=1, columnspan=3)

        # Loop used to find and return search list containing unique ID and question text
        counter = 0
        flag = None
        for k, v in simplified_question_list.items():
            flag = True
            while flag:
                if counter == len(search_results):
                    counter = 0
                    flag = False
                    continue
                elif search_results[counter] == v:
                    counter = 0
                    print(k, v)
                    result_list_box.insert(END, f'{k, v}')
                    flag = False
                else:
                    counter += 1
        result_list_box.insert(END, 'Use the Unique ID to find question in the edit/delete menu!')



    # Displays on most frames
    if direction.casefold() == 'back':
        frame.grid_forget()
        main_menu(master_win)

    pass


# function used to pick 3 random questions from question pool
def get_quiz_questions():
    global game_list, question_master_list
    temp_list = []
    game_list = []
    # for loop gets 3 unique
    while len(temp_list) < 3:
        ran = random.randint(0, (len(question_master_list) - 1))
        if ran not in temp_list:
            temp_list.append(ran)
    for n in temp_list:
        game_list.append(question_master_list[n])
    print(game_list)


# creates the master window, it is the only window that is used/created, other windows are message boxes with info
def master_window():
    quiz_window = Tk()
    quiz_window.geometry('600x600')
    quiz_window.title('Mental Anguish')
    quiz_window.config(background='gray')
    quiz_list = {'0001': {'text': '', }}
    return quiz_window


# creates main menu frame with run quiz and edit buttons
def main_menu(window):
    menu_frame = Frame(window, bg='blue', width=600, height=600, borderwidth=5, relief=SUNKEN)
    menu_frame.grid(row=0, column=0, columnspan=5)
    menu_frame.pack_propagate(0)
    Label(menu_frame, text='Welcome to Mental Anguish!', font='Arabic 12 bold', bg='blue').pack()
    Label(menu_frame, text='', bg='blue').pack()
    Label(menu_frame, text='', bg='blue').pack()
    quiz_button = Button(menu_frame, font='Arabic 12 bold', textvariable='Quiz', text='Run Quiz', width=12, command=lambda: event_handler('quiz', menu_frame, window))
    quiz_button.pack(anchor=S)
    edit_button = Button(menu_frame, font='Arabic 12 bold', textvariable='Edit', text='Edit Questions', width=12, command=lambda: event_handler('edit', menu_frame, window))
    edit_button.pack(anchor=S)


# Generates next question by loading new frame
def generate_next_question(frame, master_win):
    frame.grid_forget()
    quiz_game(master_win)


# Display on main
def quiz_game(window):
    global question_master_list, game_counter, game_list
    # Quiz frame to hold game
    quiz_frame = Frame(window, bg='sky blue', width=600, height=600, borderwidth=5, relief=SUNKEN)
    quiz_frame.grid(row=0, column=1, columnspan=5, sticky=E)
    quiz_frame.grid_propagate(0)
    # back button
    back_button = Button(quiz_frame, text='Go Back to Main', command=lambda: event_handler('back', quiz_frame, window))
    back_button.grid(row=0, column=0)
    # question label and text, derived from master list
    question_label = Label(quiz_frame, text=f'Question {game_counter + 1}/3:').grid(row=1, column=0)
    question_text = Label(quiz_frame, text=game_list[game_counter].question_text).grid(row=1, column=1, columnspan=2)
    # point text to show point value of question
    point_text = Label(quiz_frame, text=f'Points worth: {game_list[game_counter].point_value}').grid(row=0, column=1, padx=2)
    # Tracker label to show how many points are earned so far
    # tracker = Label(quiz_frame, text=f'')
    # choice 1 is the answer, a randomizer will be implemented later on
    num = IntVar()
    num.set(None)
    # Choice selected button with intvar
    num = IntVar()
    num.set(-1) # -1 is default when there is no answer selected
    # Wrong options buttons created and gridded
    answer_choices = randomize_answers()
    choice1 = Radiobutton(quiz_frame, variable=num, value=0, text=answer_choices[0], command=lambda: show_choice(answer_choices[0], selected_choice))
    choice1.grid(row=2, column=1)
    # other_choices_list = game_list[0].choice_list
    choice2 = Radiobutton(quiz_frame, variable=num, value=1, text=answer_choices[1], command=lambda: show_choice(answer_choices[1], selected_choice))
    choice2.grid(row=3, column=1)
    choice3 = Radiobutton(quiz_frame, variable=num, value=2, text=answer_choices[2], command=lambda: show_choice(answer_choices[2], selected_choice))
    choice3.grid(row=4, column=1)
    choice4 = Radiobutton(quiz_frame, variable=num, value=3, text=answer_choices[3], command=lambda: show_choice(answer_choices[3], selected_choice))
    choice4.grid(row=5, column=1)
    selected_choice = Label(quiz_frame, text='No Answer', bg='blue')
    selected_choice.grid(row=6, column=1)
    feedback_message_box = Label(quiz_frame, text='', bg='sky blue')
    feedback_message_box.grid(row=7, column=0, columnspan=2)
    print(num.get())
    # Submit button
    submit_button = Button(quiz_frame, text='Submit', command=lambda: event_handler('submit', quiz_frame, window,
                                                                                    choice=selected_choice.cget('text'),
                                                                                    disable_button=submit_button,
                                                                                    feedback_box=feedback_message_box))
    submit_button.grid(row=6, column=2, sticky=N)


# End game function called when last question is answered
def end_game(master_win):
    global game_list, points_total, points_earned
    end_frame = Frame(master_win,  bg='blue', width=600, height=600, borderwidth=5, relief=SUNKEN)
    end_frame.grid(row=0, column=1, columnspan=5, sticky=E)
    end_frame.pack_propagate(0)
    back_button = Button(end_frame, text='Go to Main menu', command=lambda: event_handler('back', end_frame, master_win))
    back_button.pack(anchor=NW)
    end_text = Label(end_frame, text='You have finished the quiz game! Here are your results:', font='Arabic 11 bold', bg='light blue').pack(anchor=N, pady=2)
    question1 = Label(end_frame, text=game_list[0].question_text).pack()
    question2 = Label(end_frame, text=game_list[1].question_text).pack()
    question3 = Label(end_frame, text=game_list[2].question_text).pack()
    points_scored = Label(end_frame, text=f'Points Earned: {points_earned} out of {points_total}').pack(anchor=W)
    # resets points earned and total
    points_earned = 0
    points_total = 0



# function used to print choice for user to see what choice is being selected, prints choice on 'selected_choice' label
# takes IntVar num and Label selected_choice
# show_choice used here instead of event handler since this is more of a accessibility/feature than an event occurring
# Also used as a debug feature to see what choice is being passed through event handler when submit is pressed
def show_choice(choice, label):
    label.config(text=choice)
    print(f'from function {choice}')


# function used to randomize answers, returns list of answers
def randomize_answers():
    global game_list, game_counter
    temp_list = []
    rand_list = []
    wrong_list = game_list[game_counter].choice_list
    while len(rand_list) < 4:
        r = random.randint(0, 3)
        if r not in rand_list:
            rand_list.append(r)
    for n in rand_list:
        if n == 0:
            temp_list.append(game_list[game_counter].correct_choice)
        else:
            temp_list.append(wrong_list[n - 1])
    return temp_list


# Frame that prompts user to enter details of a new question
# Unique ID is automatically assigned as to allow better tracking and functionality of the quiz
def new_question(window):
    global question_master_list
    id = str(len(question_master_list) + 1)
    new_frame = Frame(window, bg='sky blue', width=600, height=600, borderwidth=5, relief=SUNKEN)
    new_frame.grid(row=0, column=1, columnspan=5, sticky=E)
    new_frame.grid_propagate(0)
    back_button = Button(new_frame, text='Go Back', command=lambda: event_handler('back', new_frame, window))
    back_button.grid(row=0, column=0, )
    id_label = Label(new_frame, text=id).grid(row=0, column=1)
    text_label = Label(new_frame, text='Question').grid(row=1, column=0)
    text_entry = Entry(new_frame)
    text_entry.grid(row=1, column=1)
    c_ans_label = Label(new_frame, text='Correct answer').grid(row=2, column=0)
    c_ans_entry = Entry(new_frame)
    c_ans_entry.grid(row=2, column=1)
    wrong_msg_label = Label(new_frame, text='Message for Wrong Answer').grid(row=3, column=0)
    wrong_msg_entry = Entry(new_frame)
    wrong_msg_entry.grid(row=3, column=1)
    correct_msg_label = Label(new_frame, text='Message for Correct Answer').grid(row=4, column=0)
    correct_msg_entry = Entry(new_frame)
    correct_msg_entry.grid(row=4, column=1)
    points_msg_label = Label(new_frame, text='Number of Points').grid(row=5, column = 0)
    points_msg_entry = Entry(new_frame)
    points_msg_entry.grid(row=5, column=1)
    choices_label = Label(new_frame, text='Other choices (3)').grid(row=6, column=0)
    choices_text1 = Entry(new_frame)
    choices_text1.grid(row=6, column=1)
    choices_text2 = Entry(new_frame)
    choices_text2.grid(row=6, column=2)
    choices_text3 = Entry(new_frame)
    choices_text3.grid(row=6, column=3)
    q_list = [text_entry, c_ans_entry, wrong_msg_entry, correct_msg_entry, points_msg_entry, choices_text1, choices_text2, choices_text3]
    create_button = Button(new_frame, text='Create new question',
                           command=lambda: event_handler('create', new_frame, window, new_list=q_list))
    create_button.grid(row=7, column=0)


# Search question function takes master window
# Shows top 5 results that have 50% or more match
# User has option to go to edit frame to find using Unique ID and change/delete question
def search_questions(window):
    search_frame = Frame(window, bg='purple', width=600, height=600, borderwidth=5, relief=SUNKEN)
    search_frame.grid(row=0, column=0, columnspan=5, sticky=E)
    search_frame.grid_propagate(0)
    back_button = Button(search_frame, text='Go Back to main', command=lambda: event_handler('back', search_frame, window))
    back_button.grid(row=0, column=0)
    search_label = Label(search_frame, text='Enter text from the question to find matches: ').grid(row=0, column=1, padx=2)
    search_entry = Entry(search_frame)
    search_entry.grid(row=0, column=2, padx=2)
    # Event handler manages the search and puts in
    search_button = Button(search_frame, text='Search',
                           command=lambda: event_handler('show_results', search_frame, window, choice=search_entry))
    search_button.grid(row=1, column=1, padx=2)


# Sets up edit/delete menu, shows all details of a choosen question based on ID entered
def edit_del(window):
    global question_master_list
    edit_del_frame = Frame(window, bg='brown', width=600, height=600, borderwidth=5, relief=SUNKEN)
    edit_del_frame.grid(row=0, column=0, columnspan=5, sticky=E)
    edit_del_frame.grid_propagate(0)
    back_button = Button(edit_del_frame, text='Go Back to main', command=lambda: event_handler('back', edit_del_frame, window))
    back_button.grid(row=0, column=0)

    id_label = Label(edit_del_frame, text="ID Number: ", bg='brown').grid(row=0, column=1)
    id_entry = Entry(edit_del_frame)
    id_entry.grid(row=0, column=2)
    id_button = Button(edit_del_frame, text='Search Question',
                       command=lambda: event_handler('single_search', edit_del_frame, window,
                                                     choice=id_entry, new_list=q_list))
    id_button.grid(row=0, column=3)

    text_string = StringVar()
    text_string.set('Question')
    question_text = Entry(edit_del_frame, textvariable=text_string, width=45)
    question_text.grid(row=1, column=2)
    question_label = Label(edit_del_frame, text='Question: ').grid(row=1, column=1)

    correct_string = StringVar()
    correct_string.set('Correct Answer')
    correct_entry = Entry(edit_del_frame, textvariable=correct_string, width=45)
    correct_entry.grid(row=2, column=2)
    correct_label = Label(edit_del_frame, text='Answer: ').grid(row=2, column=1)

    w_feedback_string = StringVar()
    w_feedback_string.set('Wrong answer feedback')
    w_msg_entry = Entry(edit_del_frame, textvariable=w_feedback_string, width=45)
    w_msg_entry.grid(row=3, column=2)
    w_msg_label = Label(edit_del_frame, text='Incorrect Feedback: ').grid(row=3, column=1)

    c_feedback_string = StringVar()
    c_feedback_string.set('Correct Answer feedback')
    c_msg_entry = Entry(edit_del_frame, textvariable=c_feedback_string, width=45)
    c_msg_entry.grid(row=4, column=2)
    c_msg_label = Label(edit_del_frame, text='Correct Feedback: ').grid(row=4, column=1)

    point_value_string = StringVar()
    point_value_string.set('Point value')
    point_value_entry = Entry(edit_del_frame, textvariable=point_value_string, width=45)
    point_value_entry.grid(row=5, column=2)
    point_value_label = Label(edit_del_frame, text='Points: ').grid(row=5, column=1)

    choice1_string = StringVar()
    choice1_string.set('Wrong answer')
    choice1_entry = Entry(edit_del_frame, textvariable=choice1_string, width=45)
    choice1_entry.grid(row=6, column=2)
    choice1_label = Label(edit_del_frame, text='Wrong Choice: ').grid(row=6, column=1)

    choice2_string = StringVar()
    choice2_string.set('Wrong answer')
    choice2_entry = Entry(edit_del_frame, textvariable=choice2_string, width=45)
    choice2_entry.grid(row=7, column=2)
    choice2_label = Label(edit_del_frame, text='Wrong Choice: ').grid(row=7, column=1)

    choice3_string = StringVar()
    choice3_string.set('Wrong answer')
    choice3_entry = Entry(edit_del_frame, textvariable=choice3_string, width=45)
    choice3_entry.grid(row=8, column=2)
    choice3_label = Label(edit_del_frame, text='Wrong Choice: ').grid(row=8, column=1)

    # change button to edit text and details of focused question, updates Question object
    change_button = Button(edit_del_frame,
                           text='Change',
                           command=lambda: event_handler('change_question', edit_del_frame, window, choice=id_entry,
                                                         new_list=q_list))
    change_button.grid(row=9, column=2)

    delete_button = Button(edit_del_frame,
                           text='Delete',
                           command=lambda: event_handler('change_question', edit_del_frame, window, choice=id_entry,
                                                         new_list=q_list))
    delete_button.grid(row=9, column=3)

    q_list = [text_string, correct_string, w_feedback_string, c_feedback_string, point_value_string, choice1_string,
              choice2_string, choice3_string]


# shows "Edit" frame with options to edit questions and search questions
def edit_questions(window):
    # main edit frame
    edit_frame = Frame(window, bg='navy blue', width=600, height=600, borderwidth=5, relief=SUNKEN)
    edit_frame.grid(row=0, column=1, columnspan=5, sticky=E)
    edit_frame.grid_propagate(0)
    # back to main button
    back_button = Button(edit_frame, text='Go Back', command=lambda: event_handler('back', edit_frame, window))
    back_button.grid(row=0, column=0)
    # new question button
    new_button = Button(edit_frame, text='New Question', command=lambda: event_handler('new', edit_frame, window))
    new_button.grid(row=0, column=1)
    # Search button
    search_button = Button(edit_frame, text='Search for Questions', command=lambda: event_handler('search', edit_frame, window))
    search_button.grid(row=1, column=1)
    # edit and delete button
    edit_del_button = Button(edit_frame, text='Edit/Delete Questions', command=lambda: event_handler('edit/del', edit_frame, window))
    edit_del_button.grid(row=2, column=1)


def load_questions():
    questions_file = 'question_pool.json'  # add try statement
    with open(questions_file, 'r') as fp:
        question_dictionary = json.load(fp)
    print('data loaded')
    return question_dictionary


# Saves questions when window closes
# Saved questions, but loading is not finished, commented out to avoid duplicated in json file
def save_questions():
    global question_master_list
    questions_file = 'question_pool.json'
    dictionary_list = {}
    # for loop is used to make temp dictionary
    for q in question_master_list:
        temp_dictionary = {}  # temp will be used to save into json file since master list is an object list
        temp_dictionary['text'] = q.question_text
        temp_dictionary['answer'] = q.correct_choice
        temp_dictionary['wrong'] = q.wrong_message
        temp_dictionary['correct'] = q.correct_message
        temp_dictionary['points'] = q.point_value
        temp_dictionary['choices'] = q.choice_list
        dictionary_list[q.question_id.zfill(4)] = temp_dictionary
    print('--------------------------')
    print(dictionary_list)
    with open(questions_file, 'w') as fp:
        json.dump(dictionary_list, fp)
    print('data saved')


def main():
    global question_master_list
    win = master_window()
    main_menu(win)
    # sample questions to use for tests
    '''quest_dict = {'0001': {'text': 'what is botany in the movie "MARS"?', 'answer': 'potato growing',
                           'wrong': "You aren't a botanist", 'correct': 'you know your stuff!', 'points': '2',
                           'choices': ('dirt research', 'robot repair', 'germ growing')},
                  '0002': {'text': 'what is chemistry?', 'answer': 'study of change',
                           'wrong': 'your no heisenburg', 'correct': 'you know your stuff!', 'points': '2',
                           'choices': ('study of movement', 'study of chemical', 'study of reactions')},
                  '0003': {'text': 'Which letter is not in ANY US state?', 'answer': 'q',
                           'wrong': 'Wrong answer', 'correct': 'you know your stuff!', 'points': '2',
                           'choices': ('z', 'y', 'x')}}'''
    quest_dict = load_questions()
    for k in quest_dict:
        print(k)
        print(quest_dict[k]['text'])
        print(quest_dict[k]['answer'])
        print(quest_dict[k]['wrong'])
        print(quest_dict[k]['correct'])
        print(quest_dict[k]['choices'])
        print(quest_dict[k]['points'])
        question_master_list.append(Question(k, quest_dict[k]['text'], quest_dict[k]['answer'], quest_dict[k]['wrong'],
                                             quest_dict[k]['correct'], quest_dict[k]['points'],
                                             quest_dict[k]['choices']))
    print('---------------------------------------')
    for q in question_master_list:
        print(q)

    win.mainloop()
    save_questions()


main()
