import matplotlib.pyplot as plt
import datetime
import string

def L_system(n, name, schemat = 'F+F−F−F+F'):
    step = ((1,0), (0,1), (-1, 0), (0,-1))
    i = 0
    x, y = [0], [0]
    aktX, aktY = x[0], y[0]
    dx, dy = step[i]

    seq = schemat[0]

    try:
        #copy = schemat
        #if copy.replace(seq, '').replace('+','').replace('-','') != :
         #   raise ValueError
        pass
    except ValueError as ex1:
        print('Schemat jest niepoprawny')

    else:
        for _ in range(n):
            seq = seq.replace(seq, schemat)
            for b in seq:
                if b == 'F':
                    aktX += dx
                    aktY += dy
                    x.append(aktX)
                    y.append(aktY)
                elif b == '+':
                    if i<3:
                        i += 1
                    else:
                        i = 0
                    dx, dy = step[i]
                    aktX += dx
                    aktY += dy
                    x.append(aktX)
                    y.append(aktY)
                elif b == '-':
                    if i>0:
                        i -= 1
                    else:
                        i = 3
                    dx, dy = step[i]
                    aktX += dx
                    aktY += dy
                    x.append(aktX)
                    y.append(aktY)
        plt.plot(x,y,'-') 
        plt.savefig(name)               


def nr_pesel(pesel, day, month, year, plec):
    data1 = datetime.date(year, month, day)
    rok = str(year)
    miesiac = str(month)
    dzien = str(day)

    if rok[2] != pesel[0] or rok[3] != pesel[1]:
        return False

    if year >= 1800 and year <= 1899:
        temp_month = str(month + 80)
        if temp_month[0] != pesel[2] or temp_month[1] != pesel[3]:
            return False
    if year >= 1900 and year <= 1999:
        if month >= 10:
            if miesiac[0] != pesel[2] or miesiac[1] != pesel[3]:
                return False
        elif pesel[2] != '0' or miesiac[0] != pesel[3]:
            return False                
    if year >= 2000 and year <= 2099:
        temp_month = str(month + 20)
        if temp_month[0] != pesel[2] or temp_month[1] != pesel[3]:
            return False
    if year >= 2100 and year <= 2199:
        temp_month = str(month + 40)
        if temp_month[0] != pesel[2] or temp_month[1] != pesel[3]:
            return False
    if year >= 2200 and year <= 2299:
        temp_month = str(month + 60)
        if temp_month[0] != pesel[2] or temp_month[1] != pesel[3]:
            return False
    if day >= 10:
        if dzien[1] != pesel[4] or dzien[2] != pesel[5]:
            return False
    elif pesel[4] != '0' or pesel[5] != dzien[0]:
        return False
    if pesel[9] in ['0', '2', '4', '6', '8']:
        if plec != 'kobieta':
            return False
    elif plec != 'mezczyzna':
        return False

    suma = 0
    for i in range(10):
        liczba = int(pesel[i])
        if i in [0, 4, 8]:
            suma += liczba
        elif i in [1, 5, 9]:
            liczba *= 3
            suma += liczba
        elif i in [2, 6]:     
            liczba *= 7
            suma += liczba
        else:
            liczba *= 9
            suma += liczba       
    suma %= 10
    suma = 10 - suma
    suma %= 10
    if str(suma) != pesel[10]:
        return False
    return True        

if __name__ == '__main__':
    L_system(1, 'picture')
    L_system(3, 'picture1')
    L_system(5, 'picture2')

    print(nr_pesel('02070803628', 8, 7, 1902, 'kobieta'))
    print(nr_pesel('02270803624', 8, 7, 2002, 'kobieta'))
    print(nr_pesel('02270812350', 8, 7, 2002, 'mezczyzna'))
    pass
