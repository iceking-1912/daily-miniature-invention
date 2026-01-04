# Password Strength Checker

**Date:** January 4, 2026  
**Language:** Python 3  
**Author:** Himanshu

## Overview

A comprehensive password strength analyzer that evaluates passwords based on multiple security criteria and provides actionable feedback to improve password security.

## Features

- **Length Analysis**: Checks if password meets minimum length requirements
- **Character Diversity**: Verifies presence of lowercase, uppercase, digits, and special characters
- **Pattern Detection**: Identifies common weak patterns like sequential characters and repetitions
- **Entropy Calculation**: Measures true randomness using Shannon entropy
- **Security Score**: Provides 0-100 score with detailed rating
- **Actionable Feedback**: Gives specific suggestions to improve password strength

## How It Works

The analyzer uses multiple criteria to evaluate password strength:

1. **Length Score** (0-30 points)
   - < 6 characters: Very weak
   - 6-7 characters: Weak
   - 8-11 characters: Good
   - 12+ characters: Excellent

2. **Character Diversity** (0-45 points)
   - Lowercase letters: +10
   - Uppercase letters: +10
   - Numbers: +10
   - Special characters: +15

3. **Pattern Penalties** (-30 to 0 points)
   - Common passwords: -30
   - Sequential characters: -10
   - Repeated characters: -10

4. **Entropy Bonus** (0-15 points)
   - Rewards true randomness

## Usage

### Interactive Mode

```bash
python password_checker.py
```

Follow the prompts to enter passwords and receive instant feedback.

### As a Module

```python
from password_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker("MyP@ssw0rd123")
score, rating, feedback = checker.analyze()

print(f"Score: {score}/100")
print(f"Rating: {rating}")
for tip in feedback:
    print(tip)
```

## Example Output

```
==================================================
    PASSWORD STRENGTH ANALYZER
==================================================

Password: ************
Length: 12 characters

Strength Score: 85/100
Rating: Very Strong 💪

Entropy: 48.52 bits

Feedback:
  ✓ Excellent length
  ✓ Contains special characters

==================================================
```

## Security Tips

- Use at least 12 characters
- Mix uppercase, lowercase, numbers, and special characters
- Avoid common words and patterns
- Don't reuse passwords across sites
- Consider using a password manager
- Enable two-factor authentication when available

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Technical Details

**Entropy Calculation**: Uses Shannon entropy formula to measure the unpredictability of the password. Higher entropy indicates better randomness.

**Pattern Recognition**: Employs regex patterns to detect common weaknesses like sequential characters (123, abc) and repetitions (aaa, 111).

## License

MIT License - Feel free to use and modify as needed.
