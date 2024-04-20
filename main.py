from tkinter import *

window = Tk()
window.minsize(width=200, height=150)
window.title("BMI")
window.config(padx=20, pady=20)

def bmi_calculate():
    height = height_entry.get()
    weight = weight_entry.get()

    if weight == "" or height == "":
        answer.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            resultString = writeResult(bmi)
            answer.config(text=resultString)
        except:
            answer.config(text="Enter a valid number")

weightLabel = Label(text="Enter your weight(kg)", fg="red")
weightLabel.pack()

weight_entry = Entry(width=5)
weight_entry.pack()

heightLabel = Label(text="Enter your height(cm)", fg="red")
heightLabel.pack()

height_entry = Entry(width=5)
height_entry.pack()

button = Button(text="Calculate", command=bmi_calculate)
button.pack()

answer = Label()
answer.pack()

def writeResult(bmi):
    resultString = f"Your bmi is : {round(bmi, 2)}. You are "
    if bmi <= 16:
        resultString += "severely thin!"
    elif 16 < bmi <= 17:
        resultString += "moderately thin!"
    elif 17 < bmi <= 18.5:
        resultString += "mild thin"
    elif 18.5 < bmi <= 25:
        resultString += "normal"
    elif 25 < bmi <= 30:
        resultString += "overweight"
    elif 30 < bmi <= 35:
        resultString += "obese class 1"
    elif 35 < bmi <= 40:
        resultString += "obese class 2"
    else:
        resultString += "obese class 3"
    return resultString

window.mainloop()