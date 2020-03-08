homes = []

class Home(object):
	building = []

	def __init__(self, constructions):
		self.building = constructions
        homes.append(self)

	def __repr__(self):
		return str(self.building)

	def expand(newConstructions):
		self.building.append(newConstructions)

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
