#import modułów:
import tkinter as tk
import tkinter.messagebox


# dodawanie macierzy:
def dodawanie(a,b):
    suma = [] #lista, w której umieścimy sumę macierzy
    for i in range(len(a)):
        wiersz = [] #lista, w której umieścimy pojedyńczy wiersz sumy
        for j in range(len(a[0])):
            wiersz.append(a[i][j] + b[i][j]) #dodawanie element po elemencie
        suma.append(wiersz) #dodawanie kolejnych wierszy do listy
    return suma #zwracanie wyniku


# odejmowanie macierzy:
def odejmowanie(a,b):
    roznica = []
    for i in range(len(a)):
        wiersz = []
        for j in range(len(a[0])):
            wiersz.append(a[i][j] - b[i][j])
        roznica.append(wiersz)
    return roznica


#mnożenie macierzy:
def mnozenie(a,b):
    iloczyn = []
    for i in range(len(a)):
        wiersz = []
        for j in range(len(b[0])):
           c = 0
           for k in range(len(b)):
               c += a[i][k] * b[k][j] #obliczanie elementów macierzy wynikowej
           wiersz.append(c)
        iloczyn.append(wiersz)
    return iloczyn


#wyznacznik macierzy:
def wyznacznik(a):
    det = 0
    if len(a) == 1 and len(a[0]) == 1:
        det = a[0][0]
    else:
        for i in range(len(a)):
            b = [row[1:] for row in a]
            del b[i]
            det += ((-1)**(i+1+1))*a[i][0]*wyznacznik(b) #obliczanie wyznacznika zgodnie z rozwinięciem Laplace'a (rekurencyjnie)
    return det


#transpozycja macierzy:
def transpozycja(a):
    transponowana = []
    for i in range(len(a[0])):
        wiersz = []
        for j in range(len(a)):
            wiersz.append(a[j][i]) #zamiana wierszy z kolumnami
        transponowana.append(wiersz)
    return transponowana


#odwracanie macierzy:
def odwracanie(a):
    dopelnienia = []  #macierz dopełnień algebraicznych
    for i in range(len(a)):
        wiersz = []
        for j in range(len(a)):
            D = a[:]
            del D[i]
            D = transpozycja(D)
            del D[j]
            D = transpozycja(D)
            D = (-1)**(i+j)*wyznacznik(D)
            wiersz.append(D)
        dopelnienia.append(wiersz)
    dolaczona = transpozycja(dopelnienia) #macierz dołączona

    odwrotna = []
    for i in range(len(a)):
        wiersz = []
        for j in range(len(a)):
            o = dolaczona[i][j]/wyznacznik(a) #obliczanie elementów macierzy odwrotnej zgodnie ze wzorem
            wiersz.append(o)
        odwrotna.append(wiersz)
    return odwrotna


okno = tk.Tk() #tworzenie okna
okno.configure(bg='ivory3') #kolor tła okna
okno.title('Operacje na macierzach') #tytuł okna

#KOMUNIKAT O BłĘDZIE:
def komunikat():
    tk.messagebox.showwarning(title = 'Błąd', message = 'Niepoprawne dane!')

#DODAWANIE:

def ok1():
    okno1 = tk.Toplevel()
    okno1.focus()    #nowe okno będzie domyślnie wybranym
    okno1.title('Dodawanie macierzy')
    tekst1 = tk.Label(okno1, text='Podaj liczbę wierszy: ',height=2,width=25).grid(row = 0, column = 0) #tekst wyświetlany wewnątrz okna, o szerokości 25 i wyskokści 2
    tekst2 = tk.Label(okno1, text='Podaj liczbę kolumn: ',height=2,width=25).grid(row = 1, column = 0)
    pole1 = tk.Entry(okno1) #pole do wpisywania danch (jednolinijkowe)
    pole2 = tk.Entry(okno1)
    pole1.grid(row=0, column=1) #pozycja danego widżetu: wiersz zerowy, kolumna pierwsza
    pole2.grid(row=1, column=1)

    def obl1():
        e = 0 #zmienna kontrolująca błędy
        try: #próba wczytania danych liczbowych, w razie błędu wyświelany jest komunikat; jeśli brak błędów program wykonuje się dalej
            wiersze = int(pole1.get())
            kolumny = int(pole2.get())
        except:
            komunikat()
        else:
            okno1.destroy() #zamknięcie okna
            macierz1 = [] #lista na dane
            for i in range(wiersze): #pętla tworząca tyle okienek, ile jest wierszy w macierzy
                okno1_1= tk.Toplevel() #tworzenie nowych okienek
                okno1_1.focus()
                okno1_1.title('Dodawanie macierzy')
                tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy 1 oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                pole1_1= tk.Entry(okno1_1)
                pole1_1.grid(row = 0, column = 1)

                var = tk.IntVar() #zmienna której wartość ulega zmianie po naciśnięciu przycisku

                prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1)) #zmiana wartości zmiennej var po naciśnięciu przycisku
                prz1.grid(row = 3, columnspan = 2)
                okno.wait_variable(var) #dopiero po naciśnięciu przycisku program będzie kontynuować pracę

                row_str= pole1_1.get() #pobieranie wartości z pola do wpisywania danych
                row_str = row_str.split(' ') #rozdzielanie wiersza na elementy w miejscach spacji
                map1 = map(eval, row_str) #określanie wartości elementów (zamiana z napisów na liczby)
                row = list(map1) #zamiana na listę (z funkcji map dostajemy 'map object')
                okno1_1.destroy()
                if len(row) != kolumny: #sprawdzanie czy długość wiersza odpowiada liczbie kolumn
                    komunikat()
                    e = 1
                    break
                else:
                    macierz1.append(row) #dodawanie wiersza do macierzy

            if e == 0: #jeśli brak błędów to przechodzimy dalej
                macierz2 = []
                for i in range(wiersze):
                    okno1_1= tk.Toplevel()
                    okno1_1.focus()
                    okno1_1.title('Dodawanie macierzy')
                    tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy 2 oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                    pole1_1= tk.Entry(okno1_1)
                    pole1_1.grid(row = 0, column = 1)

                    var = tk.IntVar()

                    prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                    prz1.grid(row = 3, columnspan = 2)
                    okno.wait_variable(var)

                    row_str= pole1_1.get()
                    row_str = row_str.split(' ')
                    map1 = map(eval, row_str)
                    row = list(map1)
                    okno1_1.destroy()
                    if len(row)!=kolumny:
                        komunikat()
                        e = 1
                        break
                    else:
                        macierz2.append(row)

                if e == 0:
                    wynik = dodawanie(macierz1,macierz2) #obliczanie wyniku przy użyciu funkcji 'dodawanie'
                    okno1_2 = tk.Toplevel()
                    okno1_2.title('Suma macierzy')
                    tekst1_2= tk.Label(okno1_2, text = 'Suma macierzy to: ').grid(row = 0, column = 0)
                    pole1_2 = tk.Text(okno1_2, height = wiersze)
                    pole1_2.grid(row= 1)
                    for i in range(wiersze):
                        for j in range(kolumny):
                            pole1_2.insert('end', str(wynik[i][j])+' ') #wypisywanie macierzy wynikowej w pętli
                            if j == kolumny-1:
                                pole1_2.insert('end', '\n') #przechodzenie do nowego wiersza

    prz = tk.Button(okno1, text = 'Dalej', command = obl1).grid(row = 2, columnspan = 2) #przycisk wykonujący funkcję obl1, jest umiejscowiony w drugim wierszu i zajmuje dwie kolumny szerokości

#ODEJMOWANIE:

def ok2():
    okno1 = tk.Toplevel()
    okno1.focus()
    okno1.title('Odejmowanie macierzy')
    tekst1 = tk.Label(okno1, text='Podaj liczbę wierszy: ',height=2,width=25).grid(row = 0, column = 0)
    tekst2 = tk.Label(okno1, text='Podaj liczbę kolumn: ',height=2,width=25).grid(row = 1, column = 0)
    pole1 = tk.Entry(okno1)
    pole2 = tk.Entry(okno1)
    pole1.grid(row=0, column=1)
    pole2.grid(row=1, column=1)

    def obl2():
        e = 0
        try:
            wiersze = int(pole1.get())
            kolumny = int(pole2.get())
        except:
            komunikat()
        else:
            okno1.destroy()
            macierz1 = []
            for i in range(wiersze):
                okno1_1= tk.Toplevel()
                okno1_1.focus()
                okno1_1.title('Odejmowanie macierzy')
                tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy 1 oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                pole1_1= tk.Entry(okno1_1)
                pole1_1.grid(row = 0, column = 1)

                var = tk.IntVar()

                prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                prz1.grid(row = 3, columnspan = 2)
                okno.wait_variable(var)

                row_str= pole1_1.get()
                row_str = row_str.split(' ')
                map1 = map(eval, row_str)
                row = list(map1)
                okno1_1.destroy()
                if len(row)!=kolumny:
                    komunikat()
                    e = 1
                    break
                else:
                    macierz1.append(row)

            if e == 0:
                macierz2 = []
                for i in range(wiersze):
                    okno1_1= tk.Toplevel()
                    okno1_1.focus()
                    okno1_1.title('Odejmowanie macierzy')
                    tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy 2 oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                    pole1_1= tk.Entry(okno1_1)
                    pole1_1.grid(row = 0, column = 1)

                    var = tk.IntVar()

                    prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                    prz1.grid(row = 3, columnspan = 2)
                    okno.wait_variable(var)

                    row_str= pole1_1.get()
                    row_str = row_str.split(' ')
                    map1 = map(eval, row_str)
                    row = list(map1)
                    okno1_1.destroy()
                    if len(row)!=kolumny:
                        komunikat()
                        e = 1
                        break
                    else:
                        macierz2.append(row)

                if e == 0:
                    wynik = odejmowanie(macierz1,macierz2)
                    okno1_2 = tk.Toplevel()
                    okno1_2.title('Różnica macierzy')
                    tekst1_2= tk.Label(okno1_2, text = 'Różnica macierzy to: ').grid(row = 0, column = 0)
                    pole1_2 = tk.Text(okno1_2, height = wiersze)
                    pole1_2.grid(row= 1)
                    for i in range(wiersze):
                        for j in range(kolumny):
                            pole1_2.insert('end', str(wynik[i][j])+' ')
                            if j == kolumny-1:
                                pole1_2.insert('end', '\n')

    prz = tk.Button(okno1, text = 'Dalej', command = obl2).grid(row = 2, columnspan = 2)

#MNOŻENIE:

def ok3():
    okno1 = tk.Toplevel()
    okno1.focus()
    okno1.title('Mnożenie macierzy')
    tekst1 = tk.Label(okno1, text='Podaj liczbę wierszy macierzy 1: ',height=2,width=25).grid(row = 0, column = 0)
    tekst2 = tk.Label(okno1, text='Podaj liczbę kolumn macierzy 1: ',height=2,width=25).grid(row = 1, column = 0)
    tekst3 = tk.Label(okno1, text='Podaj liczbę wierszy macierzy 2: ',height=2,width=25).grid(row = 2, column = 0)
    tekst4 = tk.Label(okno1, text='Podaj liczbę kolumn macierzy 2: ',height=2,width=25).grid(row = 3, column = 0)
    pole1 = tk.Entry(okno1)
    pole2 = tk.Entry(okno1)
    pole3 = tk.Entry(okno1)
    pole4 = tk.Entry(okno1)
    pole1.grid(row=0, column=1)
    pole2.grid(row=1, column=1)
    pole3.grid(row=2, column=1)
    pole4.grid(row=3, column=1)

    def obl3():
        e = 0
        try:
            wiersze1 = int(pole1.get())
            kolumny1 = int(pole2.get())
            wiersze2 = int(pole3.get())
            kolumny2 = int(pole4.get())
        except:
            komunikat()
        else:
            okno1.destroy()
            if kolumny1 == wiersze2:
                macierz1 = []
                for i in range(wiersze1):
                    okno1_1= tk.Toplevel()
                    okno1_1.focus()
                    okno1_1.title('Mnożenie macierzy')
                    tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy 1 oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                    pole1_1= tk.Entry(okno1_1)
                    pole1_1.grid(row = 0, column = 1)

                    var = tk.IntVar()

                    prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                    prz1.grid(row = 3, columnspan = 2)
                    okno.wait_variable(var)

                    row_str= pole1_1.get()
                    row_str = row_str.split(' ')
                    map1 = map(eval, row_str)
                    row = list(map1)
                    okno1_1.destroy()
                    if len(row)!=kolumny1:
                        komunikat()
                        e = 1
                        break
                    else:
                        macierz1.append(row)

                if e == 0:
                    macierz2 = []
                    for i in range(wiersze2):
                        okno1_1= tk.Toplevel()
                        okno1_1.focus()
                        okno1_1.title('Mnożenie macierzy')
                        tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy 2 oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                        pole1_1= tk.Entry(okno1_1)
                        pole1_1.grid(row = 0, column = 1)

                        var = tk.IntVar()

                        prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                        prz1.grid(row = 3, columnspan = 2)
                        okno.wait_variable(var)

                        row_str= pole1_1.get()
                        row_str = row_str.split(' ')
                        map1 = map(eval, row_str)
                        row = list(map1)
                        okno1_1.destroy()
                        if len(row)!=kolumny2:
                            komunikat()
                            e = 1
                        else:
                            macierz2.append(row)

                    if e == 0:
                        wynik = mnozenie(macierz1,macierz2)
                        okno1_2 = tk.Toplevel()
                        okno1_2.title('Iloczyn macierzy')
                        tekst1_2= tk.Label(okno1_2, text = 'Iloczyn macierzy to: ').grid(row = 0, column = 0)
                        pole1_2 = tk.Text(okno1_2, height = wiersze1)
                        pole1_2.grid(row= 1)
                        for i in range(wiersze1):
                            for j in range(kolumny2):
                                pole1_2.insert('end', str(wynik[i][j])+' ')
                                if j == kolumny2-1:
                                    pole1_2.insert('end', '\n')
            else:
                komunikat()
    prz = tk.Button(okno1, text = 'Dalej', command = obl3).grid(row = 4, columnspan = 2)

#WYZNACZNIK:

def ok4():
    okno1 = tk.Toplevel()
    okno1.focus()
    okno1.title('Wyznacznik macierzy')
    tekst1 = tk.Label(okno1, text='Podaj liczbę wierszy macierzy kwadratowej: ',height=2,width=35).grid(row = 0, column = 0)
    pole1 = tk.Entry(okno1)
    pole1.grid(row=0, column=1)

    def obl4():
        e = 0
        try:
            wiersze = int(pole1.get())
        except:
            komunikat()
        else:
            okno1.destroy()
            macierz1 = []
            for i in range(wiersze):
                okno1_1= tk.Toplevel()
                okno1_1.focus()
                okno1_1.title('Wyznacznik macierzy')
                tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                pole1_1= tk.Entry(okno1_1)
                pole1_1.grid(row = 0, column = 1)

                var = tk.IntVar()

                prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                prz1.grid(row = 3, columnspan = 2)
                okno.wait_variable(var)

                row_str= pole1_1.get()
                row_str = row_str.split(' ')
                map1 = map(eval, row_str)
                row = list(map1)
                okno1_1.destroy()
                if len(row) != wiersze:
                    komunikat()
                    e = 1
                    break
                else:
                    macierz1.append(row)

            if e == 0:
                wynik = wyznacznik(macierz1)
                okno1_2 = tk.Toplevel()
                okno1_2.title('Wyznacznik macierzy')
                tekst1_2= tk.Label(okno1_2, text = 'Wyznacznik macierzy to: ').grid(row = 0, column = 0)
                pole1_2 = tk.Entry(okno1_2)
                pole1_2.grid(row= 1)
                pole1_2.insert('end',str(wynik))


    prz = tk.Button(okno1, text = 'Dalej', command = obl4).grid(row = 2, columnspan = 2)


#TRANSPONOWANIE:

def ok6():
    okno1 = tk.Toplevel()
    okno1.focus()
    okno1.title('Transpozycja macierzy')
    tekst1 = tk.Label(okno1, text='Podaj liczbę wierszy: ',height=2,width=25).grid(row = 0, column = 0)
    tekst2 = tk.Label(okno1, text='Podaj liczbę kolumn: ',height=2,width=25).grid(row = 1, column = 0)
    pole1 = tk.Entry(okno1)
    pole2 = tk.Entry(okno1)
    pole1.grid(row=0, column=1)
    pole2.grid(row=1, column=1)

    def obl6():
        e = 0
        try:
            wiersze = int(pole1.get())
            kolumny = int(pole2.get())
        except:
            komunikat()
        else:
            okno1.destroy()
            macierz1 = []
            for i in range(wiersze):
                okno1_1= tk.Toplevel()
                okno1_1.focus()
                okno1_1.title('Transpozycja macierzy')
                tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                pole1_1= tk.Entry(okno1_1)
                pole1_1.grid(row = 0, column = 1)

                var = tk.IntVar()

                prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                prz1.grid(row = 3, columnspan = 2)
                okno.wait_variable(var)

                row_str= pole1_1.get()
                row_str = row_str.split(' ')
                map1 = map(eval, row_str)
                row = list(map1)
                okno1_1.destroy()
                if len(row) != kolumny:
                    komunikat()
                    e = 1
                    break
                else:
                    macierz1.append(row)

            if e == 0:
                wynik = transpozycja(macierz1)
                okno1_2 = tk.Toplevel()
                okno1_2.title('Transpozycja macierzy')
                tekst1_2= tk.Label(okno1_2, text = 'Macierz transponowana to: ').grid(row = 0, column = 0)
                pole1_2 = tk.Text(okno1_2, height = kolumny)
                pole1_2.grid(row= 1)
                for i in range(kolumny):
                    for j in range(wiersze):
                        pole1_2.insert('end', str(wynik[i][j])+' ')
                        if j == wiersze-1:
                            pole1_2.insert('end', '\n')

    prz = tk.Button(okno1, text = 'Dalej', command = obl6).grid(row = 2, columnspan = 2)


#ODWRACANIE:

def ok5():
    okno1 = tk.Toplevel()
    okno1.focus()
    okno1.title('Odwracanie macierzy')
    tekst1 = tk.Label(okno1, text='Podaj liczbę wierszy macierzy kwadratowej: ',height=2,width=35).grid(row = 0, column = 0)
    pole1 = tk.Entry(okno1)
    pole1.grid(row=0, column=1)

    def obl5():
        e = 0
        try:
            wiersze = int(pole1.get())
        except:
            komunikat()
        else:
            okno1.destroy()
            macierz1 = []
            for i in range(wiersze):
                okno1_1= tk.Toplevel()
                okno1_1.focus()
                okno1_1.title('Odwracanie macierzy')
                tekst1_1= tk.Label(okno1_1, text = 'Podaj elementy wiersza '+str(i+1)+' macierzy oddzielone spacją: ',height=2).grid(row = 0, column = 0)
                pole1_1= tk.Entry(okno1_1)
                pole1_1.grid(row = 0, column = 1)

                var = tk.IntVar()

                prz1 = tk.Button(okno1_1, text='Dalej', command = lambda: var.set(1))
                prz1.grid(row = 3, columnspan = 2)
                okno.wait_variable(var)

                row_str= pole1_1.get()
                row_str = row_str.split(' ')
                map1 = map(eval, row_str)
                row = list(map1)
                okno1_1.destroy()
                if len(row) != wiersze:
                    komunikat()
                    e = 1
                    break
                else:
                    macierz1.append(row)

            if e == 0:
                if (wyznacznik(macierz1) == 0):
                    tk.messagebox.showwarning(title = 'Błąd', message = 'Wyznacznik macierzy jest równy zero. Takiej macierzy nie da się odwrócić!')
                else:
                    wynik = odwracanie(macierz1)
                    okno1_2 = tk.Toplevel()
                    okno1_2.title('Odwracanie macierzy')
                    tekst1_2= tk.Label(okno1_2, text = 'Macierz odwrotna to: ').grid(row = 0, column = 0)
                    pole1_2 = tk.Text(okno1_2, height = wiersze)
                    pole1_2.grid(row= 1)
                    for i in range(wiersze):
                        for j in range(wiersze):
                            pole1_2.insert('end', str(wynik[i][j])+' ')
                            if j == wiersze-1:
                                pole1_2.insert('end', '\n')

    prz = tk.Button(okno1, text = 'Dalej', command = obl5).grid(row = 2, columnspan = 2)




frame1 = tk.Frame(okno).grid(row = 0) #widżet 'frame' pomocny w grupowaniu innych widżetów w okienku
frame2 = tk.Frame(okno).grid(row = 1, column = 0)



tekst = tk.Label(okno, text = 'Wybierz operację, którą chcesz wykonać:', height = 2, bg='ivory3').grid(row = 0, columnspan = 2)


#PRZYCISKI:

bg1='ivory2' #tło przycisków
przycisk1 = tk.Button(frame2, text = 'Dodawanie macierzy',height=2,width=30, bg=bg1, command = ok1).grid(row = 1, column = 0)
przycisk2 = tk.Button(frame2, text = 'Odejmowanie macierzy',height=2,width=30, bg=bg1, command = ok2).grid(row = 1, column = 1)
przycisk3 = tk.Button(frame2, text = 'Mnożenie macierzy',height=2,width=30, bg=bg1, command = ok3).grid(row = 2, column = 0)
przycisk4 = tk.Button(frame2, text = 'Wyznacznik macierzy',height=2,width=30, bg=bg1, command = ok4).grid(row = 2, column = 1)
przycisk5 = tk.Button(frame2, text = 'Odwracanie macierzy',height=2,width=30, bg=bg1, command = ok5).grid(row = 3, column = 0)
przycisk6 = tk.Button(frame2, text = 'Transpozycja macierzy',height=2,width=30, bg=bg1, command = ok6).grid(row = 3, column = 1)



okno.mainloop() #pętla główna
