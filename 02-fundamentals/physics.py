'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''
import math

EARTH_GRAVITY = 9.80665  # m/s² - normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62      # m/s² - měsíční gravitace
SPEED_OF_LIGHT = 299792458  # m/s - rychlost světla ve vakuu
SPEED_OF_SOUND = 343       # m/s - rychlost zvuku při 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def cas_padu(h, g):
    """
    Spočítá čas pádu tělesa.

    h: Výška pádu v metrech.
    g: Tíhové zrychlení v m/s².

    Returns: Čas pádu v sekundách.
    """
    
    return math.sqrt(2 * h / g)

def vaha_na_planete(hmotnost, g):
    """
    Spočítá váhu tělesa na planetě s daným tíhovým zrychlením.

    hmotnost: Hmotnost tělesa v kilogramech.
    g: Tíhové zrychlení na planetě v m/s².

    Returns: Váha tělesa v newtonech (N).
    """
    return hmotnost / EARTH_GRAVITY * g

def svetlo(metry):
    """
    Vypočítá čas, který světlo potřebuje k překonání dané vzdálenosti.

    metry: Vzdálenost v metrech, kterou má světlo urazit.
    vrací: Čas v sekundách, který světlo potřebuje k překonání zadané vzdálenosti.
    """
    return metry  / SPEED_OF_LIGHT


def zvuk(cas):
    """
    Vypočítá vzdálenost, kterou zvuk urazí za daný čas.
    
    cas: Čas v sekundách (s)
    vrací: Vzdálenost v metrech (m)
    """
    return cas * SPEED_OF_SOUND