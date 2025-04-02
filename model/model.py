from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPd(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPdWithIscritti(self, pd):
        return DAO.getCorsiPdWithIscritti(pd)

    def getStudentiCorso(self, codins):
        return sorted(DAO.getStudentiCorso(codins),key=lambda s:s.cognome)

    def getCDSofCorso(self, codins):
        return sorted(DAO.getCDSofCorso(codins), key=lambda c: c[1], reverse=True)