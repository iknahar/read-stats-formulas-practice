# multiplying probabilities is only allowed when events are independent
p_one = 1 / 8543
print("if independent:", 1 / (p_one * p_one))    # about 73 million
#
# if a shared cause makes the second event 10 times more likely
# after the first, the honest number is ten times less extreme
p_second_given_first = 10 * p_one
print("with dependence:", 1 / (p_one * p_second_given_first))
