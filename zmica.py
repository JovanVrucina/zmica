#Zmica je zapravo blockchain ako malo bolje razmislis
import pygame as pg
import random
from collections import namedtuple

pg.init()
#Izvinjavam se u napred za ovaj font, bilo je jace od mene
FONT = 	pg.font.Font("Zmijca/BillionStars_PersonalUse.ttf", 50)

#definise se levo desno gore dole kao brojevi
LEVO = 1
DESNO = 2
GORE = 3
DOLE = 4

#struct za koordinate delova tela zmice
blok = namedtuple("blok", ['x', 'y'])

#Konstante
BIOLOSKI_MINIMUM = 25 #Velicina u pikselima osnovne jedinice gradje i funkcije zmice
SPIDOVINA = 15 #brzina takta
#Ovo su konstante za boje
FOREST_GREEN = (0,77,13)
ISLAMIC_GREEN = (0,153,25)
ELECTRIC_GREEN = (0, 255, 42)
WHITE = (255, 255, 255)

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
		self.takt = pg.time.Clock()

		#inicijalizacija pozicije zmice
		self.smer = DESNO
		self.glava = blok(self.SIRINA/2, self.DUZINA/2)
		self.telo = [self.glava, blok(self.glava.x-BIOLOSKI_MINIMUM, self.glava.y), blok((self.glava.x-(BIOLOSKI_MINIMUM*2)), self.glava.y)]
		
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
	def refreshUI(self):
		self.display.fill(FOREST_GREEN)
	
		for point in self.telo:
			pg.draw.rect(self.display, ISLAMIC_GREEN, pg.Rect(point.x, point.y, BIOLOSKI_MINIMUM, BIOLOSKI_MINIMUM))

		pg.draw.rect(self.display, ELECTRIC_GREEN, pg.Rect(self.hrana.x, self.hrana.y, BIOLOSKI_MINIMUM, BIOLOSKI_MINIMUM))
		
		skor = FONT.render("Bodovi: " + str(self.bodovi), True, WHITE)
		self.display.blit(skor, [5,5])
		pg.display.flip()

	#ovde ce se nalaziti korak igrice kada clock tickuje
	def korak(self):
		self.refreshUI()
		self.takt.tick(SPIDOVINA)

		kraj_igre = False
		return kraj_igre


#glavni game loop, tu je ono turbo
igrica = zmijca()
igrica.inicijalizacija()

while True:
	kraj_igre = igrica.korak()
	igrica.korak()
	if kraj_igre:
		break;

print("Bratski, izgubio si!")