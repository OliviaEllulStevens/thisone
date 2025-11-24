import tkinter as tk
from tkinter import font, messagebox
import time #rt stuff idk if it is right
import csv
import os

#tkinter = library of layout stuff
#imports fonts (size, fam etc) and messageboxes for popups (eg. ID page)
#tkMessageBox = used to diplay message boxes -- perf for ID popup https://www.tutorialspoint.com/python/tk_messagebox.htm

#questions, each mcq, 4 options, with correct poption at the end from 0-3
#https://www.youtube.com/watch?v=SgQhwtIoQ7o
questions = [
    {"q": "What is the largest planet in our Solar System?", "opts": ["Earth","Jupiter","Saturn","Neptune"], "a":1}, 
    {"q": "Who wrote 'Romeo and Juliet'?", "opts": ["Charles Dickens","William Shakespeare","Jane Austen","Mark Twain"], "a":1}, 
    {"q": "What is the capital city of Japan?", "opts": ["Kyoto","Osaka","Tokyo","Sapporo"], "a":2}, 
    {"q": "Which element has the symbol 'O'?", "opts": ["Oxygen","Gold","Silver","Osmium"], "a":0}, 
    {"q": "Which country hosted the 2016 Summer Olympics?", "opts": ["Brazil","China","UK","Russia"], "a":0}, 
    {"q": "What is the chemical formula of water?", "opts": ["CO2","H2O","O2","NaCl"], "a":1}, 
    {"q": "Which continent is the Sahara Desert on?", "opts": ["Asia","Africa","Australia","South America"], "a":1}, 
    {"q": "Who developed the theory of relativity?", "opts": ["Isaac Newton","Albert Einstein","Niels Bohr","Galileo"], "a":1}, 
    {"q": "What is the smallest prime number?", "opts": ["0","1","2","3"], "a":2}, 
    {"q": "Which ocean is the largest?", "opts": ["Atlantic","Indian","Pacific","Arctic"], "a":2}, 
    {"q": "What is the capital of France?", "opts": ["Paris","Berlin","Rome","Madrid"], "a":0}, 
    {"q": "Who painted the Mona Lisa?", "opts": ["Van Gogh","Leonardo da Vinci","Michelangelo","Picasso"], "a":1}, 
    {"q": "Which gas do humans breathe in?", "opts": ["Carbon dioxide","Oxygen","Nitrogen","Hydrogen"], "a":1}, 
    {"q": "How many continents are there?", "opts": ["5","6","7","8"], "a":2}, 
    {"q": "Which country is known as the Land of the Rising Sun?", "opts": ["China","South Korea","Japan","Thailand"], "a":2}, 
    {"q": "What is the boiling point of water in Celsius?", "opts": ["90","100","110","120"], "a":1}, 
    {"q": "What is the fastest land animal?", "opts": ["Cheetah","Horse","Leopard","Lion"], "a":0}, 
    {"q": "Which is the largest mammal?", "opts": ["Elephant","Blue Whale","Giraffe","Hippo"], "a":1}, 
    {"q": "What is the capital of Italy?", "opts": ["Rome","Milan","Venice","Naples"], "a":0}, 
    {"q": "What is H in the periodic table?", "opts": ["Helium","Hydrogen","Hafnium","Holmium"], "a":1}, 
    {"q": "Which planet is known as the Red Planet?", "opts": ["Venus","Mars","Jupiter","Mercury"], "a":1}, 
    {"q": "Who was the first man on the moon?", "opts": ["Neil Armstrong","Buzz Aldrin","Yuri Gagarin","John Glenn"], "a":0}, 
    {"q": "What is the currency of Japan?", "opts": ["Yen","Won","Dollar","Peso"], "a":0}, 
    {"q": "Which language has the most speakers worldwide?", "opts": ["English","Mandarin","Hindi","Spanish"], "a":1}, 
    {"q": "Which bird is known for its colorful feathers?", "opts": ["Crow","Parrot","Peacock","Penguin"], "a":2}, 
    {"q": "Which is the smallest country in the world?", "opts": ["Monaco","Vatican City","San Marino","Liechtenstein"], "a":1}, 
    {"q": "Which organ pumps blood in the body?", "opts": ["Liver","Lungs","Heart","Kidney"], "a":2}, 
    {"q": "Which is the tallest mountain?", "opts": ["K2","Everest","Kilimanjaro","Denali"], "a":1}, 
    {"q": "Which desert is the largest in the world?", "opts": ["Sahara","Gobi","Kalahari","Arabian"], "a":0}, 
    {"q": "What is the national sport of Japan?", "opts": ["Karate","Judo","Sumo wrestling","Baseball"], "a":2}, 
    {"q": "What is the longest river in the world?", "opts": ["Amazon","Nile","Yangtze","Mississippi"], "a":1}, 
    {"q": "Which country is famous for pizza and pasta?", "opts": ["France","Italy","Spain","Portugal"], "a":1}, 
    {"q": "What is the chemical symbol for gold?", "opts": ["Ag","Au","Pb","Gd"], "a":1}, 
    {"q": "Which is the fastest bird?", "opts": ["Falcon","Eagle","Sparrow","Ostrich"], "a":0}, 
    {"q": "How many players in a football (soccer) team?", "opts": ["9","10","11","12"], "a":2}, 
    {"q": "Which ocean is the Bermuda Triangle in?", "opts": ["Pacific","Atlantic","Indian","Arctic"], "a":1}, 
    {"q": "Which is the deepest ocean trench?", "opts": ["Java","Puerto Rico","Mariana","Tonga"], "a":2}, 
    {"q": "Who invented the light bulb?", "opts": ["Alexander Graham Bell","Thomas Edison","Nikola Tesla","Einstein"], "a":1}, 
    {"q": "Which is the largest island?", "opts": ["Greenland","New Guinea","Borneo","Madagascar"], "a":0}, 
    {"q": "What is the capital of Canada?", "opts": ["Toronto","Ottawa","Vancouver","Montreal"], "a":1}, 
    {"q": "What is the capital of England?", "opts": ["London","Paris","Berlin","Spain"], "a":0}, 
    {"q": "What is 51 + 24?", "opts": ["72", "75", "77", "74"], "a": 1},
    {"q": "What is 9 + 43?", "opts": ["54", "51", "52", "49"], "a": 2},
    {"q": "What is 4 + 37?", "opts": ["31", "41", "44", "45"], "a": 1},
    {"q": "What is 31 x 3?", "opts": ["93", "63", "91", "90"], "a": 0},
    {"q": "Which number is not a multiple of 6?", "opts": ["24", "66", "32", "6"], "a": 2},
    {"q": "Choose the sum that does not equal one", "opts": [ "0.51+0.49", "12+88", "0.76+0.24", "0.80+0.20"], "a": 1},
    {"q": "What is 130 + 170?", "opts": ["300", "400", "280", "330"], "a": 0},
    {"q": "What is 36/6?", "opts": ["5", "6", "7", "8"], "a": 1},
    {"q": "What is 56 - 58?", "opts": ["4", "1", "2", "-2"], "a": 3},
    {"q": "What is 98.7 + 0.5?", "opts": ["99.2", "99.4", "100.2", "100.4"], "a": 0},
    {"q": "What is 23 + 78?", "opts": ["100", "101", "103", "104"], "a": 1},
    {"q": "How many faces are on a cube?", "opts": ["5", "4", "7", "6"], "a": 3},
    {"q": "Which of these numbers is prime?", "opts": ["15", "16", "19", "21"], "a": 2},
    {"q": "Halve 26", "opts": ["12", "14", "13", "11"], "a": 2},
    {"q": "What is 90 - 53?", "opts": ["37", "47", "33", "29"], "a": 0},
    {"q": "What is 10 - 11?", "opts": ["1", "2", "-2", "-1"], "a": 3},
    {"q": "What is 43 - 13?", "opts": ["30", "29", "28", "31"], "a": 0},
    {"q": "What is 5 - 0?", "opts": ["0", "5", "6", "4"], "a": 1},
    {"q": "What is 94 - 67?", "opts": ["39", "32", "27", "31"], "a": 2},
    {"q": "What is 56 + 42?", "opts": ["88", "98", "94", "86"], "a": 1},
    {"q": "How many degrees are in a square?", "opts": ["720", "360", "180", "420"], "a": 1},
    {"q": "What is 5 x 13?", "opts": ["60", "75", "70", "65"], "a": 3},
    {"q": "What is 0 x 0?", "opts": ["0.1", "0", "1", "2"], "a": 1},
    {"q": "What is 5 x 0?", "opts": ["1", "5", "0", "4"], "a": 2},
    {"q": "What is 93 - 89?", "opts": ["5", "4", "6", "7"], "a": 1},
    {"q": "What is 12/3?", "opts": ["4", "3", "6", "2"], "a": 0},
    {"q": "What is 5/5?", "opts": ["5", "2", "1", "0"], "a": 2},
    {"q": "What is 4 x 22?", "opts": ["44", "88", "99", "80"], "a": 1},
    {"q": "What is 60 + 82?", "opts": ["122", "136", "142", "132"], "a": 2},
    {"q": "What is 20/5?", "opts": ["2", "4", "6", "5"], "a": 1},
    {"q": "What is 58 + 90?", "opts": ["139", "150", "138", "148"], "a": 3},
    {"q": "What is 83 - 63?", "opts": ["15", "20", "22", "23"], "a": 1},
    {"q": "What is 23.25 to the nearest whole number?", "opts": ["23", "24", "22", "20"], "a": 0},
    {"q": "What is the square root of 64?", "opts": ["6", "12", "8", "16"], "a": 2},
    {"q": "What is 54/6?", "opts": ["9", "6", "12", "4"], "a": 0},
    {"q": "What is 11 x 11?", "opts": ["139", "111", "121", "100"], "a": 2},
    {"q": "What is 73 - 37?", "opts": ["41", "51", "42", "36"], "a": 3},
    {"q": "What is 4 squared?", "opts": ["24", "16", "8", "4"], "a": 1},
    {"q": "What is 9 x 7?", "opts": ["63", "61", "70", "54"], "a": 0},
    {"q": "What is 50 x 11?", "opts": ["520", "500", "550", "450"], "a": 2},
]

questions_part1 = questions[:40]
questions_part2 = questions[41:]

#runs quiz after ID is entered
def start_quiz(pid, questions_set):  # pid = participant ID
    global id_window
    try:
        id_window.destroy()
    except Exception:
        pass
    # safely destroy ID entry window if it exists

#https://youtu.be/0WafQCaok6g?si=bqKZaCDFdM-gYS4E
#^^ super useful to understand code stucture, BUT HAS OUTDATED CODE
    root = tk.Tk() # root = main tkinter window
    root.title("Knowledge Quiz")
    root.attributes('-fullscreen', True)
    root.configure(bg="white")

    #fontsssss
    title_font = font.Font(family="Times New Roman", size=22, weight="bold")
    question_font = font.Font(family="Times New Roman", size=17)
    option_font = font.Font(family="Times New Roman", size=17)

    #creating a main frame
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(fill="both", expand = True)

    #create a canvas to be held in root
    canvas = tk.Canvas(main_frame, bg="white", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    #add a scrollbar to canvas
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    #setting yscroll to main_frame, BUT set scrollbar to canvas

    #create another frame inside canvas and configure it
    second_window = tk.Frame(canvas, bg="white")
    second_window.bind(
        "<Configure>", 
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    #to run a function we use lambda, bound to e (an event like mouseclick)
    
    canvas.create_window((0, 0), window=second_window, anchor="n", width=root.winfo_screenwidth())
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    #quiz title
    title_lbl = tk.Label(second_window, text="Knowledge Quiz", font=title_font, bg="white", fg="black")
    title_lbl.pack(side="top", pady=8)

    #tracking of answers + RTs
    user_vars = [] #stores selected answers
    option_labels = [] #stores clickable label widgets
    answered_questions = set() # keep track of answered question numbers
    reaction_times = {} #store reaction times for answered questions
    question_counter = 0


    #CUMULATIVE RT: track when last question was answered
    last_answer_time = time.time()

    #mcq option selection
    def on_select(question_number, option_index):
        nonlocal last_answer_time, question_counter 

        user_vars[question_number].set(option_index)
        refresh_question(question_number)

        # Count only FIRST answer to each question
        if question_number not in answered_questions:
            answered_questions.add(question_number)
            question_counter += 1   

            # Reaction-time logic
            current_time = time.time()
            reaction_times[question_number] = current_time - last_answer_time
            last_answer_time = current_time

    def refresh_question(question_number):
        sel = user_vars[question_number].get()
        for option_index, lbl in enumerate(option_labels[question_number]):
            if sel == option_index:
                lbl.config(text=f"●  {questions_set[question_number]['opts'][option_index]}", fg="black", bg="white")
            else:
                lbl.config(text=f"◯  {questions_set[question_number]['opts'][option_index]}", fg="black", bg="white")

    def submit():
        score = sum(1 for i, v in enumerate(user_vars) if v.get() == questions_set[i]["a"])
        messagebox.showinfo("Result", f"You scored {score} out of {len(questions_set)}")
        #accuracy measure (not a countervariable) - loops through all questions, checks if correct
        #if correct, adds 1
        #v.get() = option selected 
        #for i (qn) and v (selected option) in enumerate (allows you to know both index and value)
        #enumerate loops through all the participants answers to compare their answer to correct answer  
        
        data = []
        for qn, question in enumerate(questions_set):
            selected = user_vars[qn].get()
            correct = question["a"]
            rt = reaction_times.get(qn, None)
            data.append({
                "Participant ID": pid,
                "Question Number": qn + 1,
                "Question Text": question["q"],
                "Selected Option": question["opts"][selected] if selected != -1 else "Skipped",
                "Correct Option": question["opts"][correct],
                "Is Correct": selected == correct if selected != -1 else False,
                "Reaction Time (s)": round(rt, 3) if rt is not None else "N/A"
            })

        #https://www.geeksforgeeks.org/python/writing-csv-files-in-python/
        with open('3.csv', mode="w", newline="") as f:
            fieldnames = [
                "Participant ID", "Question Number", "Question Text",
                "Selected Option", "Correct Option", "Is Correct", "Reaction Time (s)"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        if questions_set == questions_part1:
            messagebox.showinfo("Next Section", "Now starting Part 2.")
            root.destroy()
            start_quiz(pid, questions_part2)
        else:
            messagebox.showinfo("End", "Thank you for completing the quiz!")
            root.destroy()

    #layout of qs
    for question_number, question in enumerate(questions_set): #enumerate allos you to get index (0, 1, 2) and the actual question
        q_frame = tk.Frame(second_window, bg="white", padx=4, pady=6)
        q_frame.pack(fill="x", anchor="center", padx=10, pady=6)

        q_label = tk.Label(q_frame, text=f"{question_number+1}. {question['q']}",
                           font=question_font, bg="white", fg="black", wraplength=1000, justify="center")
        q_label.pack(anchor="center")

        var = tk.IntVar(value=-1)
        user_vars.append(var)

        labels_for_q = []
        for option_index, option_text in enumerate(question["opts"]):
            opt_lbl = tk.Label(q_frame, text=f"◯  {option_text}", font=option_font,
                               bg="white", fg="black", justify="center")
            opt_lbl.bind(
            "<Button-1>", 
            lambda e, qn=question_number, oi=option_index: on_select(qn, oi))
            opt_lbl.pack(anchor="center", pady=2)
            labels_for_q.append(opt_lbl)

        option_labels.append(labels_for_q)

    tk.Button(second_window, text="Submit", command=submit,
              font=question_font, bg="lightblue", fg="black").pack(pady=20)

    root.mainloop()

#info screen page
def show_info_sheet():
    info = tk.Tk()
    info.title("Information Sheet")
    info.attributes('-fullscreen', True)
    info.configure(bg="white")

    text = """Welcome to the experiment. 
Please enter your Participant ID next."""
    lbl = tk.Label(info, text=text, font=("Times New Roman", 22), bg="white", fg="black", justify="center", wraplength=1000)
    lbl.pack(pady=50)

    tk.Button(info, text="Continue", font=("Times New Roman", 18),
              bg="lightblue", command=lambda: (info.destroy(), ask_participant_id())).pack()

    info.mainloop()

#ID page
def ask_participant_id():
    global id_window
    id_window = tk.Tk()
    id_window.title("Participant ID Entry")
    id_window.attributes('-fullscreen', True)
    id_window.configure(bg="white")

    tk.Label(id_window, text="Enter Participant ID:", font=("Times New Roman", 22),
             bg="white", fg="black").pack(pady=20)

    entry = tk.Entry(id_window, font=("Times New Roman", 20), justify="center")
    entry.pack(pady=10)
    #https://www.tutorialspoint.com/python/tk_entry.htm

    def proceed():
        pid = entry.get().strip()
        if not pid:
            messagebox.showerror("Error", "Please enter a valid Participant ID.")
            return
        start_quiz(pid, questions_part1)

    tk.Button(id_window, text="Start Quiz", font=("Times New Roman", 18),
              bg="black", fg="black", command=proceed).pack(pady=30)

    id_window.mainloop()


show_info_sheet()

#to make it run in person
#go to terminal, 
#python -m http.server 0000
#^^ opened up port on internet, 