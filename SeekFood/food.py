class Food():
    def __init__(self):
        self.score =0
        self.setPosition()
    
    def setPosition(self):
        x = random(width)
        y = random(height)
        self.position = PVector(x,y)
    
    def display(self):
        ellipse(self.position.x,self.position.y,10,10)

    def atualiza(self, posV):
        if abs(posV.x- self.position.x) <= 3 and abs(posV.y- self.position.y) <= 3:
            self.setPosition()
            self.score+=1
