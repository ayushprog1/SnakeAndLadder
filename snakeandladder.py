import tkinter as tk
from PIL import ImageTk, Image
import random 

def start_game():
    global im
    global b1,b2

    #button
    #Player 1
    
    b1.place(x=1200,y=400) 

    #Player 2
    
    b2.place(x=1200,y=600)

    #dice
    im=Image.open("dice.jpeg")
    im=im.resize((98,98))
    im=ImageTk.PhotoImage(im)
    b4=tk.Button(root,image=im,height=100,width=100)
    b4.place(x=1275,y=250)

    #exit
    b3=tk.Button(root,text="Exit",height=3,width=20,fg="red",bg="yellow",font=('cursive',14,'bold'),activebackground='black',command=root.destroy)
    b3.place(x=1200,y=100)

def reset_coin():
    global player_1,player_2
    global pos1,pos2
    player_1.place(x=0,y=630)
    player_2.place(x=50,y=630)

    pos1=0
    pos2=0

def load_dice_image():
    global dice 
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for nam in names:
        im=Image.open(nam)
        im=im.resize((98,98))
        im=ImageTk.PhotoImage(im)
        dice.append(im)

def roll_dice():
    global dice,turn,pos1,pos2
    global b1,b2 
    r=random.randint(1,6)
    b4=tk.Button(root,image=dice[r-1],height=100,width=100)
    b4.place(x=1275,y=250)
    lad=0
    if turn==1:
        if (pos1+r)<=100:
            pos1 =pos1 +r
        lad=check_ladder(turn)
        check_snake(turn)
        move_coin(turn,pos1)
        if r!=6 and lad!=1:
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2+r)<=100:
            pos2=pos2 +r
        lad=check_ladder(turn)
        check_snake(turn)
        move_coin(turn,pos2)
        if r!=6 and lad!=1:
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')

    is_winner()

def is_winner():
    global pos1,pos2

    if pos1==100:
        msg="player 1 is winner"
        Lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coin()
    elif pos2==100:
        msg="player 2 is winner"
        Lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coin()
    


def check_ladder(turn):
    global pos1,pos2
    global ladder
    
    if turn==1:
        if pos1 in ladder:
            pos1=ladder[pos1]
  
    else:
        if pos2 in ladder:
            pos2=ladder[pos2]

def check_snake(turn):
    global pos1,pos2
    global snake
    if turn==1:
        if pos1 in snake:
            pos1=snake[pos1]

    else:
        if pos2 in snake:
            pos2=snake[pos2]





def move_coin(turn,r):
    global player_1,player_2
    global Index
    if turn==1:
        player_1.place(x=Index[r][0],y=Index[r][1])
    else:
        player_2.place(x=Index[r][0],y=Index[r][1])

def get_index():
    global player_1,player_2

    Num=[100, 99,98, 97, 96, 95, 94, 93 ,92 ,91,81, 82, 83, 84, 85, 86, 87, 88, 89, 90,80 ,79 ,78 ,77 ,76 ,75, 74, 73, 72, 71,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
40, 39, 38 ,37, 36, 35, 34, 33, 32, 31,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
20, 19, 18, 17, 16, 15, 14 ,13, 12, 11,
1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    row=10
    i=0
    for x in range(1,11):
        col=10
        for y in range(1,11):
            Index[Num[i]]=(col,row)
            col=col +60
            i=i+1
        row=row+60
    #print(Index)
    


 
dice=[]

Index={}

#intial position
pos1=None
pos2=None

root = tk.Tk()
root.geometry("1200x800")
root.title("Snake and Ladder Game")


F1= tk.Frame(root,width=612,height=612, relief='raised')
F1.place(x=0,y=0)

#Set Board
img1 = ImageTk.PhotoImage(Image.open("board.jpg"))
Lab = tk.Label(F1, image=img1)
Lab.place(x=0,y=0)

#player 1 coin
player_1 = tk.Canvas(root,width=40,height=40)
player_1.create_oval(10,10,40,40,fill='blue')


#player 2 coin
player_2 = tk.Canvas(root,width=40,height=40)
player_2.create_oval(10,10,40,40,fill='red')

turn=1

#player 1 and 2 button
b1=tk.Button(root,text="player 1",height=3,width=20,fg="red",bg="cyan",font=('cursive',14,'bold'),activebackground='blue',command=roll_dice)
b2=tk.Button(root,text="player 2",height=3,width=20,fg="red",bg="pink",font=('cursive',14,'bold'),activebackground='red',command=roll_dice)

#Lader
ladder={2:23,6:45,20:59,52:72,57:96,71:92}

#snake
snake={43:17,50:5,56:8,73:15,84:58,87:49,98:40}

reset_coin()

get_index()

#dice image
load_dice_image()

start_game()

root.mainloop ()