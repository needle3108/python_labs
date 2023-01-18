class IFS:
    def __init__(self, wsp, pr):
        self.x = []
        self.y = []
        self.wspolczynniki = wsp
        self.p = pr
        self.x.append(0)
        self.y.append(0)

    def przeksztalc(self, i):
        import random
        for j in range(i):
            losowanie = random.choices(self.wspolczynniki, self.p)[0]
            self.x.append(losowanie[0]*self.x[-1] + losowanie[1]*self.y[-1] + losowanie[2])
            self.y.append(losowanie[3]*self.x[-2] + losowanie[4]*self.y[-1] + losowanie[5])
    
    def rysuj(self, nazwa):
        import matplotlib.pyplot as plt
        plt.clf()
        plt.plot(self.x, self.y,'.')
        plt.savefig(nazwa)
            
