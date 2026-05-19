# To import tkinter for GUI creation
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import colorchooser
#########################################################################

# Sets application main window parameters

m = Tk()
m. title('BMR & BMI CACULATOR © FAISAL HUSSAIN 2024')
m.geometry('750x550')
m.config(bg='royalblue2')
valBMR = 0
valBMI = 0

##############################################################################################

# Sets label parameters for appliction name (Title) text

label1=Label(m, text = "BMR & BMI CACULATOR",  
          background = 'green', foreground ="white",  
          font = ("Arial Black", 12)).place (x= 250, y=15)

##############################################################################################

# Adds a widget which enables users to change the background colour of the application

def chooseColour():
    color=colorchooser.askcolor()
    colorname=color[1]
    m.configure(background=colorname)
    
# Sets background colour selection button parameters

btncolour = Button(m, text = 'Select background colour', bg='white', fg='green',font=("Arial Black",9),height = 3, width = 25, command = chooseColour )
btncolour.place(x= 15  , y = 15)

################################################################################################################

# Sets label parameters for age selection

Label2 = Label(m, text='Select Your Age (to the nearest Whole Year)',bg="black",fg="white")
Label2.place(x=250,y=50)

# Sets slider parameters which will enable a user to select age, ranging from 18years-100years

ages = Scale(m, from_=18, to = 100, orient=HORIZONTAL, background='snow', fg='red', troughcolor='aqua', activebackground='lawn green')
ages.place(x=500,y=30)

#####################################################################################################

# Sets label parameters for height selection

Label3 = Label(m,text='Select Your Height (to the nearest whole CM)',bg="black",fg="white")
Label3.place(x=250,y=110)

# Sets slider parameters which enables a user to select their height, ranging from 120cm-200cm

heightcm = Scale(m, from_ = 120, to = 200, orient = HORIZONTAL,  background='snow', fg='red', troughcolor='aqua', activebackground='lawn green')
heightcm.place(x=500,y=90)

##########################################################################################

# Sets label parameters for weight selection

Label4 = Label (m,text='Select Your Weight (to the nearest whole KG)',bg="black",fg="white")
Label4.place(x=250,y=170)

# to add a slider which enables a user to select their weight, ranging from 40kg-250kg

weight = Scale(m, from_ = 40, to= 250, orient = HORIZONTAL,  background='snow', fg='red', troughcolor='aqua', activebackground='lawn green')
weight.place(x=500,y=150)

###########################################################################################

# Sets label parameters for exercise selection

Label5 = Label(m,text='Select Exercise Routine:',bg='black', fg='white')
Label5.place(x=250,y=210)

# Creates combobox & selectable values

exercisechoosen = ttk.Combobox(m, state="readonly", width = 27, values=["None",
                                                                        "Light (1-3 Days/Week)"
                                                                        , "Moderate (3-5 Days/Week)"
                                                                        , "Heavy (5-6 Days/Week)"
                                                                        , "Intense (7 Days/ Week)"])

# Set combobox parameters

exercisechoosen. place(x="415",y="210")

# creates a Function for when different exercises are selected

def exercise_selected(event):
   selected_exercise = exercisechoosen.get()
   print("You selected:", selected_exercise)
exercisechoosen.bind("<<ComboboxSelected>>", exercise_selected)

# Sets combobox default value 

exercisechoosen.current(0)

###########################################################################################################################

# Does BMR calculation using the Harrison Bendict formula for males 

def harriscalcmale():
    bmr = round(66.47 + (13.75 * weight.get()) + (5.003 * heightcm.get()) - (6.775 * ages.get()))
    textBMR = Label(m, text=bmr, bg='green', fg='white')
    textBMR.place(x=300, y=350)
    valBMR = int(textBMR.cget("text"))  # Get the text from the label and convert it to an integer
    if exercisechoosen.get() == "None":
        valBMR = round(valBMR * 1.2)
    elif exercisechoosen.get() == "Light (1-3 Days/Week)":
            valBMR = round(valBMR * 1.375)
    elif exercisechoosen.get() == "Moderate (3-5 Days/Week)":
            valBMR = round(valBMR * 1.55)
    elif exercisechoosen.get() == "Heavy (5-6 Days/Week)":
            valBMR = round(valBMR * 1.725)
    else:valBMR = round(valBMR * 1.9)
            # Apply the multiplier to valBMR
    multiExercise = Label(m, text=valBMR)
    multiExercise.place(x=500, y=350)
btn = Button(m, text = 'BMR - Harris-Bendict Male',bg='green', fg='aqua', bd = '5',height = 2,width = 25,command = harriscalcmale)
btn.place(x=150,y=250)

#################################################################################################################################################

# Does BMR calculation using the Harrison Bendict formula for females

def harriscalcFemale():
    textBMR = Label(m,text = round(655.1 + (9.563 * weight.get()) + (1.85 * heightcm.get()) - (4.676 * ages.get())),bg='green', fg='white')
    textBMR.place(x=300,y=350)
    valBMR = int(textBMR.cget("text"))  # Get the text from the label and convert it to an integer
    if exercisechoosen.get() == "None":
        valBMR = round(valBMR * 1.2)
    elif exercisechoosen.get() == "Light (1-3 Days/Week)":
            valBMR = round(valBMR * 1.375)
    elif exercisechoosen.get() == "Moderate (3-5 Days/Week)":
            valBMR = round(valBMR * 1.55)
    elif exercisechoosen.get() == "Heavy (5-6 Days/Week)":
            valBMR = round(valBMR * 1.725)
    else:valBMR = round(valBMR * 1.9)
            # Apply the multiplier to valBMR
    multiExercise = Label(m, text=valBMR)
    multiExercise.place(x=500, y=350)

btn2 = Button(m, text = 'BMR - Harris-Bendict Female',bg='pink', fg='purple', bd = '5',height = 2,width = 25,command =harriscalcFemale )
btn2.place(x=350,y=250)

##################################################################################################################################################

# Does the BMR calculation using the Mifflin formula for males

def joercalcmale():
    textBMR = Label(m,text = round((10 * weight.get()) + (6.25 * heightcm.get()) - 5* ages.get()+ 5),bg='green', fg='white')
    textBMR.place(x=300,y=350)
    valBMR = int(textBMR.cget("text"))  # Get the text from the label and convert it to an integer
    if exercisechoosen.get() == "None":
        valBMR = round(valBMR * 1.2)
    elif exercisechoosen.get() == "Light (1-3 Days/Week)":
            valBMR = round(valBMR * 1.375)
    elif exercisechoosen.get() == "Moderate (3-5 Days/Week)":
            valBMR = round(valBMR * 1.55)
    elif exercisechoosen.get() == "Heavy (5-6 Days/Week)":
            valBMR = round(valBMR * 1.725)
    else:valBMR = round(valBMR * 1.9)
            # Apply the multiplier to valBMR
    multiExercise = Label(m, text=valBMR)
    multiExercise.place(x=500, y=350)# Adds button & parameters

btn3 = Button(m, text = 'BMR - Miffin St Jeor Male',bg='aqua', fg='green', bd = '5',height = 2,width = 25,command =joercalcmale )
btn3.place(x=150,y=300)

#############################################################################################################################################

# Does the BMR calculation using the Mifflin formula for females    

def joercalcFemale():
    textBMR = Label(m,text = round((10 * weight.get()) + (6.25 * heightcm.get()) - 5* ages.get()-161),bg='green', fg='white')
    textBMR.place(x=300,y=350)
    valBMR = int(textBMR.cget("text"))  # Get the text from the label and convert it to an integer
    if exercisechoosen.get() == "None":
        valBMR = round(valBMR * 1.2)
    elif exercisechoosen.get() == "Light (1-3 Days/Week)":
            valBMR = round(valBMR * 1.375)
    elif exercisechoosen.get() == "Moderate (3-5 Days/Week)":
            valBMR = round(valBMR * 1.55)
    elif exercisechoosen.get() == "Heavy (5-6 Days/Week)":
            valBMR = round(valBMR * 1.725)
    else:valBMR = round(valBMR * 1.9)
            # Apply the multiplier to valBMR
    multiExercise = Label(m, text=valBMR)
    multiExercise.place(x=500, y=350)# Adds button & parameters
# Adds button & parameters

btn4 = Button(m, text = 'BMR - Miffin St Jeor Female',bg='purple', fg='pink', bd = '5',height = 2,width = 25,command =joercalcFemale )
btn4.place(x=350,y=300)

#############################################################################################################################################    

# Adds label to inform user the the data that follows is the results of the BMR calculation

textBMR = Label(m,text='BMR is ',bg="black",fg="white")
textBMR.place(x=150,y=350)

#################################################################################################################################################

#routine = exercisechoosen.get()


#if routine == "None" : texBMR =textBMR*1.2


# This is the formula & caculation for BMI

def bmi():
    bmi_value = round(weight.get() / ((heightcm.get() / 100) ** 2))
    textBMI.config(text=f'{bmi_value}', bg='green', fg='white')
    textBMI.place(x=400, y=400)

    if bmi_value < 18:
        weightclass = "UNDERWEIGHT!"
    elif 18 <= bmi_value < 25:
        weightclass = "HEALTHY WEIGHT!!"
    elif 25 <= bmi_value < 30:
        weightclass = "OVERWEIGHT!!!"
    else:
        weightclass= "OBESSE!!!"

    bmiresult.config(text=f'Your BMI category is: {weightclass}')

btn5 = Button(m, text='BMI', bg='orange', fg='red', bd='5', height=2, width=25, command=bmi)
btn5.place(x=150, y=375)

# Adds label to inform user the data that follows is the results of the BMI calculation
textBMI = Label (m, text= bmi)
textBMI.place(x=400, y=400)
textrange = Label(m, text='BMI is ', bg='black', fg='white')
textrange.place(x=350, y=400)

bmiresult = Label(m, text='', bg='black', fg='white')
bmiresult.place(x=600, y=550)

    #elif exercisechoosen.get() == "Light (1-3 Days/Week)":
           # valBMR = round(valBMR * 1.375)
    #elif exercisechoosen.get() == "Moderate (3-5 Days/Week)":
            #valBMR = round(valBMR * 1.55)
    #elif exercisechoosen.get() == "Heavy (5-6 Days/Week)":
            #valBMR = round(valBMR * 1.725)
   # else:valBMR = round(valBMR * 1.9)
            

#btn5 = Button(m, text = 'BMI', bg='orange', fg='red', bd = '5',height = 2,width = 25,command = bmi)
#btn5.place(x=150,y=375)

# Adds label to inform user the the data that follows is the results of the BMI calculation

#textBMI = Label(m,text='BMI is ',)
#textBMI.place(x=350,y=400)


#################################################################################################################################################
#def bmi():
    #bmi_value = round(weight.get() / ((heightcm.get() / 100) ** 2))
    #textBMI.config(text=f'BMI is {bmi_value}', bg='green', fg='white')
   # textBMI.place(x=400, y=400)




#bmiranger = Label(m, text='', bg='black', fg='white')
#bmiranger.place(x=600, y=550)
m.mainloop()
    

