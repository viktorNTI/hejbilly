choice = 0
message = " "
meny = 0

while meny !=3:
    try: 
        meny = int(input("Läs loggar (1) Skriv ut en logg (2) Avsluta (3)")) 
    except:
        print("Välj (1), (2) eller (3)")
    if meny == 1:
        f = open('log.txt', 'r')
        for line in f:
            print(line)
        f.close()

    elif meny == 2:
        f = open('log.txt', 'w+')
        message = (input("Skriv till loggen"))
        f.write(message)     
        f.close() 
