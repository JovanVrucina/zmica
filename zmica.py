#Zmica je zapravo blockchain ako malo bolje razmislis
import pygame as pg
import random
from collections import namedtuple

#definise se levo desno gore dole kao brojevi
LEVO = 1
DESNO = 2
GORE = 3
DOLE = 4

#struct za koordinate delova tela zmice
blok = namedtuple('x', 'y')

#Velicina u pikselima osnovne jedinice gradje i funkcije zmice
BIOLOSKI_MINIMUM = 25

#klasa igre
class zmijca:
	#konstruktor kao bajagi
	def inicijalizacija(self, SIRINA=512, DUZINA=512):
		#inicijalizacija ekrana
		self.SIRINA = SIRINA
		self.DUZINA = DUZINA

		self.display = pg.display.set_mode((self.SIRINA, self.DUZINA))
		pg.display.set_caption("Zmijca (ili zmijca, nisam siguran)")
		#radni takt igre 
		self.takt = pg.time.clock()

		#inicijalizacija pozicije zmice
		self.smer = DESNO
		self.glava = (self.SIRINA/2, self.DUZINA/2)
		self.telo = [self.glava, blok(self.glava.x-BIOLOSKI_MINIMUM, self.glava.y), blok(self.glava.x-(BIOLOSKI_MINIMUM*2), self.glava.y)]
		
		#inicijalizacija hrane i bodova
		self.bodovi = 0
		self.hrana = None #none se stavlja tako da to ne bude koordinata (slicano kao NULL pretpostavljam)
		self.generisatiHranu()

	#funkcija za generisanje hrane sa proverom da li je koordinata hrana negde u zmiji
	def generisatiHranu(self):
		while True:
			x = random.randint(2, (self.SIRINA))
			y = random.randint(2, (self.DUZINA))
			self.hrana = blok(x, y)
			if self.hrana in self.telo:
				continue
			break

	#ovde ce se nalaziti korak igrice kada clock tickuje
	def korak(self):
		pass


#glavni game loop, tu je ono turbo
igrica = zmijca()

while True:
	igrica.korak()