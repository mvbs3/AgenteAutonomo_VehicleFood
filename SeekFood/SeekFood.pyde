# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from food import Food

def setup():
    global v
    global f
    global fonte
    size(640, 360)
    v = Vehicle(width / 2, height / 2)
    f = Food()
    fonte = createFont("Arial",30,True)
    
def draw():
    background(51)
    f.display()
    textFont(fonte,40)
    text(str(f.score),20,40)
    v.arrive(f.position)
    f.atualiza(v.position)
    
    v.update()
    v.display()
