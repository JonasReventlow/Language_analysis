def showmyname(name):
    print('hej med dig', name)

showmyname('Jonas')


def to_km(mil):
    """ int -> float
    Omregner en værdi i kilometer til dens værdi i miles
    """

    print(mil * 1.6)

    
to_km(26)


def average(a,b,c,d):

    print((a+b+c+d)/4)

average(1,2,3,4)




#forskellen på anvendelse af print og return

def to_celsius(fahrenheit):
    print((fahrenheit - 32.0) * 5 / 9)

    
to_celsius(100)


def to_celsius(fahrenheit):
    """(int)-> float
    returns celsius degree when given a fahrenheit
    """
    
    return round((fahrenheit - 32.0) * 5 / 9,2)

fahrenheit_input = int(input('give me a fahrenheit temp.:'))
#uanset hvor vi bruger input, så vil den lave det om til et string


tempe = to_celsius(fahrenheit_input)

#(husk at python altid konverterer fra top til slut)

print(tempe)
#tempe bliver printet --> tempe er defineret som to_celsius --> to_celsius har
    #argmentet (fahrenheit) --> fahrenheit har en returnfunktion som ligning)

#"print kan kun printe"

#return kan returnerer værdien til funktionskaldet --> der skal der være en
    #varibale til at modtage funktionen





#Definer en funktion som har 4 parametre. Funktionen skal beregne gennemsnittet
    #af de 3 højeste tal
def average(a,b,c,d):
    exclude = min(a,b,c,d)
    total = (a+b+c+d)
    return (total - exclude)/3

maxthree = average(1,2,3,4)

print(maxthree)





