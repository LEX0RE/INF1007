class Noeud(object):
    """
    Représente un noeud d'un graphe
    """
    def __init__(self, nom: str):
        """
        Initialise le noeud

        Parameters
        -------
        nom : str.
            Noeud du noeud

        Raise
        -------
        TypeError
            Si le nom du noeud n'est pas un string
        """
        # TODO: à implémenter
        if type(nom) != str:
            raise TypeError()

        self.nom = nom
        self.voisins = []
    
    def ajoute_voisin(self, noeud):
        """
        Ajoute un noeud aux voisins du noeud (une arête)

        Parameters
        -------
        noeud : Noeud
            Noeud à ajouter comme voisin au noeud initial.

        Raise
        -------
        TypeError
            Si le noeud n'est pas un Noeud.
        """
        # TODO: à implémenter
        if type(noeud) != Noeud:
            raise TypeError()

        if noeud not in self.voisins:
            self.voisins.append(noeud)

    def __str__(self):
        """
        Afficher le noeud et ses noeuds voisins
        """
        # TODO: à implémenter
        return f"{self.__repr__()} est connecté à {str(self.voisins)[1:-1]}"
    
    def __repr__(self):
        """
        Afficher le nom du noeud
        """
        # TODO: à implémenter
        return self.nom


class Graphe(object):
    """
    Représente un ensemble de noeud relié entre eux qu'on appelle graphe
    """
    def __init__(self):
        """
        Initialise le graphe vide
        """
        # TODO: à implémenter
        self.graphe = []
        
    def ajoute_noeud(self, noeud: Noeud, aretes: list):
        """
        Ajoute un noeud dans le graphe ainsi que c'est lien (arêtes) avec les autres noeuds

        Parameters
        -------
        noeud : Noeud
            Noeud qui sera ajouté au graphe et auquel les arêtes seront relié.
        
        aretes : list
            Liste des noeuds qui seront relié à noeud

        Raise
        -------
        TypeError
            Si le noeud n'est pas un Noeud ou si arêtes n'est pas une liste
        """
        # TODO: à implémenter
        if type(noeud) != Noeud or type(aretes) != list:
            raise TypeError()

        if noeud not in self.graphe:
            self.graphe.append(noeud)
        for n in range(len(aretes)):
            self.ajoute_arete(noeud, aretes[n])

    def ajoute_arete(self, noeud1: Noeud, noeud2: Noeud):
        """
        Ajoute une arête entre deux noeuds

        Parameters
        -------
        noeud1 : Noeud
            Premier noeud qui sera relié par une arête au deuxième.
        
        noeud2 : Noeud
            Deuxième noeud qui sera relié par une arête au premier.

        Raise
        -------
        TypeError
            Si le noeud1 ou le noeud2 ne sont pas des Noeud
        """
        # TODO: à implémenter
        if type(noeud1) != Noeud or type(noeud2) != Noeud:
            raise TypeError()

        noeud1.ajoute_voisin(noeud2)

    def trouve_chemin(self, debut: Noeud, fin: Noeud, chemin=None):
        """
        Trouve une chemin possible entre deux noeuds du graphe
        (Pas nécessairement le plus court)

        Return
        -------
        None : Aucun chemin trouvé
        list : liste des noeuds qui forme le chemin

        Parameters
        -------
        debut : Noeud
            Le noeud auquel nous commençons le chemin
        
        fin : Noeud
            Deuxième noeud qui sera relié par une arête au premier.
        
        chemin : list ou None
            Deuxième noeud qui sera relié par une arête au premier. 
            (Défaut = None)

        Raise
        -------
        TypeError
            Si debut ou fin ne sont pas des Noeud ou 
            si chemin n'est pas de type None ou List
        
        ValueError
            Si chemin contient de noeud qui ne sont pas des graphes ou
            debut et fin ne sont pas dans graphe
        """
        # TODO: à implémenter
        if type(debut) != Noeud or type(fin) != Noeud:
            raise TypeError()
        elif debut not in self.graphe or fin not in self.graphe:
            raise ValueError()
        else:
            if type(chemin) is list:
                for noeud in chemin:
                    if noeud not in self.graphe:
                        raise ValueError()
            elif chemin:
                raise TypeError()

        if not chemin:
            chemin = []
        if debut in chemin:
            return None

        chemin.append(debut)
        for noeud in debut.voisins:
            if debut == fin or self.trouve_chemin(noeud, fin, chemin):
                return chemin

        if len(chemin):
            chemin.pop()


if __name__ == "__main__":
    # Création des noeuds
    a, b, c, d, e = Noeud('A'), Noeud('B'), Noeud('C'), Noeud('D'), Noeud('E')

    # Création du graphe
    graphe = Graphe()

    # Ajout des noeuds et des arêtes au graphe
    graphe.ajoute_noeud(noeud=a, aretes=[b, d])
    graphe.ajoute_noeud(noeud=b, aretes=[c])
    graphe.ajoute_noeud(noeud=c, aretes=[d, e])
    graphe.ajoute_noeud(noeud=d, aretes=[a, c, e])
    graphe.ajoute_noeud(noeud=e, aretes=[d])

    # Affichage de quelques noeuds
    print(a)
    print(d)
    print(e)

    # Recherche d'un chemin entre le noeud B et le noeud A
    chemin = graphe.trouve_chemin(b, a)
    print(f'Le chemin entre B et A est {chemin}')

    # Recherche d'un chemin entre le noeud E et le noeud B
    chemin = graphe.trouve_chemin(e, b)
    print(f'Le chemin entre E et B est {chemin}')
