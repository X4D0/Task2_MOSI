import turtle
import random
import math
import numpy as np

jarakGaris = 100
panjangJarum = 80
jumlahJarum = 100
    
gambar = turtle.Turtle()
gambar.hideturtle()
gambar.speed(0)

y = 180
#Menggammbar Garis/Line di kertas
for i in range(0,10):
  gambar.penup()
  gambar.goto(-200,y)
  gambar.pendown()
  gambar.goto(200,y)
  y-=jarakGaris

#Menjatuhkan Jarum ke Kertas
gambar.color("red")
hits = 0
for needle in range(0,jumlahJarum):
#Posisi Jatuhnya Jarum dilakukan secara Random,
  x = random.randint(-180,180)
  y = random.randint(-180,180)
#Sudut/Kemiringan posisi Jarum Random,
  sudut = random.randint(0,360)
  if x <= panjangJarum * np.cos(sudut) or y <= panjangJarum * np.cos(sudut) :
            hits += 1
#Menggambar Jarum diatas kertas.
  gambar.penup()
  gambar.goto(x,y)
  gambar.setheading(sudut)
  gambar.pendown()
  gambar.forward(panjangJarum)
  
print("L = " + str(panjangJarum))
print("N = " + str(jumlahJarum))
print("D = " + str(jarakGaris))
print("Q = " + str(hits))
pi = (2*panjangJarum*jumlahJarum)/(jarakGaris*hits)
print("Pi = "+ str(pi))
error = math.pi-pi
print("Error = " + str(error))
