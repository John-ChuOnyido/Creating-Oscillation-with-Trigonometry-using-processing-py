r1 = 300.0
r2 = 61.0
r3 = 5.0
x1 = 0
y1 = 0
prop = 0.9
points = []
t = 0

def setup():
    size(600,600)

def draw():
    global r1,r2,x1,y1,t,prop,points
    translate(width/2, height/2)
    background(255)
    noFill()
    #big circle
    stroke(0)
    ellipse(x1,y1,2*r1, 2*r1)
    
    #small circle
    x2 = (r1-r2)*cos(t)
    y2 = (r1-r2)*sin(t)
    ellipse(x2,y2,2*r2,2*r2)
    
    #drawing dot
    x3 = x2+prop*(r2-r3)*cos(-((r1-r2)/r2)*t)
    y3 = y2+prop*(r2-r3)*sin(-((r1-r2)/r2)*t)
    fill(255,0,0)
    ellipse(x3,y3,2*r3,2*r3)
    
    #add points to list
    points = [[x3,y3]] + points[:2000]
    for i,p in enumerate(points): #go through the points list
        if i < len(points)-1: #up to the next to last point
            stroke(255,0,0) #draw red lines between
            line(p[0],p[1],points[i+1][0],points[i+1][1])
            
    t += 0.05
