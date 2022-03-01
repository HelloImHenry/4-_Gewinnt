import tkinter
import Spielfeld
import ZeichenProzesse
zeichner = ZeichenProzesse.Zeichne()

feld = Spielfeld.Feld()
fenster = tkinter.Tk()
sizeX = 700
sizeY = 600
offsetY = 100
displayOffset = 10
cv = tkinter.Canvas(fenster,width = sizeX+2*displayOffset, height=(sizeY+offsetY))
cv.pack()
fenster.geometry(str(sizeX+2*displayOffset)+"x"+ str(sizeY+offsetY+displayOffset))
spielerAmZug = 1
spielAktiv = True
zeichner.ZeichneTrennLinien([cv,sizeX,sizeY,displayOffset,offsetY])
#--------------------Spieler drückt Maus Event----------------------------------------------------
def click(event):
    global spielerAmZug
    global spielAktiv
    if spielAktiv:
        posX = event.x
        feldX = feld.PixelKoordinatenZuFeldPosition(posX,sizeX,displayOffset)
        if feldX != 999:
            if feld.SpalteIstVoll(feldX) != True:
                #Physik gibt die neue Y Position zurück
                feldY = feld.Physik(feldX,spielerAmZug)
                #Die Figur wird gezeichnet.
                zeichner.ZeichneFigur(feldX,feldY,spielerAmZug)
                #Es wird geprüft ob ein Spieler gewonnen hat.
                anzahlDerFigurenInReihe = feld.FigurenInReihePrüfung([feldX,feldY],spielerAmZug)
                if anzahlDerFigurenInReihe < 4:
                    if spielerAmZug == 1:
                        spielerAmZug =2
                    else:
                        spielerAmZug = 1
                else:
                    spielAktiv = False
                    print("Spieler " + str(spielerAmZug) + "hat gewonnen!")           
#--------------------------------------------------------------------------------------------------

fenster.bind('<Button-1>',click)
fenster.mainloop()
