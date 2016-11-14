# -*- coding:Utf-8 -*-
import Tkinter as tk
import tkFileDialog
import tkMessageBox
import os, os.path
import sys
import matplotlib.pyplot as plt
import csv
from obspy.imaging.beachball import Beachball

class drawTheseBeachballs(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.master.title("Draw these beachballs!")
		self.master.columnconfigure(0, weight=1)
		self.master.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.grid(sticky="NSEW")
		self.createWidgets()

	def createWidgets(self):
		#creation des variables
		self.fichierSrc = tk.StringVar()
		self.fichierSrc.set("")
		self.repSave = tk.StringVar()
		self.repSave.set("")
		self.rapport = tk.StringVar()
		self.rapport.set("")
		#creation des widgets
		mainFrame = tk.Frame(self, borderwidth=2, relief="groove")
		mainFrame.columnconfigure(0, weight=1)
		mainFrame.columnconfigure(1, weight=1)
		mainFrame.columnconfigure(2, weight=1)
		
		videLabel0 = tk.Label(mainFrame)
		
		dessinLabel = tk.Label(mainFrame, justify='left', text=" . -- .\n:  \/  :\n . /\ .")
		
		videLabel1 = tk.Label(mainFrame)
		
		entreeLabel = tk.Label(mainFrame, text="CSV file")
		entreeEntry = tk.Entry(mainFrame, width=120, textvariable=self.fichierSrc)
		entreeButton = tk.Button(mainFrame, text="Select", command=lambda: self.ouvrir(self.fichierSrc))
		
		videLabel2 = tk.Label(mainFrame)
		
		saveLabel = tk.Label(mainFrame, text="Output directory")
		saveEntry = tk.Entry(mainFrame, textvariable=self.repSave)
		saveButton = tk.Button(mainFrame, text="Select", command=lambda: self.select_rep(self.repSave))
		
		videLabel3 = tk.Label(mainFrame)
		
		#fenetre rapport
		rapportLabel = tk.Label(mainFrame, text="Progress")
		self.texte=tk.Text(mainFrame, width=25, height=1)
		
		videLabel4 = tk.Label(mainFrame)

		button_launch = tk.Button(mainFrame, text="Go! Go! Go!",bg='#66e060', command=self.launch)
		
		quitButton = tk.Button(mainFrame, text="Quit", bg='#f9363d', command=lambda : quit(drawTheseBeachballs))
		
		videLabel5 = tk.Label(mainFrame, text="©0|)é 3|\| 5£!|* ©|-|4|_|5537735", anchor="se")
		
		
		
		#position des widgets
		rowI=0
		mainFrame.grid(column=0, row=rowI, sticky="NSEW")
		
		rowI=rowI+1
		videLabel0.grid(column=0, row=rowI, sticky="EW")
		
		rowI=rowI+1
		dessinLabel.grid(column=1, columnspan=6, row=rowI, sticky="W")
		videLabel3 = tk.Label(mainFrame)
		
		rowI=rowI+1
		videLabel1.grid(column=0, row=rowI, sticky="EW")
		
		rowI=rowI+1
		entreeLabel.grid(column=0, row=rowI, sticky="EW")
		entreeEntry.grid(column=1, columnspan=4, row=rowI, sticky="EW")
		entreeButton.grid(column=5, row=rowI, sticky="NSEW")
		
		rowI=rowI+1
		videLabel2.grid(column=0, row=rowI, sticky="EW")
		
		rowI=rowI+1
		saveLabel.grid(column=0, row=rowI, sticky="EW")
		saveEntry.grid(column=1, columnspan=4, row=rowI, sticky="EW")
		saveButton.grid(column=5, row=rowI, sticky="NSEW")
		
		rowI=rowI+1
		videLabel3.grid(column=0, row=rowI, sticky="EW")
		
		rowI=rowI+1
		rapportLabel.grid(column=0, row=rowI, sticky="EW")
		self.texte.grid(column=1, columnspan=4, row=rowI, sticky="EW")
				
		rowI=rowI+1
		videLabel4.grid(column=0, row=rowI, sticky="EW")
		
		rowI=rowI+1
		button_launch.grid(column=0, columnspan=4, rowspan=2, row=rowI, sticky="NSEW")
		quitButton.grid(column=4, columnspan=2,rowspan=2, row=rowI, sticky="NSEW")
		
		rowI=rowI+2
		videLabel5.grid(column=0, row=rowI, sticky="EW")
		
	def ouvrir(self,fichier) :
		rep = os.path.dirname(sys.argv[0])
		fic = ""
		repfic = tkFileDialog.askopenfilename(title="Select CSV file", initialdir=rep,initialfile=fic, filetypes = [("All", "*"),("CSV","*.csv")]) 
		if len(repfic) > 0:
			rep=os.path.dirname(repfic)
			fic=os.path.basename(repfic)
		fichier.set(repfic)	
  
  	def select_rep(self,repertoire) :
		rep=os.getcwd()
		rep = tkFileDialog.askdirectory(title="Select output directory", initialdir=rep) 
		if len(rep) > 0:
			rep = rep
			os.chdir(rep)
		repertoire.set(rep)
		
	def erreur(self,texte) :
		tkMessageBox.showerror("Error", texte)
		
	def launch(self) :
		if self.fichierSrc.get() == "" :
			self.erreur('Select CSV file')
		elif self.repSave.get() == "" :
			self.erreur('Select output directory')
		else :
			self.draw()
	
	def progress(self,addText) :
		self.texte.insert(tk.END, "\n"+addText)
		self.texte.see(tk.END)
		self.texte.update_idletasks()
  
	def draw(self) :
	
		csvfile = self.fichierSrc.get()
		saveDir = self.repSave.get()

		fichier = open(csvfile)
		fichercsv = csv.reader(fichier, delimiter=' ')
		
		nb_meca = 0
		for var in fichercsv :
			nb_meca = nb_meca+1
		nb_meca = nb_meca-1
		fichier.close()
		
		fichier = open(csvfile)
		fichercsv = csv.reader(fichier, delimiter=' ')
		
		i=1

		for var in fichercsv :
			if i>1 :
				bb=Beachball([float(var[1]),float(var[2]),float(var[3])], size=1, linewidth=2, facecolor='r',outfile=saveDir+'/'+str(var[0])+".svg")
				plt.close("all")
			i=i+1
			self.progress(str(i)+'/'+str(nb_meca))
			
		self.progress("Done")
	
	
if __name__ =='__main__':
	drawTheseBeachballs().mainloop()
