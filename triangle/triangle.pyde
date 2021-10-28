p = []
selected = None
class Point:
    def __init__(self):
        self.x = random(width)
        self.y = random(height)
    def show(self):
        point(self.x,self.y)

def setup():
    size(400,500)
    for i in range(3):
        p.append(Point())
    stroke(255)
    strokeWeight(8)
def draw():
    global p
    background(55)
    prev = p[-1]
    sides = []
    for i in p:
        i.show()
        push()
        strokeWeight(3)
        line(i.x,i.y,prev.x,prev.y)
        pop()
        
        prev = i
        
    s = [0,0]
    for i in p:
        s[0]+=i.x/3
        s[1]+=i.y/3
    push()
    stroke(255,90,80)
    point(s[0],s[1])
    pop()
    angles = []
    sides.append(PVector(p[2].x-p[1].x,p[2].y-p[1].y).mag())
    sides.append(PVector(p[2].x-p[0].x,p[2].y-p[0].y).mag())
    sides.append(PVector(p[0].x-p[1].x,p[0].y-p[1].y).mag())
    
    angles.append(PVector.angleBetween(PVector(p[1].x-p[0].x,p[1].y-p[0].y),PVector(p[2].x-p[0].x,p[2].y-p[0].y)))
    angles.append(PVector.angleBetween(PVector(p[0].x-p[1].x,p[0].y-p[1].y),PVector(p[2].x-p[1].x,p[2].y-p[1].y)))
    angles.append(PVector.angleBetween(PVector(p[0].x-p[2].x,p[0].y-p[2].y),PVector(p[1].x-p[2].x,p[1].y-p[2].y)))
    
    orthoc = [0,0]
    d = 0
    for i in range(3):
        d+=tan(angles[i])
        orthoc[0]+=p[i].x*tan(angles[i])
        orthoc[1]+=p[i].y*tan(angles[i])
    orthoc[0]/=d; orthoc[1]/=d
    push()
    stroke(100,255,100)
    point(orthoc[0],orthoc[1])
    pop()
    circum = [0,0]
    d = 0
    for i in range(3):
        d+=sin(2*angles[i])
        circum[0]+=p[i].x*sin(2*angles[i])
        circum[1]+=p[i].y*sin(2*angles[i])
    circum[0]/=d
    circum[1]/=d
    push()
    stroke(100,100,255)
    point(circum[0],circum[1])
    pop()
def mousePressed():
    global selected
    for i in p:
        if dist(mouseX,mouseY,i.x,i.y)<=10:
            selected = i
def mouseDragged():
    global selected
    if selected:
        selected.x = constrain(mouseX,0,width)
        selected.y = constrain(mouseY,0,height)
def mouseReleased():
    global selected
    selected = None
