from tkinter import *
#Emma: import du package pour régler les chronos
import datetime 

#Emma: demander les noms d'utilisateurs
def demande(question):
	reponse=input(question)
	while len(reponse)<1 or len(reponse)>10:
		if len(reponse)>10:
			print("Donnez un nom de moins de 10 caractères")
		if len(reponse)<1:
			print("Donnez un nom plus long")
		reponse=input(question)
	return reponse
	
nomBlanc=demande("Quel est le nom du joueur des pions blancs ?  ")
nomNoir=demande("Quel est le nom du joueur des pions noirs ?  ")

fen=Tk()
fen.title("Jeu de Dames de Léo Flandin et Emma Desté")
#Emma: adaptation à la taille de mon écran
c=Canvas(fen, height=960,width=1000,bg='white')
#Emma: utilisation de rowspan pour placer plusieurs chronomètres à côté du damier
c.grid(row=0,rowspan=7,column=0)


#Pion =======================
Pion_x=0
xx=0
yy=0
Pion_y=0
pionB= PhotoImage(file="pion_blanc.png")
pionN= PhotoImage(file="pion_noir.png")
pionblanc=0
pionnoir=0
g=False
turn=1
ligneliste=0
carreauxliste=[]
pionblanc=[]
pionnoir=[]
vg=True
Pionjouer=True
allier=False
verif=[]

pionb1=""
pionb2=""
pionb3=""
pionb4=""
pionb5=""
pionb6=""
pionb7=""
pionb8=""
pionb9=""
pionb10=""
pionb11=""
pionb12=""
pionb13=""
pionb14=""
pionb15=""
pionb16=""
pionb17=""
pionb18=""
pionb19=""
pionb20=""

pionn1=""
pionn2=""
pionn3=""
pionn4=""
pionn5=""
pionn6=""
pionn7=""
pionn8=""
pionn9=""
pionn10=""
pionn11=""
pionn12=""
pionn13=""
pionn14=""
pionn15=""
pionn16=""
pionn17=""
pionn18=""
pionn19=""
pionn20=""



crochet=0


ligne=0

paire= True
nbdecase=0

def pion():
	global pionb1,pionb2,pionb3,pionb4,pionb5,pionb6,pionb7,pionb8,pionb9,pionb10,pionb11,pionb12,pionb13,pionb14,pionb15,pionb16,pionb17,pionb18,pionb19,pionb20,pionblanc
	global pionn1,pionn2,pionn3,pionn4,pionn5,pionn6,pionn7,pionn8,pionn9,pionn10,pionn11,pionn12,pionn13,pionn14,pionn15,pionn16,pionn17,pionn18,pionn19,pionn20,pionnoir
	
	pionb1=c.create_image(250,250,image=pionB,anchor=NW)
	pionblanc+=[[250,250]]
	pionb2=c.create_image(390,250,image=pionB,anchor=NW)
	pionblanc+=[[390,250]]
	pionb3=c.create_image(530,250,image=pionB,anchor=NW)
	pionblanc+=[[530,250]]
	pionb4=c.create_image(670,250,image=pionB,anchor=NW)
	pionblanc+=[[670,250]]
	pionb5=c.create_image(810,250,image=pionB,anchor=NW)
	pionblanc+=[[810,250]]
	pionb6=c.create_image(320,320,image=pionB,anchor=NW)
	pionblanc+=[[320,320]]
	pionb7=c.create_image(460,320,image=pionB,anchor=NW)
	pionblanc+=[[460,320]]
	pionb8=c.create_image(600,320,image=pionB,anchor=NW)
	pionblanc+=[[600,320]]
	pionb9=c.create_image(740,320,image=pionB,anchor=NW)
	pionblanc+=[[740,320]]
	pionb10=c.create_image(880,320,image=pionB,anchor=NW)
	pionblanc+=[[880,320]]
	pionb11=c.create_image(250,390,image=pionB,anchor=NW)
	pionblanc+=[[250,390]]
	pionb12=c.create_image(390,390,image=pionB,anchor=NW)
	pionblanc+=[[390,390]]
	pionb13=c.create_image(530,390,image=pionB,anchor=NW)
	pionblanc+=[[530,390]]
	pionb14=c.create_image(670,390,image=pionB,anchor=NW)
	pionblanc+=[[670,390]]
	pionb15=c.create_image(810,390,image=pionB,anchor=NW)
	pionblanc+=[[810,390]]
	pionb16=c.create_image(320,460,image=pionB,anchor=NW)
	pionblanc+=[[320,460]]
	pionb17=c.create_image(460,460,image=pionB,anchor=NW)
	pionblanc+=[[460,460]]
	pionb18=c.create_image(600,460,image=pionB,anchor=NW)
	pionblanc+=[[600,460]]
	pionb19=c.create_image(740,460,image=pionB,anchor=NW)
	pionblanc+=[[740,460]]
	pionb20=c.create_image(880,460,image=pionB,anchor=NW)
	pionblanc+=[[880,460]]


	pionn1=c.create_image(250,670,image=pionN,anchor=NW)
	pionnoir+=[[250,670]]
	pionn2=c.create_image(390,670,image=pionN,anchor=NW)
	pionnoir+=[[390,670]]
	pionn3=c.create_image(530,670,image=pionN,anchor=NW)
	pionnoir+=[[530,670]]
	pionn4=c.create_image(670,670,image=pionN,anchor=NW)
	pionnoir+=[[670,670]]
	pionn5=c.create_image(810,670,image=pionN,anchor=NW)
	pionnoir+=[[810,670]]
	pionn6=c.create_image(320,740,image=pionN,anchor=NW)
	pionnoir+=[[320,740]]
	pionn7=c.create_image(460,740,image=pionN,anchor=NW)
	pionnoir+=[[460,740]]
	pionn8=c.create_image(600,740,image=pionN,anchor=NW)
	pionnoir+=[[600,740]]
	pionn9=c.create_image(740,740,image=pionN,anchor=NW)
	pionnoir+=[[740,740]]
	pionn10=c.create_image(880,740,image=pionN,anchor=NW)
	pionnoir+=[[880,740]]
	pionn11=c.create_image(250,810,image=pionN,anchor=NW)
	pionnoir+=[[250,810]]
	pionn12=c.create_image(390,810,image=pionN,anchor=NW)
	pionnoir+=[[390,810]]
	pionn13=c.create_image(530,810,image=pionN,anchor=NW)
	pionnoir+=[[530,810]]
	pionn14=c.create_image(670,810,image=pionN,anchor=NW)
	pionnoir+=[[670,810]]
	pionn15=c.create_image(810,810,image=pionN,anchor=NW)
	pionnoir+=[[810,810]]
	pionn16=c.create_image(320,880,image=pionN,anchor=NW)
	pionnoir+=[[320,880]]
	pionn17=c.create_image(460,880,image=pionN,anchor=NW)
	pionnoir+=[[460,880]]
	pionn18=c.create_image(600,880,image=pionN,anchor=NW)
	pionnoir+=[[600,880]]
	pionn19=c.create_image(740,880,image=pionN,anchor=NW)
	pionnoir+=[[740,880]]
	pionn20=c.create_image(880,880,image=pionN,anchor=NW)
	pionnoir+=[[880,880]]
	majM()



#============================================================================
#liste pion==================================================================

#============================================================================
#def Plateau noir puis blanc puis noir...====================================

def pair(x):
	global ligne
	global nbdecase
	b=nbdecase
	a=ligne
	while a>=0:
		a-=2
	if a==-2:
		vraie= True
	elif a==-1:
		vraie=False
	if vraie== True:
		while b>=0:
			b-=2
		if b==-2:
			paire= True
		else:
			paire=False
	else:
		while b>=0:
			b-=2
		if b==-1:
			paire= False
		else:
			paire=True
	return(paire)

def plateau():
	global ligne,nbdecase, carreauxliste
	carreauxliste=[]
	ligne=0
	nbdecase=0
	x=250
	y=320
	xx=320
	yy=250
	e=0
	for loop in range(109):
		paire=pair(x)
		if e==10:
			y+=70
			yy+=70
			x=250
			xx=320
			e=0
			ligne+=1
		else:
			if paire== True:
				c.create_rectangle(x,y,xx,yy,outline="black",fill="white")
				carreauxliste+=[[x,y]]
				x+=70
				xx+=70
				e+=1
			elif paire== False:
				c.create_rectangle(x,y,xx,yy,outline="black",fill="black")
				x+=70
				xx+=70
				e+=1

		nbdecase+=1


#=============================================================================
#def placement des pions======================================================


#fin placement des pions========================================================

#def bouger les pions Blanc=========================================================



def clique(evt):
#	print(evt.x,evt.y)
	global g,pionblanc,pionnoir,Pion_x,Pion_y,pion,crochet,ligneliste,Pionjouer
	if Pionjouer== True:
		ligneliste=-1
		x=evt.x
		y=evt.y
		a=2
		if turn==1:
			if g == False:
				for sigma in pionblanc:
					ligneliste+=1
					for alpha in sigma:
						if a//2==0:
							a+=1
							Pion_y=alpha
						else:
							a-=1 
							Pion_x=alpha
						if Pion_x-35<=x<=Pion_x+35 and Pion_y-35<=y<=Pion_y+35:
							g=True
							crochet=sigma
							pion=pionbougb()
		else:	
			if g== False:
				for sigma in pionnoir:
					ligneliste+=1
					for alpha in sigma:
						if a//2==0:
							a+=1
							Pion_y=alpha
						else:
							a-=1 
							Pion_x=alpha
						if Pion_x-35<=x<=Pion_x+35 and Pion_y-35<=y<=Pion_y+35:
							g=True
							crochet=sigma
							pion=pionbougn()
	#Emma: ajout de l'instruction dans la zone de texte
	majM()




#fin deplacement pion blanc========================================================
#def deplacement pion noir=========================================================

def pionbougn():
	global pionn1,pionn2,pionn3,pionn4,pionn5,pionn6,pionn7,pionn8,pionn9,pionn10,pionn11,pionn12,pionn13,pionn14,pionn15,pionn16,pionn17,pionn18,pionn19,pionn20
	
	pionbouger=pion
	a=False
	while a==False:
		if crochet == c.coords(pionn1):
			pionbouger=pionn1
			a=True
		elif crochet == c.coords(pionn2):
			pionbouger=pionn2
			a=True
		elif crochet == c.coords(pionn3):
			pionbouger=pionn3
			a=True
		elif crochet == c.coords(pionn4):
			pionbouger=pionn4
			a=True
		elif crochet == c.coords(pionn5):
			pionbouger=pionn5
			a=True
		elif crochet == c.coords(pionn6):
			pionbouger=pionn6
			a=True
		elif crochet == c.coords(pionn7):
			pionbouger=pionn7
			a=True
		elif crochet == c.coords(pionn8):
			pionbouger=pionn8
			a=True
		elif crochet == c.coords(pionn9):
			pionbouger=pionn9
			a=True
		elif crochet == c.coords(pionn10):
			pionbouger=pionn10
			a=True
		elif crochet == c.coords(pionn11):
			pionbouger=pionn11
			a=True
		elif crochet == c.coords(pionn12):
			pionbouger=pionn12
			a=True
		elif crochet == c.coords(pionn13):
			pionbouger=pionn13
			a=True
		elif crochet == c.coords(pionn14):
			pionbouger=pionn14
			a=True
		elif crochet == c.coords(pionn15):
			pionbouger=pionn15
			a=True
		elif crochet == c.coords(pionn16):
			pionbouger=pionn16
			a=True
		elif crochet == c.coords(pionn17):
			pionbouger=pionn17
			a=True
		elif crochet == c.coords(pionn18):
			pionbouger=pionn18
			a=True
		elif crochet == c.coords(pionn19):
			pionbouger=pionn19
			a=True
		elif crochet == c.coords(pionn20):
			pionbouger=pionn20
			a=True
	return(pionbouger)

def pionbougb():
	global pionb1,pionb2,pionb3,pionb4,pionb5,pionb6,pionb7,pionb8,pionb9,pionb10,pionb11,pionb12,pionb13,pionb14,pionb15,pionb16,pionb17,pionb18,pionb19,pionb20
	global pionn1,pionn2,pionn3,pionn4,pionn5,pionn6,pionn7,pionn8,pionn9,pionn10,pionn11,pionn12,pionn13,pionn14,pionn15,pionn16,pionn17,pionn18,pionn19,pionn20
	
	pionbouger=pion
	a=False
	while a==False:
		if crochet == c.coords(pionb1):
			pionbouger=pionb1
			a=True
		elif crochet == c.coords(pionb2):
			pionbouger=pionb2
			a=True
		elif crochet == c.coords(pionb3):
			pionbouger=pionb3
			a=True
		elif crochet == c.coords(pionb4):
			pionbouger=pionb4
			a=True
		elif crochet == c.coords(pionb5):
			pionbouger=pionb5
			a=True
		elif crochet == c.coords(pionb6):
			pionbouger=pionb6
			a=True
		elif crochet == c.coords(pionb7):
			pionbouger=pionb7
			a=True
		elif crochet == c.coords(pionb8):
			pionbouger=pionb8
			a=True
		elif crochet == c.coords(pionb9):
			pionbouger=pionb9
			a=True
		elif crochet == c.coords(pionb10):
			pionbouger=pionb10
			a=True
		elif crochet == c.coords(pionb11):
			pionbouger=pionb11
			a=True
		elif crochet == c.coords(pionb12):
			pionbouger=pionb12
			a=True
		elif crochet == c.coords(pionb13):
			pionbouger=pionb13
			a=True
		elif crochet == c.coords(pionb14):
			pionbouger=pionb14
			a=True
		elif crochet == c.coords(pionb15):
			pionbouger=pionb15
			a=True
		elif crochet == c.coords(pionb16):
			pionbouger=pionb16
			a=True
		elif crochet == c.coords(pionb17):
			pionbouger=pionb17
			a=True
		elif crochet == c.coords(pionb18):
			pionbouger=pionb18
			a=True
		elif crochet == c.coords(pionb19):
			pionbouger=pionb19
			a=True
		elif crochet == c.coords(pionb20):
			pionbouger=pionb20
			a=True
	return(pionbouger)



					
def bouge(evt):
	global Pion_x,Pion_y,g,x,y,pion,vg,allier
	pion_y=0
	pion_x=0
	if g == True :
		if 250<evt.x<1000 and 250<evt.y<1000: 
			c.coords(pion,evt.x,evt.y)
	if vg== False :
		c.coords(pion,Pion_x,Pion_y)
		vg=True
	elif allier==True:
		pion_x=crochet[0]
		pion_y=crochet[1]
		print(pion_x,pion_y)
		c.coords(pion,pion_x,pion_y)
		allier=False
		g=False
					

def clique2(evt):
	global x,y,g,Pion_x,Pion_y,turn,pionblanc,pionnoir,xx,yy,vg,Pionjouer,allier,verif
	print("crochet :",crochet)
	if Pionjouer==True:
		xx=evt.x
		yy=evt.y
#		print(carreauxliste)
		o=[]
		b=[]
		xg=0
		carreauxlist=carreauxblanc2()
		yg=0
		a=0
		for i in carreauxlist:
			a+=1
			if crochet == i:
	
				if turn==1:
					if crochet[1]==250 or crochet[1]== 390 or crochet[1]==530 or crochet[1]== 670 or crochet[1]==810:
						b=carreauxlist[a+4]
						o=carreauxlist[a+3]
					else:
						b=carreauxlist[a+5]
						o=carreauxlist[a+4]
				else:
					if crochet[1]==880 or crochet[1]== 740 or crochet[1]==600 or crochet[1]== 460 or crochet[1]== 320:
						b=carreauxlist[a-5]
						o=carreauxlist[a-6]
					else:
						b=carreauxlist[a-7]
						o=carreauxlist[a-6]
	
		verif=verify()
		Pion_x=verif[0]
		Pion_y=verif[1]
#		print("o",o,"b",b,"verif",verif,crochet)
		if verif==o:
			pionallier = pionallie()
			if pionallier==False:
				g=False
				vg=False
				Pionjouer=False
			elif pionallier==True:
				allier=True
		elif verif==b:
			pionallier = pionallie()
			if pionallier==False:
				g=False
				vg=False
				Pionjouer=False
			elif pionallier==True:
				allier=True
		else:
			g=True
			vg=True
	#Emma: ajout de l'instruction dans la zone de texte
	majM()




def verifx():
	xg=0
	if 250<=xx<320:
		xg=250
	elif 320<=xx<390:
		xg=320
	elif 390<=xx<460:
		xg=390
	elif 460<=xx<530:
		xg=460
	elif 530<=xx<600 :
		xg=530
	elif 600<=xx<670:
		xg=600
	elif 670<=xx<740:
		xg=670	
	elif 740<=xx<810:
		xg=740
	elif 810<=xx<880:
		xg=810
	elif 880<=xx<950:
		xg=880

	return(xg)
		
def verify():
	c=verifx()	
	yg=0
	
	if 250<=yy<320:
		yg=250
	elif 320<=yy<390:
		yg=320
	elif 390<=yy<460:
		yg=390
	elif 460<=yy<530:
		yg=460
	elif 530<=yy<600:
		yg=530
	elif 600<=yy<670:
		yg=600
	elif 670<=yy<740:
		yg=670
	elif 740<=yy<810 :
		yg=740
	elif 810<=yy<880:
		yg=810
	elif 880<=yy:
		yg=880
	a=[c,yg]
	return(a)
	

def carreauxblanc2():
	carreauxlist=[]
	x=250
	y=250
	for loop in range (50):
		if x==880:
			carreauxlist+=[[x,y]]
			x=250
			y+=70
		elif x==810:
			carreauxlist+=[[x,y]]
			x=320
			y+=70
		else :
			carreauxlist+=[[x,y]]
			x+=140
	return(carreauxlist)

def pionallie():
	global pionn1,pionn2,pionn3,pionn4,pionn5,pionn6,pionn7,pionn8,pionn9,pionn10,pionn11,pionn12,pionn13,pionn14,pionn15,pionn16,pionn17,pionn18,pionn19,pionn20
	global turn, verif
	a=False
	print(verif)
	if turn==1:
		a=False
		if verif == c.coords(pionb1):
			a=True
		elif verif == c.coords(pionb2):
			a=True
		elif verif == c.coords(pionb3):
			a=True
		elif verif == c.coords(pionb4):
			a=True
		elif verif == c.coords(pionb5):
			a=True
		elif verif == c.coords(pionb6):
			a=True
		elif verif == c.coords(pionb7):
			a=True
		elif verif == c.coords(pionb8):
			a=True
		elif verif == c.coords(pionb9):
			a=True
		elif verif == c.coords(pionb10):
			a=True
		elif verif == c.coords(pionb11):
			a=True
		elif verif == c.coords(pionb12):
			a=True
		elif verif == c.coords(pionb13):
			a=True
		elif verif == c.coords(pionb14):
			a=True
		elif verif == c.coords(pionb15):
			a=True
		elif verif == c.coords(pionb16):
			a=True
		elif verif == c.coords(pionb17):
			a=True
		elif verif == c.coords(pionb18):
			a=True
		elif verif == c.coords(pionb19):
			a=True
		elif verif == c.coords(pionb20):
			a=True
	else :
		if verif == c.coords(pionn1):
			a=True
		elif verif == c.coords(pionn2):
			a=True
		elif verif == c.coords(pionn3):
			a=True
		elif verif == c.coords(pionn4):
			a=True
		elif verif == c.coords(pionn5):
			a=True
		elif verif == c.coords(pionn6):
			a=True
		elif verif == c.coords(pionn7):
			a=True
		elif verif == c.coords(pionn8):
			a=True
		elif verif == c.coords(pionn9):
			a=True
		elif verif == c.coords(pionn10):
			a=True
		elif verif == c.coords(pionn11):
			a=True
		elif verif == c.coords(pionn12):
			a=True
		elif verif == c.coords(pionn13):
			a=True
		elif verif == c.coords(pionn14):
			a=True
		elif verif == c.coords(pionn15):
			a=True
		elif verif == c.coords(pionn16):
			a=True
		elif verif == c.coords(pionn17):
			a=True
		elif verif == c.coords(pionn18):
			a=True
		elif verif == c.coords(pionn19):
			a=True
		elif verif == c.coords(pionn20):
			a=True
	return(a)
	

def debut():
	plateau()
	pion()

def Tour():
	global turn, Pionjouer
	if turn==1:
		turn+=1
		pionblanc.pop(ligneliste)
		pionblanc.insert(ligneliste,[Pion_x,Pion_y])
		Pionjouer=True
	else :
		turn-=1
		pionnoir.pop(ligneliste)
		pionnoir.insert(ligneliste,[Pion_x,Pion_y])
		Pionjouer=True
	#Emma: ajout de l'instruction dans la zone de texte
	majM()
	
	
#Emma: instructions pour le joueur 
def majM1():
	"""Fonction qui met à jour la zone de texte pour indiquer les instructions à suivre pour jouer"""	
	global nbdecase,g,Pionjouer
	global message1
	if nbdecase<=0:
		message=listTradClicJouer[nLangue]
	elif Pionjouer==False:
		message=listTradFin[nLangue]
	elif g==False:
		if turn==1:
			message=listTradClicPionB[nLangue]
		elif turn==2:
			message=listTradClicPionN[nLangue]
	elif g==True:
		message=listTradDoubleClic[nLangue]
	else:
		message="error 407"
	message1.set(message)
	
#Emma: instructions pour le joueur avec son nom	
def majM2():
	"""Fonction qui met à jour la zone de texte pour indiquer si c'est aux pions noirs ou aux pions noirs de jouer"""
	global turn, nbdecase
	global message2
	if nbdecase<=0:
		message=""
	elif turn==1:
		message=listTradTourDe[nLangue]+nomBlanc+listTradDeJouer[nLangue]
	elif turn==2:
		message=listTradTourDe[nLangue]+nomNoir+listTradDeJouer[nLangue]
	else:
		message="error 404"
	message2.set(message)
	
#Emma
def majChrono():
	"""Calcul et Affichage des quatre valeurs des chronomètres"""
	global oldnbdecase,oldturn,partieEnCours,heureDebutCoup,dureeTotaleBlanc,dureeTotaleNoir
	heureActuelle=datetime.datetime.now()
	if oldnbdecase<=0 and nbdecase>0:
		heureDebutCoup=heureActuelle
		partieEnCours=True
	if partieEnCours:
		dureeCoupActuel=(heureActuelle-heureDebutCoup).total_seconds()
		if turn==1:
			s=str(dureeCoupActuel)[:6]+" s"
			textChrono1.set(s)
			textChrono2.set("")
		if turn==2:
			s=str(dureeCoupActuel)[:6]+" s"
			textChrono1.set("")
			textChrono2.set(s)
		if oldturn!=turn:
			heureDebutCoup=heureActuelle
			if oldturn==1:
				dureeTotaleBlanc+=dureeCoupActuel
				s=str(dureeTotaleBlanc)+" s"
				textChrono3.set(s)
			if oldturn==2:
				dureeTotaleNoir+=dureeCoupActuel
				s=str(dureeTotaleNoir)+" s"
				textChrono4.set(s)
				
	oldnbdecase=nbdecase
	oldturn=turn
	

#Emma
def majM():
	"""Mise à jour de l'ensemble des Labels: au tour de quel joueur est-ce de jouer, sur quel bouton appuyer, chronometre..."""
	global c
	majM1()
	majM2()
	majChrono()
	c.after(100,majM)
	
def majTextJouer():
	"""Mise à jour du texte du bouton Jouer"""
	s=listTradJouer[nLangue]
	textJouer.set(s)
	
def majTextQuitter():
	"""Mise à jour du texte du bouton Quitter"""
	s=listTradQuitter[nLangue]
	textQuitter.set(s)
	
def majTextFinTour():
	"""Mise à jour du texte du bouton Fin du Tour"""
	s=listTradFinTour[nLangue]
	textFinTour.set(s)

def majTextes():
	"""Mise à jour des textes des boutons"""
	majTextJouer()
	majTextQuitter()
	majTextFinTour()

def francais():
	"""Traduit les textes en français"""
	global nLangue
	nLangue=0
	majTextes()
	
def english():
	"""Traduit les textes en anglais"""
	global nLangue
	nLangue=1
	majTextes()
	
def deustch():
	"""Traduit les textes en allemand"""
	global nLangue
	nLangue=2
	majTextes()
	
	


#Emma: mémorisation des anciennes valeurs pour déclencher les chronos sur les changements
oldnbdecase=nbdecase
oldturn=turn
heureDebutCoup=0
dureeTotaleBlanc=0.0
dureeTotaleNoir=0.0
partieEnCours=False

c.bind_all('<Button-1>',clique)
c.bind_all ('<Motion>', bouge)
c.bind_all('<Button-3>',clique2) 
#Emma: adaptation au trackpad du Mac qui ne comporte qu'un bouton
c.bind_all('<Double-1>',clique2)


#Emma: ajout des messages dans les différentes langues
nLangue=0
listTradJouer=["Jouer","Play","Spielen"]
listTradQuitter=["Quitter","Leave","Weggehen"]
listTradFinTour=["Fin du Tour","End of the Round","Rundes Ende"]
listTradTourDe=["C'est au tour de ","It's ",""]
listTradDeJouer=[" de jouer"," turn"," ist dran"]
listTradClicJouer=["Cliquer sur le bouton Jouer","Click on the Play button","Klick auf das Spielen Taste"]
listTradFin=["Cliquer sur le bouton Fin du Tour","Click on the button End of the Round","Klick auf Rundes Ende Taste"]
listTradClicPionB=["Cliquer sur un de vos pions blancs","Click on one of your white pawns","Klick auf einer von deinen Weiss Bauer"]
listTradClicPionN=["Cliquer sur un de vos pions noirs","Click on one of your black pawns","Klick auf einer von deinen Schwarz Bauer"]
listTradDoubleClic=["Double cliquer sur la case destination de votre pion","Doucle-click on the destination's square of your pawn","Zweimal-klick auf dein Ziels Feld auf deiner Bauer"]

#Emma: ajout des drapeaux
drapeau0= PhotoImage(file="drapeau_fr.png")
Wdrapeau0=Button(fen,image=drapeau0,command=francais,width=100)
Wdrapeau0.grid(row=0,column=1)
drapeau1= PhotoImage(file="drapeau_en.png")
Wdrapeau1=Button(fen,image=drapeau1,command=english,width=100)
Wdrapeau1.grid(row=0,column=2)
drapeau2= PhotoImage(file="drapeau_de.png")
Wdrapeau2=Button(fen,image=drapeau2,command=deustch,width=100)
Wdrapeau2.grid(row=0,column=3)

#Emma: ajout des chronomètres
titreC1=StringVar()
titreC1.set(nomBlanc)
Wtitre1=Label(fen,textvariable=titreC1,width=7)
Wtitre1.grid(row=3,column=2)
titreC2=StringVar()
titreC2.set(nomNoir)
Wtitre2=Label(fen,textvariable=titreC2,width=7)
Wtitre2.grid(row=3,column=3)
Wtitre0=Label(fen,text="Durées",width=10)
Wtitre0.grid(row=3,column=1)
Wtitre3=Label(fen,text="Coup actuel",width=10)
Wtitre3.grid(row=4,column=1)
Wtitre4=Label(fen,text="Totaux",width=10)
Wtitre4.grid(row=5,column=1)

textChrono1=StringVar()
textChrono1.set(".......")
Wchrono1=Label(fen,textvariable=textChrono1, width=15)
Wchrono1.grid(row=4,column=2)
textChrono2=StringVar()
textChrono2.set(".......")
Wchrono2=Label(fen,textvariable=textChrono2, width=15)
Wchrono2.grid(row=4,column=3)
textChrono3=StringVar()
textChrono3.set("0 s")
Wchrono3=Label(fen,textvariable=textChrono3, width=15)
Wchrono3.grid(row=5,column=2)
textChrono4=StringVar()
textChrono4.set("0 s")
Wchrono4=Label(fen,textvariable=textChrono4, width=15)
Wchrono4.grid(row=5,column=3)

#Emma: création des Labels pour donner les instructions
message1=StringVar()
message1.set("Initialisation en cours")
Wmessage1=Label(fen,textvariable=message1,width=40)
Wmessage1.grid(row=7,column=0)

message2=StringVar()
message2.set("Initialisation en cours")
Wmessage2=Label(fen,textvariable=message2,width=40)
Wmessage2.grid(row=7,column=1,columnspan=3)

textFinTour=StringVar()
textFinTour.set("")
Wtour=Button(fen,textvariable=textFinTour,command=Tour,width=12)
Wtour.grid(row=8,column=1,columnspan=3)

textJouer=StringVar()
textJouer.set("")
Winterrupteur=Button(fen,textvariable=textJouer,command=debut,width=12)
Winterrupteur.grid(row=8,column=0,)

textQuitter=StringVar()
textQuitter.set("")
Wquitter=Button(fen,textvariable=textQuitter,command=fen.quit)  
Wquitter.grid(row=9,column=0) 
english() #pour définir l'anglais comme langage par défaut
fen.mainloop()
