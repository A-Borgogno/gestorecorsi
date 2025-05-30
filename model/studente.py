from dataclasses import dataclass


@dataclass
class Studente:
    matricola: str
    cognome: str
    nome: str
    CDS: str
    # corsi: list[Corso] = None
    # codins: list[str] = None

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola}) - {self.CDS}"