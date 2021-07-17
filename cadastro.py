class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

        def exibir(self):
            print(f'-> {self.nome} - {self.fone}')

class Squad:
    def __init__(self, nome, techlead=None, devs=None) -> object:
        self.nome = nome
        self.devs = []
        self.techlead = techlead

        def incluir_tech(self, techlead):
            self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)

    def incluir_tech(self, techlead):
        pass


class Colaborador(Pessoa):
    def __init__(self, nome, fone, squad=None):
        super().__init__(nome, fone)
        self.squad = squad

    def incluir_squad(self, squad):
        self.squad = squad
class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad=None):
        super().__init__(nome, fone, squad)
        self.cargo = cargo

        def exibir(self):
            super().exibir()
            print(f'  Cargo de {self.cargo} na squad {self.squad.nome}\n')
print('\n-==-=-=-=-=-=-=-=-=-=-Sky One solutions-==-=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de cadastro de squads\n')

while True:
    squads = []
    nome_squad = input('\nNome da Squad: ')
    nome_techlead = input('Nome do Techlead da Squad: ')
    fone_techlead = input('Telefone do Techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_tech(techlead)
    techlead.incluir_squad(squad)
    option = input('\nDeseja adicionar mais um squad [S/N]: ')
    if option in 'Nn':
        break
    squads.append(squad)
    while True:
        nome_dev = input('\n Nome do desenvolvedor: ')
        fone_dev = input('Fone do desenvolvedor: ')
        cargo_dev = input('Cargo do desenvolvedor')
        dev = Dev(nome_dev, fone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)

        option = input('\nDeseja adicionar mais um Dev [S/N]: ')
        if option in 'Nn':
            break
            for squad in squads:
                print(f'\n-------------------------------{squad.nome}-------------------------------')
                print(f'\Techlead: {squad.techlead.nome}')
                print('\n-----Devs do Squad-----')

                for dev in squad.devs:
                    dev.exibir()
                print(f'---------------------------------{nome, squad}---------------------------------')

                print('\n-==-=-=-=-=-=-=-=-=-=-Sky One solutions-==-=-=-=-=-=-=-=-=-=-')
