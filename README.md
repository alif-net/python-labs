# Python Labs

Hands-on Python exercises, one script per lab, written and tested from the command line.

## Lab 1: Smart Survey Onboarding Engine

**File:** `survey_onboarding.py`

An interactive command-line script that interviews a user, collects their profile, and assigns an access clearance tier based on age and developer status.

### How it works

1. **Input:** asks for name, age, and whether the user is a developer (yes/no)
2. **Process:** converts the answers to the right data types and applies the tier rules
3. **Output:** prints a formatted profile card

### Tier rules

| Condition | Clearance tier |
|---|---|
| Under 18 | Tier 3: Guest |
| 18 or older and a developer | Tier 1: Admin Infrastructure Access |
| 18 or older, not a developer | Tier 2: Standard Executive Access |

### Run it

```bash
python3 survey_onboarding.py
```

### Example

```
What is your name? Alif
how old are you? 29
are you a developer? (yes/no): yes

========================================
        PROFILE CONFIGURATION
========================================
Name:       Alif
Age:        29
Developer:  Yes
Clearance:  Tier 1: Admin Infrastructure Access
========================================
Welcome, Alif! You have been assigned Tier 1: Admin Infrastructure Access.
```

### Concepts practised

- `input()` to read user input, and type casting with `int()`
- Cleaning input with `.strip()` and `.lower()`
- `if` / `elif` / `else` with the logical operators `and` and `or`
- f-strings for formatted output

