homes = []

class Home(object):
    building = []
    allx = 0
    ally = 0
    street = False

    def __init__(self, constructions):
        self.building = constructions
        self.posCount()
        
        homes.append(self)

    def __repr__(self):
        if self.street:
            return "Street"

        else:
            return "Home at ({}, {})".format(self.allx, self.ally)

    def expand(newConstructions):
        self.building.append(newConstructions)

        self.allx = 0
        self.ally = 0
        self.posCount()

    def posCount(self):
        try:
            for i in self.building:
                self.allx += i.posX
                self.ally += i.posY

            self.allx /= len(self.building)
            self.ally /= len(self.building)

        except:
            self.street = True

            self.allx = 0
            self.ally = 0

class Wall(object):
	angle = 0
	posX = 0
	posY = 0
	width = 0
	length = 0
	height = 0

	def __init__(self, nAngle, nPosX, nPosY, nWidth, nLength, nHeight):
		self.angle = nAngle
		self.posX = nPosX
		self.posY = nPosY
		self.width = nWidth
		self.length = nLength
		self.height = nHeight
		
	def __repr__(self):
		return "Wall at ({}, {})".format(self.posX, self.posY)

	def getFullInf(self):
		return "{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n".format("Angle",
                                                                         self.angle,
                                                                         "X coordinate",
																		 self.posX,
                                                                         "Y coordinate",
                                                                         self.posY,
                                                                         "Width",
                                                                         self.width,
                                                                         "Length",
                                                                         self.length,
                                                                         "Height",
                                                                         self.height)

noHome = Home(constructions = [])
