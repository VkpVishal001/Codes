while True:
    num = int(input("How many pairs of teams you want to create ? : ")) ; print()
    teams = []

    for i in range(num):
        var = input("Enter team's name : ")
        teams.append(var)

    if len(teams) % 2:
        teams.append('Day off')

    n = len(teams)
    matchs = []
    fixtures = []
    return_matchs = []

    for fixture in range(1,n):
        for i in range(int(n/2)):
            matchs.append((teams[i], teams[n - 1 - i]))
            return_matchs.append((teams[n - 1 - i], teams[i]))

        teams.insert(1, teams.pop())
        fixtures.insert(int(len(fixtures)/2), matchs)
        fixtures.append(return_matchs)
        matchs = []
        return_matchs = []

    for i in fixtures:
        for x in i:
            for y in x:
                if y == "Day off":
                    i.remove(x)

    grandlist = sum(fixtures, [])
    print()

    for i in fixtures:
        print(i)
