class Ball:
    def __init__(self,vel,pos):
        self.vel = vel
        self.pos = pos
        self.prev = pos
    def move(self):
        self.vel.y+=g
        self.pos.add(self.vel)
        line(self.pos.x,self.pos.y,self.prev.x,self.prev.y)
        self.prev = self.pos.copy()
        if self.pos.y>=400:
            self.pos.y = 400
            self.vel.y*=-1
        # if self.pos.x>=width:
        #     self.vel.x*=-1
        # elif self.pos.x<=0:
        #     self.vel.x*=-1
        
g = 1
mouseP = None
b = []
def setup():
    global bg
    size(500,500)
    b.append(Ball(PVector(1,-20),PVector(100,400)))
    background(55)
    stroke(255)
    bg = createGraphics(width,height)
    # bg.clear()
def draw():
    fill(55,20)
    strokeWeight(2)
    line(0,400,width,400)
    strokeWeight(5)
    rect(0,0,width,height)
    dels = []
    for i in range(len(b)):
        b[i].move()
        if (b[i].vel.y==0 and b[i].pos.y==400) or b[i].pos.x>width or b[i].pos.x<0: 
            dels.append(i)
    for i in dels:del b[i]
def mousePressed():
    global mouseP
    mouseP = PVector(mouseX,mouseY)
def mouseReleased():
    global mouseP
    if mouseP.y>400:return
    v = PVector.sub(mouseP,PVector(mouseX,mouseY))
    if v.mag()>7:v.setMag(7)
    b.append(Ball(v,mouseP))
    mouseP=None
