import os, sys, io
import M5
from M5 import *
import time

label1 = None
value = 17
buttons = []

class Button:
  def __init__(self, title, x, y, w, h, c, fc):
    self.title = title
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.tx = -1
    self.ty = -1
    self.rect = Widgets.Rectangle(x, y, w, h, c, fc)
    self.label = Widgets.Label(title, x+45, y+10, 1.0, 0xffffff, fc, Widgets.FONTS.DejaVu18)

  def update(self):
    if M5.Touch.getCount() > 0:
      tx = M5.Touch.getX()
      ty = M5.Touch.getY()
      if tx != self.tx or ty != self.ty:
        self.tx = tx - 20
        self.ty = ty
        if self.x <= tx <= self.x + self.w and self.y <= ty <= self.y + self.h:
          if callable(self.click): self.click()
    
  def click(self):
    global value
    if self.title=='+2': value += 2
    if self.title=='*2': value *= 2
    if self.title=='/2' and value % 2 == 0: value //= 2
    label1.setText(str(value))
    time.sleep_ms(250)

def setup():
  global label1
  M5.begin()
  Widgets.fillScreen(0x222222)
  
  label1 = Widgets.Label(str(value), 150, 80, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  buttons.append(Button('+2',  5, 200, 100, 35, 0xff0000, 0x880000))
  buttons.append(Button('*2',110, 200, 100, 35, 0x00ff00, 0x008800))
  buttons.append(Button('/2',215, 200, 100, 35, 0x0000ff, 0x000088))

def loop():
  M5.update()
  for button in buttons:
    button.update()

setup()
while True:
  loop()
