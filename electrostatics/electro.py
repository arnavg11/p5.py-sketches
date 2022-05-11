charges = []
k = 20
chrg = 0
mss = 1
cmove = True
massKeys = [81,87,69,82,84,89,85,73,79,80]
sgn = 1
def sign(x):
    if x<0:return -1
    return 1
class Charge:#movable
    def __init__(self,pos,canMove = True,charge=1,mass=1):
        self.pos = pos
        self.vel = PVector(0,0)
        self.m = mass
        self.q = charge
        self.move = canMove
        charges.append(self)
    def update(self):
        if self.move or self.q==0:
            self.vel.add(self.calcforce())
            if self.vel.mag()>10:self.vel.setMag(10)
            self.pos.add(self.vel)
            if not 0<self.pos.x<width or not 0<self.pos.y<height:
                self.pos.x = constrain(self.pos.x,0,width)
                self.pos.y = constrain(self.pos.y,0,height)
                self.move = False
        push()
        if self.q>=0:fill(self.q*255/10,255,255)
        else:fill(255,-self.q*255/10,0)
        circle(self.pos.x,self.pos.y,10*self.m)
        pop()
    def calcforce(self):
        a = PVector(0,0)
        for i in charges:
            if i==self:continue
            elif (self.pos-i.pos).mag<=(self.m+i.m)*10:
                self.vel = PVector(0,0)
                continue
            try:
                m = k*i.q*self.q/(self.m*(self.pos-i.pos).mag()**2)
            except ZeroDivisionError:
                m=0
            if sign(self.q*i.q)==1:
                a.add((self.pos-i.pos).setMag(m))
            else:
                a.add((self.pos-i.pos).setMag(m))
        return a
def setup():
   size(400,400)
   background(0)
   noStroke()
# Charge(PVector(200,0),False,3)
# Charge(PVector(200,400),False,3)
# Charge(PVector(50,200),True,-3)
# Charge(PVector(350,200),True,-3)
def draw():
    background(0)
    circle(200,0,10)
    circle(200,400,10)
    push()
    stroke(255)
    line(0,200,400,200)
    pop()
    for i in charges:
        i.update()
    if mousePressed:
        mouse = PVector(mouseX,mouseY)
        for i in charges:
            if (mouse-i.pos).mag()<10:
                break
        else:
            '''
            shift:canMove = false
            0-9:charge-1
            q-p:mass-2
            '''
            if not keyPressed:
                print(1)
                Charge(mouse)
                return
            Charge(mouse,cmove,sgn*chrg,mss)
def keyPressed():
    global chrg,cmove,mss,sgn
    if 48<=keyCode<58:
        chrg = keyCode-47
    elif keyCode ==16:
        cmove = False
    elif keyCode in massKeys:
        mss = 2+massKeys.index(keyCode)
    elif keyCode ==88:
        sgn = -1
def keyReleased():
    global chrg,cmove,mss,sgn
    if 48<=keyCode<58:
        chrg = 0
    elif keyCode ==16:
        print(5)
        cmove = True
    elif keyCode in massKeys:
        mss = 1
    elif keyCode ==88:
        sgn = 1
