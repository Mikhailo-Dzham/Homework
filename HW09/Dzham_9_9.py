tests = int(input())
for test in range(tests):
    dict_votes = {}
    votes = int(input())
    for aboba in range(votes):
        vote = int(input())
        if vote in dict_votes:
            dict_votes[vote] +=1
        else:
            dict_votes[vote] = 1
    win_count = 0
    winner = 0
    for kay, count in dict_votes.items():
        if count > win_count or count == win_count and kay < winner:
            win_count = count
            winner = kay

    print(winner)