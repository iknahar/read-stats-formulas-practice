# Read Stats Formulas Practice

Practice code for learning to read statistics formulas and turn them into NumPy.
Every script uses the same tiny dataset: one week of step counts and hours of sleep.

```
day   i   steps    sleep (hours)
Mon   1    6,200   7.5
Tue   2    8,400   6.0
Wed   3    4,100   7.5
Thu   4    9,800   7.0
Fri   5    7,300   6.5
Sat   6   11,800   6.5
Sun   7    3,500   8.0
```

## Setup

```bash
python -m pip install -r requirements.txt
```

Then run any script, for example `python 01_sigma.py`.

## Scripts

| File | Formula idea |
|---|---|
| `01_sigma.py` | Σ as a loop, `np.sum`, and Σx² versus (Σx)² |
| `02_subscripts_and_limits.py` | what the index i does, sum limits as slices, double subscripts x_ij |
| `03_greek_vs_latin.py` | μ (truth) versus x̄ (your guess) across forty imaginary weeks |
| `04_hats.py` | β̂ and p̂, estimates that change with every sample |
| `05_expectation.py` | E[X] = Σ x·p(x) for roulette and a die, checked by simulation |
| `06_variance_ddof.py` | the variance formula term by term, and why NumPy and pandas disagree |
| `07_bias_simulation.py` | why dividing by n − 1 fixes a too-small variance |
| `08_z_scores.py` | standardising: subtract the mean, divide by the spread |
| `09_logs_vs_products.py` | multiplying many probabilities underflows, summing logs does not |
| `10_correlation_from_parts.py` | the correlation formula built by hand and checked against NumPy |
| `11_rain_two_days.py` | why 0.5 × 0.5 is wrong when rain sticks around |
| `12_week_change.py` | a phone's weekly report as two averages and a percent change |
| `13_poll_margin.py` | p versus p-hat, and where "plus or minus 3" comes from |
| `14_exam_z_scores.py` | comparing 72 on a hard exam with 80 on an easy one |

## Exercises

1. Change `steps` in `01_sigma.py` to your own week. Does the loop total still match `np.sum`?
2. Write Σ(xᵢ − 1)² for x = 1, 2, 3 by hand, then in NumPy.
3. In `02_subscripts_and_limits.py`, compute the mean of the weekend only (i = 6 to 7).
4. Run `06_variance_ddof.py` on a single number, `np.array([5000])`. What do NumPy and pandas return, and why?
5. In `07_bias_simulation.py`, change the sample size from 5 to 2. How far off is dividing by n now?
6. Compute the z-score of your own busiest day.
7. In `09_logs_vs_products.py`, find the smallest number of 0.5s whose product prints 0.0.
8. Measure `sleep` in minutes instead of hours in `10_correlation_from_parts.py`. Which numbers change?
9. In `11_rain_two_days.py`, set both 0.7 and 0.3 to 0.5. What does "both days" come out as now, and why?
10. In `13_poll_margin.py`, ask 4,000 people per poll instead of 1,000. What happens to the margin?

<details>
<summary>Answers</summary>

1. Yes, they always match, because `np.sum` is the same loop.
2. (0)² + (1)² + (2)² = 5. In NumPy: `np.sum((x - 1) ** 2)`.
3. `steps[5:].mean()` gives 7,650.
4. NumPy gives 0.0. pandas gives NaN, because it divides by n − 1 = 0.
5. With n = 2, dividing by n averages about half the true variance (a factor of 1/2).
6. `(my_day - steps.mean()) / steps.std(ddof=1)`.
7. 1,075. The product of 1,074 halves is the smallest positive float, about 4.9e-324.
8. The covariance grows 60 times. The correlation r stays at -0.7334.
9. About 0.25. With no link between the days, multiplying works again.
10. It halves, to about 0.015, because the margin shrinks with the square root of the sample size.

</details>

## License

MIT
