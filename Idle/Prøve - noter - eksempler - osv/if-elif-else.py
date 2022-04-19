#if, elif og else

colour = input('what is your favourite colour?')

if colour == 'red':
    print ('I like your taste in colours')
    # to lighedstegn (==) skaber ægvedvalens til colour
    #if gør at hvis man skriver red får man det printede
elif colour == 'white':
    print ('your taste in colours is dull')
    #ligesom elif, men elif er der kun hvis if fejler
else:
    print('your taste in colours is bad')
    #alt andet der bliver skrevet får denne printet besked


#et problem kunne være hvis brugere skriver med store eller små bogstaver =
           # kan løses ved lower()
