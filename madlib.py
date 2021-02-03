import tkinter as tk

def madlib1 ():
    name = input("what is the name of your hero?: ")
    weapon = input("Your hero's weapon of choice?: ")
    location = input("What world does your hero come from?: ")
    villian = input("Who or what is your hero fighting?: ")

    print (name + " was the greatest hero of " + location + ". They had fought many a beast and enemy but their greatest battle of all was agaisnt " + villian +
    ", the fiercest of all. " + name + " defeated this evil using only their " + weapon + ".")

class interface():
    def __init__(self, master = None): 

        self.colour = None
        self.plural_noun = None
        self.snack = None
        self.new_sentence = None
        self.build_window()

    def build_window(self):
        master = tk.Tk()
        #creating all elements to populate the window
        tk.Label(master, text="Colour: ").grid(row=0)
        tk.Label(master, text="Plural Noun: ").grid(row=1)
        tk.Label(master, text=" Favourite Snack: ").grid(row=2)
        self.new_sentence = tk.Label(master, text=" ")
        self.new_sentence.grid(row=3)
        submit = tk.Button(text="SUBMIT", command = self.update_sentence)

        self.colour = tk.Entry(master)
        self.plural_noun = tk.Entry(master)
        self.snack = tk.Entry(master)

        #positioning elements in window using grid method
        self.colour.grid(row=0, column=1)
        self.plural_noun.grid(row=1, column=1)
        self.snack.grid(row=2, column=1)
        submit.grid(row=4, columnspan=2)
        master.mainloop()

    def update_sentence (self):
        sentence = ("Roses are " + self.colour.get() + ", " + self.plural_noun.get() + " are blue, I love " + self.snack.get())
        self.new_sentence.config(text=sentence)



interface()

