from M5 import Widgets,begin,Touch,update
import time

label1 = None
value = 19
buttons = []

class Button:
  def __init__(self, title, x):
    self.title = title
    self.x = x
    self.y = 200
    self.w = 100
    self.h = 35
    self.tx = -1
    self.ty = -1
    self.rect = Widgets.Rectangle(self.x, self.y, self.w, self.h) #, c, fc)
    self.label = Widgets.Label(title, x+45, self.y+10, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)

  def update(self):
    if Touch.getCount() > 0:
      tx = Touch.getX()
      ty = Touch.getY()
      if tx != self.tx or ty != self.ty:
        self.tx = tx - 20
        self.ty = ty
        if 0 <= tx-self.x <= self.w and 0 <= ty-self.y <= self.h: self.click()
    
  def click(self):
    global value
    if self.title=='+2': value += 2
    if self.title=='*2': value *= 2
    if self.title=='/2' and value % 2 == 0: value //= 2
    label1.setText(str(value))
    time.sleep_ms(250)

begin()
Widgets.fillScreen(0x222222)

label1 = Widgets.Label(str(value), 150, 80, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
buttons.append(Button('+2',  5))
buttons.append(Button('*2',110))
buttons.append(Button('/2',215))

while True:
  update()
  for button in buttons:
    button.update()
