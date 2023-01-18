import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
for file_name in glob.glob('data*in'): 
        y = numpy.loadtxt(file_name, unpack = True)
        plt.plot(range(len(y)), y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
    x, y, od = numpy.loadtxt('data.out', unpack = True)
    plt.errorbar(x, y, marker='*', yerr=od)
    #opis osi
    plt.xlabel('x')
    plt.ylabel('y')
#zapis do pliku, format określony przez rozszerzenie w nazwie
    plt.savefig('res.pdf')
    