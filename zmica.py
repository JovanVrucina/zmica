#Zmica je zapravo blockchain ako malo bolje razmislis
import pygame as pg
import random
from collections import namedtuple

pg.init()
#Izvinjavam se u napred za ovaj font, bilo je jace od mene
FONT = 	pg.font.Font("Zmijca/Z003-MediumItalic.otf", 32)

#definise se levo desno gore dole kao brojevi
LEVO = 1
DESNO = 2
GORE = 3
DOLE = 4

#struct za koordinate delova tela zmice
blok = namedtuple("blok", ['x', 'y'])

while(True):
	dips = int(input("1 - Sporije\n2 - Brzina\n Vas unos: "))
	if dips==1:
		SPIDOVINA = 8
		break
	elif dips==2:
		SPIDOVINA = 16
		break

#Konstante
BIOLOSKI_MINIMUM = 16 #Velicina u pikselima osnovne jedinice gradje i funkcije zmice
#Ovo su konstante za boje
FOREST_GREEN = (0,77,13)
ISLAMIC_GREEN = (0,153,25)
ELECTRIC_GREEN = (0, 255, 42)
WHITE = (255, 255, 255)

#klasa igre
class zmijca:
	#konstruktor manje vise
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
			#Oca formula je potrebna da bi se hrana mogla generisati na koordinatima po kojim zmija moze da se nalazi
			x = random.randint(BIOLOSKI_MINIMUM, (self.SIRINA-BIOLOSKI_MINIMUM)//BIOLOSKI_MINIMUM)*BIOLOSKI_MINIMUM
			y = random.randint(BIOLOSKI_MINIMUM, (self.DUZINA-BIOLOSKI_MINIMUM)//BIOLOSKI_MINIMUM)*BIOLOSKI_MINIMUM
			self.hrana = blok(x, y)
			if self.hrana in self.telo:
				continue
			break

	def refreshUI(self): #refreshUI se pokrece svakim radnim taktom igrice
		self.display.fill(FOREST_GREEN)

		#iscrtuje na ekran celo telo zmijce u blokvima
		for point in self.telo:
			pg.draw.rect(self.display, ISLAMIC_GREEN, pg.Rect(point.x, point.y, BIOLOSKI_MINIMUM, BIOLOSKI_MINIMUM))

		#iscrtuje na ekranu hranu za zmijcu na nasumicnoj koordinati na ekranu
		pg.draw.rect(self.display, ELECTRIC_GREEN, pg.Rect(self.hrana.x, self.hrana.y, BIOLOSKI_MINIMUM, BIOLOSKI_MINIMUM))
		
		#ovo prikazuje tekst na ekranu sa brojem bodova
		skor = FONT.render("Bodovi: " + str(self.bodovi), True, WHITE)
		self.display.blit(skor, [5,5])
		pg.display.flip()

	#funkcija za pomeranje
	def mrdaj(self, smer):
		x = self.glava.x
		y = self.glava.y

		if smer == DESNO:
			x += BIOLOSKI_MINIMUM
		elif smer == LEVO:
			x -= BIOLOSKI_MINIMUM
		elif smer == GORE:
			y -= BIOLOSKI_MINIMUM
		elif smer == DOLE:
			y += BIOLOSKI_MINIMUM

		self.glava = blok(x, y) #menja poziciju glave
	
	def kolizija(self):
		if self.glava.x > self.SIRINA-BIOLOSKI_MINIMUM or self.glava.x <0 or self.glava.y > self.DUZINA-BIOLOSKI_MINIMUM or self.glava.y < 0:
			return True
		elif self.glava in self.telo[1:]:
			return True
		else:
			return False

	#ovde ce se nalaziti korak igrice kada clock tickuje
	def korak(self):
		#ovde program slusa za tipke stisnute na tastaturi (Strelice)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit() #Handluje onaj iksic na prozoru
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					self.smer = LEVO
				elif event.key == pg.K_RIGHT:
					self.smer = DESNO
				elif event.key == pg.K_UP:
					self.smer = GORE
				elif event.key == pg.K_DOWN:
					self.smer = DOLE

		self.mrdaj(self.smer)
		self.telo.insert(0, self.glava)

		if self.kolizija():
			kraj_igre = True
			return kraj_igre

		elif self.glava == self.hrana:
			self.bodovi+= 1
			self.generisatiHranu()

		else:
			self.telo.pop()
        
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

print("Bratski, izgubio si!\nFinalni broj bodova: ", igrica.bodovi)