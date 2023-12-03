from abc import ABCMeta, abstractmethod


class Personne(metaclass=ABCMeta):
    def __init__(self, code, nom, prenom, age):
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._age = age

    @property
    def getGode(self):
        return self._code


    def setCode(self, n):
        self._code = n

    @property
    def getNom(self):
        return self._nom


    def setNom(self, n):
        self._nom = n

    @property
    def getPrenom(self):
        return self._prenom


    def setNom(self, n):
        self._nom = n

    @property
    def getAge(self):
        return self._age

    @property
    def setAge(self, n):
        self._age = n

    @abstractmethod
    def ToString(self):
        pass

    def Equals(self, other):
        return self._code == other._code


class Employe(Personne):
    def __init__(self, code, nom, prenom, age, grade):
        super().__init__(code, nom, prenom, age)
        self._grade = grade

    @property
    def getGrade(self):
        return self._grade


    def setGrade(self, n):
        self._grade = n

    def ToString(self):
        return f"Employé - Code: {self._code}, Nom: {self._nom}, Prénom: {self._prenom}, Âge: {self._age}, Grade: {self._grade}"


class Eleve(Personne):
    def __init__(self, code, nom, prenom, age, niveau, moyenne):
        super().__init__(code, nom, prenom, age)
        self._niveau = niveau
        self._moyenne = moyenne

    @property
    def niveau(self):
        return self._niveau

    @property
    def moyenne(self):
        return self._moyenne

    def ToString(self):
        return f"Élève - Code: {self._code}, Nom: {self._nom}, Prénom: {self._prenom}, Âge: {self._age}, Niveau: {self._niveau}, Moyenne: {self._moyenne}"


# Classe de test
class Test:
    employes = []
    eleves = []

    def __init__(self):
        # Création d'objets Employe
        emp1 = Employe(1, "yahya", "zaizi", 30, "Manager")
        emp2 = Employe(2, "Smith", "Jane", 25, "Supervisor")
        emp3 = Employe(3, "Johnson", "Bob", 35, "Director")

        # Création d'objets Eleve
        eleve1 = Eleve(101, "Parker", "Peter", 18, "12th Grade", 85)
        eleve2 = Eleve(102, "Watson", "Mary", 17, "11th Grade", 90)
        eleve3 = Eleve(103, "Thompson", "Flash", 19, "12th Grade", 75)


        self.employes.extend([emp1, emp2, emp3])
        self.eleves.extend([eleve1, eleve2, eleve3])

    def afficher_informations(self):
        print("Informations des Employés:")
        for employe in self.employes:
            print(employe.ToString())

        print("\nInformations des Élèves:")
        for eleve in self.eleves:
            print(eleve.ToString())

    def tester_equals(self):
        emp1 = self.employes[0]
        emp2 = Employe(1, "Doe", "John", 30, "Manager")

        eleve1 = self.eleves[0]
        eleve2 = Eleve(101, "Parker", "Peter", 18, "12th Grade", 85)

        print(f"\nTester Equals pour Employé : {emp1.Equals(emp2)}")
        print(f"Tester Equals pour Élève : {eleve1.Equals(eleve2)}")

    def afficher_nombre_objets(self):
        print(f"\nNombre d'objets Employé créés : {len(self.employes)}")
        print(f"Nombre d'objets Élève créés : {len(self.eleves)}")


# Exécution du test
test = Test()
test.afficher_informations()
test.tester_equals()
test.afficher_nombre_objets()
