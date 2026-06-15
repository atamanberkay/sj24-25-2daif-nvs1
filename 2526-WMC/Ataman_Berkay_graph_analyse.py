def csv_einlesen(dateiname):
    matrix = []
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            zeile = zeile.strip()
            if zeile:
                matrix.append([int(x) for x in zeile.split(";")])
    return matrix


def matrix_mult_bool(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i][k] == 1 and B[k][j] == 1:
                    C[i][j] = 1
                    break
    return C


def distanzen_berechnen(adj):
    n = len(adj)
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    potenz = [zeile[:] for zeile in adj]

    for schritt in range(1, n):
        for i in range(n):
            for j in range(n):
                if potenz[i][j] == 1 and dist[i][j] == -1:
                    dist[i][j] = schritt
        potenz = matrix_mult_bool(potenz, adj)

    return dist


def exzentrizitaeten(dist):
    exz = []
    for zeile in dist:
        if -1 in zeile:
            exz.append(float("inf"))
        else:
            exz.append(max(zeile))
    return exz


def radius_durchmesser_zentrum(exz):
    endliche = [x for x in exz if x != float("inf")]

    if not endliche:
        return None, None, []

    radius = min(endliche)
    durchmesser = max(endliche)
    zentrum = [i for i, x in enumerate(exz) if x == radius]

    return radius, durchmesser, zentrum


def komponenten(adj):
    n = len(adj)
    besucht = [False] * n
    erg = []

    for start in range(n):
        if not besucht[start]:
            stack = [start]
            besucht[start] = True
            komp = []

            while stack:
                v = stack.pop()
                komp.append(v)

                for nachbar in range(n):
                    if adj[v][nachbar] == 1 and not besucht[nachbar]:
                        besucht[nachbar] = True
                        stack.append(nachbar)

            erg.append(komp)

    return erg


def entferne_knoten(adj, k):
    neue = []
    for i in range(len(adj)):
        if i != k:
            zeile = []
            for j in range(len(adj)):
                if j != k:
                    zeile.append(adj[i][j])
            neue.append(zeile)
    return neue


def artikulationen(adj):
    ursprung = len(komponenten(adj))
    erg = []

    for k in range(len(adj)):
        neue_matrix = entferne_knoten(adj, k)
        if len(komponenten(neue_matrix)) > ursprung:
            erg.append(k)

    return erg


def entferne_kante(adj, a, b):
    neue = [zeile[:] for zeile in adj]
    neue[a][b] = 0
    neue[b][a] = 0
    return neue


def bruecken(adj):
    n = len(adj)
    ursprung = len(komponenten(adj))
    erg = []

    for i in range(n):
        for j in range(i + 1, n):
            if adj[i][j] == 1:
                neue_matrix = entferne_kante(adj, i, j)
                if len(komponenten(neue_matrix)) > ursprung:
                    erg.append((i, j))
    return erg


def main():
    dateiname = input("CSV-Datei eingeben: ")
    adj = csv_einlesen(dateiname)

    dist = distanzen_berechnen(adj)
    exz = exzentrizitaeten(dist)
    radius, durchmesser, zentrum = radius_durchmesser_zentrum(exz)

    print("Distanzmatrix:", dist)
    print("Exzentrizitäten:", exz)
    print("Radius:", radius)
    print("Durchmesser:", durchmesser)
    print("Zentrum:", zentrum)
    print("Komponenten:", komponenten(adj))
    print("Artikulationen:", artikulationen(adj))
    print("Brücken:", bruecken(adj))


if __name__ == "__main__":
    main()
