 
# Lab 3: The Deployment Budget Optimizer

**File:** `budget_optimizer.py`

A function that estimates the monthly cost of running a group of cloud servers and checks it against a budget cap, returning an approval or rejection message.

## How it works

1. `estimate_deployment_cost(instance_count, hourly_rate, budget_cap)` takes three inputs
2. Monthly cost = instances x hourly rate x 720 hours (30 days x 24 hours)
3. If the cost is above the budget cap, it returns `REJECTED: Budget Exceeded by $X!` (X = amount over budget)
4. Otherwise it returns `APPROVED: Total Estimated Cost is $X.` (X = total cost)
5. Dollar amounts are formatted to two decimal places

## Run it

```bash
python3 budget_optimizer.py
```

## Example output

```
REJECTED: Budget Exceeded by $120.00!
REJECTED: Budget Exceeded by $2344.00!
APPROVED: Total Estimated Cost is $720.00.
APPROVED: Total Estimated Cost is $720.00.
REJECTED: Budget Exceeded by $16.00!
```

## Concepts practised

- Functions with parameters and return values
- Keyword arguments when calling a function
- Arithmetic with floats, and formatting money with `:.2f`
- `if` / `else` with the comparison operators `>` and `<=`

## Tested cases

| Instances | Hourly rate | Budget cap | Monthly cost | Result |
|---|---|---|---|---|
| 5 | 0.45 | 1500 | 1620 | Rejected, $120.00 over |
| 12 | 0.85 | 5000 | 7344 | Rejected, $2344.00 over |
| 2 | 0.50 | 1000 | 720 | Approved |
| 1 | 1.00 | 720 | 720 | Approved (exactly on budget) |
| 3 | 0.10 | 200 | 216 | Rejected, $16.00 over |
