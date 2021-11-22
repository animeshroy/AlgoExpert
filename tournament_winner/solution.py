def tournamentWinner(competitions, results):
	index=0
	default_team = 0
	len_result = len(results)
	winner_list = {}
	winner_team = competitions[0][0]
	winner_list[winner_team] = 0
	while index<len_result:
		team_cate = default_team if results[index] else 1
		current_team=competitions[index][team_cate]
		if competitions[index][team_cate] in winner_list:
			winner_list[competitions[index][team_cate]]+=1
		else:
			winner_list[competitions[index][team_cate]]=1
		if winner_list[current_team] > winner_list[winner_team]:
			winner_team = current_team
		index+=1
	return winner_team
