#### UTILIZZO

1)	Dal "cerca" lanciare una finestra di prompt col comando cmd
	cambiare il percorso col comando cd C:\Users\nome.cognome\Desktop\Scripts

	Lanciare lo script col comando: py MOS_frame_to_movV06.py
	
	Nel terminale andrà inserito il nome della CARTELLA PRINCIPALE ( PR, CH, FL, BLD, GRD, ENV)

	SE le cartelle SONO TUTTE TUE seleziona T per fare il mov di tutte,   ALTRIMENTI inserisci il nome della cartella della quale fare il mov

	Il/i mov verrano messi in : R:\mini_eroi\Library\MovJpg_Nimbus

	
	NB Finito....
	1) Le cartelle con i render vanno spostate nella cartella __OK__
	2) Il/i mov caricati su nimbus e una volta caricati ... spostati nella cartella PR ( o CH, FL, BLD, GRD, ENV) 









#### PRIMA INSTALLAZIONE ####

1)	installare Python da https://www.python.org/downloads/
	ultima versione Download Python 3.11.1
	selezionare CUSTOMIZE INSTALLATION
	prima finesta di opzioni --> lasciare quelle già presenti 
	next
	seconda finestra di opzioni --> lasciare quelle già presenti e aggiungere ADD PYTHON TO ENVIRONMENT VARIABILES

2) 	Copiare la cartella FFMPEG presente in CODEC sul disco locale C:
	In Cerca cercate e selezionate: Sistema (Pannello di controllo)
	Fate clic sul collegamento Impostazioni di sistema avanzate.
	Fate clic su Variabili di ambiente. ...
	Nella finestra variabili dell'utente...selezionare path e cliccare su modifica
	Nella finestra modifica fare NUOVO e scrivere C:\FFMPEG\bin e dare l'OK

3) 	Creare una cartella Scripts sul desktop e copiarci dentro lo script: frame_to_movV04_autoRemote.py

4) 	Dal "cerca" lanciare una finestra di prompt col comando cmd
	verificare che python e pip siano installati:
	digitare: 		python --version
	dovremmo ottenere:	Python 3.7.3
	digitare: 		pip --version
	dovremmo ottenere:	pip 9.0.1 from c:\users\myname\appdata\local\programs\python\python37\lib\site-packages (python 3.7)
	se tutto ok
	lanciare pip install opencv-python

5)	RIAVVIARE IL PC !!!!



