import turtle as t
import random

#Setup Turtle
t.screensize(2000, 3000) #mengatur ukuran layar turtle 
t.speed(0) #Mengatur kecepatan penggambaran
t.hideturtle() #menyembunyikan cursor
t.width(10) #mengatur ketebalan pulpen

title = "Olympic Logo and Colorful Chessboard"
t.title(title) #Membuat judul pada window
t.colormode(255) #mengatur mode warna ke RGB

#meminta input kepada user
row = t.numinput(title , "Enter the number of rows: ", 10, 2, 25)
size = t.numinput(title , "Enter the square size(pixels): ", 20, 5, 50)

#mendefinisikan warna
blue = (0, 129, 200)
yellow = (252, 177, 49)
black = (0, 0, 0)
green = (0, 166, 81)
red = (238, 51, 78)

#membuat logo Olympic pertama
t.penup()
t.goto(-120, 200)
t.pendown()
t.color(blue)
t.circle(50)

t.penup()
t.goto(-60, 150)
t.pendown()
t.color(yellow)
t.circle(50)

t.penup()
t.goto(0, 200)
t.pendown()
t.color(black)
t.circle(50)

t.penup()
t.goto(60, 150)
t.pendown()
t.color(green)
t.circle(50)

t.penup()
t.goto(120, 200)
t.pendown()
t.color(red)
t.circle(50)

#menumpuk lingkaran di logo olympic pertama agar menjadi terhubung satu sama lain (interlocked)
t.penup()
t.goto(-120, 200)
t.color(blue)
t.pendown()
t.circle(50, -280)

t.penup()
t.goto(-60, 250)
t.color(yellow)
t.pendown()
t.setheading(180)
t.circle(50, -60)

t.penup()
t.goto(0, 200)
t.color(black)
t.pendown()
t.setheading(0)
t.circle(50, 120)

t.penup()
t.goto(60, 250)
t.color(green)
t.pendown()
t.setheading(180)
t.circle(50, -300)

t.penup()
t.goto(120, 200)
t.color(red)
t.pendown()
t.setheading(0)
t.circle(50, -40)

#membuat logo olympic kedua
t.penup()
t.home()
t.goto(-120, 0)
t.pendown()
t.color(blue)
t.circle(50)

t.penup()
t.goto(-60, 0)
t.pendown()
t.color(yellow)
t.circle(50)

t.penup()
t.goto(0, 0)
t.pendown()
t.color(black)
t.circle(50)

t.penup()
t.goto(60, 0)
t.pendown()
t.color(green)
t.circle(50)

t.penup()
t.goto(120, 0)
t.pendown()
t.color(red)
t.circle(50)


#menumpuk lingkaran di logo kedua agar menajadi terhubung satu sama lain (interlocked)
t.penup()
t.goto(-120, 0)
t.pendown()
t.color(blue)
t.circle(50,)


t.penup()
t.home()
t.goto(-60, 0)
t.pendown()
t.color(yellow)
t.circle(50,-90)

t.penup()
t.home()
t.goto(-60, 0)
t.pendown()
t.color(yellow)
t.circle(50,180)

t.penup()
t.home()
t.goto(0, 0)
t.pendown()
t.color(black)
t.circle(50,-90)

t.penup()
t.home()
t.goto(0, 0)
t.pendown()
t.color(black)
t.circle(50,180)

t.penup()
t.home()
t.goto(60, 0)
t.pendown()
t.color(green)
t.circle(50,-90)

t.penup()
t.home()
t.goto(60, 0)
t.pendown()
t.color(green)
t.circle(50,180)

t.penup()
t.home()
t.goto(120, 0)
t.pendown()
t.color(red)
t.circle(50,-90)

t.penup()
t.home()
t.goto(120, 0)
t.pendown()
t.color(red)
t.circle(50, 180)

t.width(1) #mengatur ulang ketebalan pulpen


#menentukan titik awal penggambaran chessboard
startx = (size * row) / -2 
starty = -25 

#membuat chessboard
for i in range(int(row)):
    t.penup()
    t.home()
    t.goto(startx, starty)
    t.pendown()
    starty = starty - size
    for i in range(int(row)):
        #mendefinisikan random color
        r = random.randint(0, 255)  
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)

        t.color(color)    
        t.fillcolor(color)  
        t.begin_fill()
        for i in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()
        t.forward(size)

t.penup()
t.goto(0, starty - 50)
t.color("blue")
t.pendown()


#menulis judul dan jumlah kotak di bawah gambar
t.write(f'{title} of {int(row*row)} Squares', align="center", font=("Arial", 16, "normal"))


t.penup()
t.done() #membuat screen tidak langsung tertutup