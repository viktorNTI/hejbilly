choice = 0 #här bestämmer vi ett värde på variabeln så programmet inte kraschar
message = " " #här sätter vi en tom sträng i variabeln så vi kan använda den senare
meny = 0 #här bestämmer vi ett värde på variabeln så programmet inte kraschar
loglist = ["test", "slumpmässigt"]

while meny !=3: #medans variabeln inte är 3 så loopar den
    try: #så försöker den...
        meny = int(input("Läs loggar (1) Skriv ut en logg (2) Avsluta (3)")) #få en input från användaren 
    except: #om användaren inte anger 1, 2 eller 3 så skriver den ut...
        print("Välj (1), (2) eller (3)") #ett meddelande
    if meny == 1: #om användaren anger 1
        choice = int(input("Skriv ut alla loggar (1) Läs loggar (2)"))
        if choice == 1:
            print("försök")
            f = open('log.txt', 'w+')
            for line in f:
                print(line)
                loglist.append("Jens")
                print(loglist)
            
        elif choice == 2:
            f = open('log.txt', 'r') #så öppnar programmet log.txt med läsrättigheter
            for line in f: #en loop som skriver ut det som står i log.txt
                print(line) #den skriver ut linjen
            f.close() #programmet stänger log.txt och sparar innehållet

    elif meny == 2: #om användaren anger 2
        f = open('log.txt', 'a+') #så öppnar programmet log.txt med write and read funktioner
        message = (input("Skriv till loggen")) #programmet frågar efter en input i syfte att skriva in i log.txt som en sträng
        f.write(message) #skriver in vad användaren tilldelade variabeln message i log.txt     
        f.close() #programmet stänger log.txt och sparar innehållet
