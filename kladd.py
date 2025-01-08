def serielån(månedlig_innbetaling, rente, gjenværende_hovedstol): #antar at rente er rentesatsen i desimaltall
    rente_beløp = gjenværende_hovedstol * rente / 12
    avdrag = månedlig_innbetaling - rente_beløp #antar månedlig innbetaling = rente + avdrag
    gjenværende_hovedstol -= avdrag
    return gjenværende_hovedstol

print(serielån(2083.34, 0.05, 100000))

def måneder(lånebeløp,månedlig_avdrag,rente):
    måned = 0
    gjenværende_hovedstol = lånebeløp
    månedlig_innbetaling = månedlig_avdrag + rente * gjenværende_hovedstol

    while gjenværende_hovedstol > 0:

        if gjenværende_hovedstol < månedlig_avdrag:
            return måned

        else:
            gjenværende_hovedstol = serielån(månedlig_innbetaling, rente, gjenværende_hovedstol)
        
        måned += 1
    

print(måneder(100000,1667,0.05))