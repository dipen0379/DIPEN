import random

# importing GUI components
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog



# fetch english words - all words in a dictionary
from english_words import english_words_lower_alpha_set
# from random_word import RandomWords

# defining a class for the game
class HangmanGame:
    # -------------------------- methods
    # default constructor - runs when initializing the class
    def __init__(self, master,word=None):
        #rw = RandomWords()

        
        if word == None:
            #self.word = rw.get_random_word()

            # pull a word from the english_words package
            # english_words package returns a set (without index) so change to list and fetch a random word
            self.word = random.choice(list(english_words_lower_alpha_set))
        else:
            self.word = word
        
        # initialize the window look and feel
        self.master = master
        master.geometry('905x700') # dimension of window
        master.title('HANGMAN') #title of this program
        master.config(bg = '#E7FFFF')# giving color prefrence 

        self.temp_arr = [] # creating a temporary array as a list 
        self.is_game_over = False # preventing infinite loop

    # event listener for exit button
    def close(self):
        global run # making a global variable that can be run through out the program
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
         

    # test print random word
    def displayRandomWord(self):
        return self.word

    # alphabet button press check function
    # runs when an alphabet button is clicked
    def check(self,letter,button):
        global count,win_count,run
        # on click remove the button so it cant be clicked again
        exec('{}.destroy()'.format(button))
        if letter in self.word:
            for i in range(0,len(self.word)):
                if self.word[i] == letter:
                    print (" {} is a correct guess".format(self.word[i]))
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper())) # .config to change the label
            if win_count == len(self.word):
                self.is_game_over = True
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            print ('{} is a wrong guess'.format(letter))
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,150,-50))
            if count == 6:
                self.is_game_over = True
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()

    def player_choice(self,args):
        global run, given_word, choice
        if args == 'comp':
            choice = 'comp'
            given_word = simpledialog.askstring("Word of you Choice", "Please give us a word:")
            run = True
            root.destroy()

        else:
            choice = 'self'
            run = True
            root.destroy()

if __name__ == '__main__':
    global choice, given_word
    given_word = ''
    choice = 'self'
    run = True
    # loop to check if continue playing or not
    while run:
        # instance of tkinter
        root = Tk() #root is window
        if given_word == '':
            # instance of class Hangman
            hangman_test = HangmanGame(root)
        else:
            hangman_test = HangmanGame(root, given_word)

        # initialize exit button and placement
        e1 = PhotoImage(file = 'exit.png')
        ex = Button(root,bd = 0,command = hangman_test.close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
        ex.place(x=770,y=10)

        # initialize play computer button and placement
        comp_img = PhotoImage(file = 'comp.png')
        comp_btn = Button(root,bd = 0,command = lambda: hangman_test.player_choice('comp'),bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = comp_img)
        comp_btn.place(x=665,y=130)

        # initialize play self button and placement
        self_img = PhotoImage(file = 'self.png')
        self_btn = Button(root,bd = 0,command = lambda: hangman_test.player_choice('self'),bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = self_img)
        self_btn.place(x=720,y=70)  

       
        if choice == 'self':
            count = 0
            win_count = 0
            print (hangman_test.displayRandomWord())

            # initialize masked characters in the form of dashes
            x = 200
            for i in range(0,len(hangman_test.word)):
                x += 60
                exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
                exec('d{}.place(x={},y={})'.format(i,x,450))
            
            # letters icon
            # easier by creating png files else would have 26 lines of code for labels
            alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            for alphabet in alphabets:
                exec('{}=PhotoImage(file="{}.png")'.format(alphabet,alphabet))
                
            # hangman images
            hangman_images = ['h1','h2','h3','h4','h5','h6','h7']
            for hangman_image in hangman_images:
                exec('{}=PhotoImage(file="{}.png")'.format(hangman_image,hangman_image))
                
            # letters placement
            buttons = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

            for button in buttons:
                exec('{}=Button(root,bd=0,command=lambda:hangman_test.check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(button[0],button[1],button[0],button[1]))
                exec('{}.place(x={},y={})'.format(button[0],button[2],button[3]))
                
            # hangman placement
            hangman_image_to_places = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
            for hangman_image_to_place in hangman_image_to_places:
                exec('{}=Label(root,bg="#E7FFFF",image={})'.format(hangman_image_to_place[0],hangman_image_to_place[1]))

            # placement of first hangman image
            c1.place(x = 150,y =- 50)

        else:
            # reinitialize given_word so that the same word doesnt repeat
            given_word = ''
            count = 0
            win_count = 0
            hangman_test.temp_arr.clear()
            print (hangman_test.displayRandomWord())
            while not hangman_test.is_game_over:
                # initialize masked characters in the form of dashes
                x = 200
                for i in range(0,len(hangman_test.word)):
                    x += 60
                    exec('d{}=Label(root,text="_",bg="#E7FFFF",justify="center",font=("arial",40))'.format(i))
                    exec('d{}.place(x={},y={})'.format(i,x,450))
                
                # letters icon
                # easier by creating png files else would have 26 lines of code for labels
                alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                for alphabet in alphabets:
                    exec('{}=PhotoImage(file="{}.png")'.format(alphabet,alphabet))
                    
                # hangman images
                hangman_images = ['h1','h2','h3','h4','h5','h6','h7']
                for hangman_image in hangman_images:
                    exec('{}=PhotoImage(file="{}.png")'.format(hangman_image,hangman_image))

                # hangman placement
                hangman_image_to_places = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
                for hangman_image_to_place in hangman_image_to_places:
                    exec('{}=Label(root,bg="#E7FFFF",image={})'.format(hangman_image_to_place[0],hangman_image_to_place[1]))

                # placement of first hangman image
                c1.place(x = 200,y =- 50)

                # -------------- computer guesses
                print (hangman_test.temp_arr)

                while True:
                    guessed_alphabet = random.choice(alphabets)
                    if guessed_alphabet in hangman_test.temp_arr:
                        continue
                    else:
                        hangman_test.temp_arr.append(guessed_alphabet)
                        break
                # test print    
                print (hangman_test.temp_arr)
                # letters placement
                buttons = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

                for button in buttons:
                    exec('{}=Button(root,bd=0,bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(button[0],button[1]))
                    exec('{}.place(x={},y={})'.format(button[0],button[2],button[3]))
                    if guessed_alphabet == button[1]:
                        root.after(3000,hangman_test.check(button[1], button[0]))
            
        # end tkinter
        root.mainloop()

            
