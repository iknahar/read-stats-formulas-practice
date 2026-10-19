# which is better: 72 on a hard exam or 80 on an easy one?
hard_mean, hard_spread, hard_score = 55, 10, 72
easy_mean, easy_spread, easy_score = 78, 6, 80
#
z_hard = (hard_score - hard_mean) / hard_spread   # subtract, then divide
z_easy = (easy_score - easy_mean) / easy_spread
print("z on the hard exam:", round(z_hard, 2))    # 1.7
print("z on the easy exam:", round(z_easy, 2))    # 0.33
