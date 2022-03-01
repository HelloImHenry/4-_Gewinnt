import ZeichenProzesse
class Feld:
    #Initzialisiert das Spielfeld und füllt es mit leeren Feldern, in diesem Fall 0
    def __init__(self):
        self.zeichner = ZeichenProzesse.Zeichne()
        #Die Erste Koordinate ist y und die zweite ist x
        self.feldPositionen = []
        for y in range(6):
            self.feldPositionen.append([0,0,0,0,0,0,0])
    #Wendet die Physik auf die Spielfiguren an, damit sie immer nach unten Fallen
    def Physik(self,posX,spieler):
        derzeitigePosition = 5
        #Die Figur wird so lange nach unten verschoben bis das Feld darunter entweder nicht frei, oder außerhalb des Spielfeld ist.
        while self.feldPositionen[derzeitigePosition][(posX)] == 0 and derzeitigePosition != -1:
            derzeitigePosition-=1
        #Daher das immer das darunterliegende Feld geprüft wird muss es anschließend eines nach Oben verschoben werden damit man die wirkliche freie Position erhält.
        derzeitigePosition+=1
        self.feldPositionen[derzeitigePosition][posX] = spieler        
        return derzeitigePosition
    #Ermittelt Falls mögliche den Gewinner oder ein Unentschieden
    def FigurenInReihePrüfung(self,pos,spieler):
        #Enthält die maximale Anzahl von Figuren in der Reihe. Wenn der Wert 4 ist hat ein Spieler im übrigen gewonnen.
        maxFiguren = 0
        #Die x und Y Position die gerade überprüft wird,
        derzeitigesX, derzeitigesY = pos[0],pos[1]
        #Die Figuren, die der Zeit in Reihe sind. Der Wert ist 0, da die Unten stehende Schleife beim ersten durchlauf die neu platzierte Figur bereits berücksichtigt.
        derzeitigeFiguren = 0
        #Enthält die Bewegungen die gemacht werden müssen um die entsprechenden Felder zu überprüfen. [-1,0] überprüft zum Beispiel das Feld Links vom derzeitigen.
        #Ein anderes Beispiel ist [-1,-1]. Es prüft das Feld oben Links.
        operationsListe = [[-1,0],[+1,0],[0,-1],[0,+1],[-1,-1],[-1,+1],[+1,-1],[+1,+1]]
        #Es wird durch jedes Element der operationsListe geloopt um in jede Richtung nach weiteren Figuren zu suchen.
        for x in range(len(operationsListe)):
            #Es wird so lange nach weiteren Figuren des Spielers gesucht, bis das nächste Feld keine Figur des zu prüfenden Spielers besitzt, oder das Feld auserhalb des Feldes liegt.
            while self.PositionImSpielFeld(derzeitigesX,derzeitigesY) and self.feldPositionen[derzeitigesY][derzeitigesX] == spieler :
                derzeitigeFiguren+=1
                #Das von der Operation in der Liste abhängige nächste Feld wird geprüft.
                derzeitigesX+=operationsListe[x][0]
                derzeitigesY+=operationsListe[x][1]
            #Kleines Beispiel. Das Feld hat wenn es nach Links geht 2 weitere Felder des Spielers (Vorherige Prüfung). -> maxFiguren = 2 
            # Gehst du aber nach oben rechts sind es 3 Weitere felder, also mehr. (Neue Prüfunf) -> maxFiguren = 3 
            if derzeitigeFiguren > maxFiguren:
                maxFiguren = derzeitigeFiguren
            #Es wird die nächste Richtung geprüft und die Werte deshalb auf die Ausgangswerte zurückgesetzt
            derzeitigeFiguren = 0
            derzeitigesX = pos[0]
            derzeitigesY = pos[1]
        return maxFiguren
            
        """------------- Das ist der Code wenn es nach 2 Uhr ist und mann nicht nachdenkt hahahahahaha xd
        #Chech wie viele Figuren Links von dir in der Reihe
        while self.feldPositionen[derzeitigesY][derzeitigesX] == spieler and self.PositionImSpielFeld(derzeitigesX,derzeitigesY):
            derzeitigeFiguren+=1
            derzeitigesX-=1

        derzeitigesX = pos[0]
        derzeitigesY = pos[1]
        if derzeitigeFiguren > maxFiguren:
            maxFiguren = derzeitigeFiguren
        derzeitigeFiguren = 1
        #Chech wie viele Figuren Rechts von dir in der Reihe
        while self.feldPositionen[derzeitigesY][derzeitigesX] == spieler and self.PositionImSpielFeld(derzeitigesX,derzeitigesY):
            derzeitigeFiguren+=1
            derzeitigesX+=1
        
        derzeitigesX = pos[0]
        derzeitigesY = pos[1]
        if derzeitigeFiguren > maxFiguren:
            maxFiguren = derzeitigeFiguren
        derzeitigeFiguren = 1   

        #Chech wie viele Figuren Rechts Unten von der neuen Figur
        while self.feldPositionen[derzeitigesY][derzeitigesX] == spieler and self.PositionImSpielFeld(derzeitigesX,derzeitigesY):
            derzeitigeFiguren+=1
            derzeitigesX+=1
            derzeitigesY+=1
        
        derzeitigesX = pos[0]
        derzeitigesY = pos[1]
        if derzeitigeFiguren > maxFiguren:
            maxFiguren = derzeitigeFiguren
        derzeitigeFiguren = 1 

        #Chech wie viele Figuren Rechts Oben von der neuen Figur
        while self.feldPositionen[derzeitigesY][derzeitigesX] == spieler and self.PositionImSpielFeld(derzeitigesX,derzeitigesY):
            derzeitigeFiguren+=1
            derzeitigesX+=1
            derzeitigesY-=1
        
        derzeitigesX = pos[0]
        derzeitigesY = pos[1]
        if derzeitigeFiguren > maxFiguren:
            maxFiguren = derzeitigeFiguren
        derzeitigeFiguren = 1 

        #Chech wie viele Figuren Unten Links von der neuen Figur
        while self.feldPositionen[derzeitigesY][derzeitigesX] == spieler and self.PositionImSpielFeld(derzeitigesX,derzeitigesY):
            derzeitigeFiguren+=1
            derzeitigesX-=1
            derzeitigesY+=1
        
        derzeitigesX = pos[0]
        derzeitigesY = pos[1]
        if derzeitigeFiguren > maxFiguren:
            maxFiguren = derzeitigeFiguren
        derzeitigeFiguren = 1

        #Chech wie viele Figuren Oben Links von der neuen Figur
        while self.feldPositionen[derzeitigesY][derzeitigesX] == spieler and self.PositionImSpielFeld(derzeitigesX,derzeitigesY):
            derzeitigeFiguren+=1
            derzeitigesX-=1
            derzeitigesY-=1
        
        derzeitigesX = pos[0]
        derzeitigesY = pos[1]
        if derzeitigeFiguren > maxFiguren:
            maxFiguren = derzeitigeFiguren
        derzeitigeFiguren = 1
    """
    #Diese Funktion prüft, ob die Eingegebene Position inerhalb des Spielfeld liegt.
    def PositionImSpielFeld(self,x,y):
        output = True
        if x <= -1 or x >= 7 or y <=-1 or y >= 6:
            output = False
        return output
    #Nimmt als Parameter die MausPosition posX und die Spielfeldgröße X
    def PixelKoordinatenZuFeldPosition(self,posX,sizeX,offsetX):
        #Enthält die Koordinaten ab denen ein neues Feld beginnt. Es wird nur nach x unterschieden, da y irrelevant istz
        pixelPos = []
        #Speichert die derzeitige Position des For Loops. Es wird nicht bei 0 sondern beim Offset gestartet.
        curPixelPos = offsetX
        #Enthält den Rückgabewert, sprich das angeclickte Feld. Wenn der Wert 999 bleibt hat ein Spieler außerhalb des Bildschirm geclickt.
        pos = 999
        for z in range(8):
            pixelPos.append(curPixelPos)
            #/7 Weil es sieben Felder in x gibt.
            curPixelPos=curPixelPos + (sizeX/7)
        for x in range(7):
            if posX >= pixelPos[x] and posX < pixelPos[(x+1)]:
                pos = x
                break
        return pos
    
    def SpalteIstVoll(self,x):
        if self.feldPositionen[5][x] != 0:
            return True
        else:
            return False