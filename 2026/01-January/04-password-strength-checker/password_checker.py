#!/usr/bin/env python3
"""
Password Strength Checker
=========================

A comprehensive password strength analyzer that evaluates passwords based on:
- Length (minimum 8 characters recommended)
- Character diversity (uppercase, lowercase, digits, special characters)
- Common patterns and sequences
- Entropy calculation for randomness

Author: Himanshu
Date: January 4, 2026
"""

import re
import math
from typing import Tuple, List


class PasswordStrengthChecker:
    """Analyzes password strength and provides security feedback."""
    
    # Common weak passwords and patterns
    COMMON_PASSWORDS = [
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', '1234567', 'letmein', 'trustno1', 'dragon'
    ]
    
    def __init__(self, password: str):
        self.password = password
        self.length = len(password)
        self.score = 0
        self.feedback = []
    
    def calculate_entropy(self) -> float:
        """Calculate Shannon entropy to measure password randomness."""
        if not self.password:
            return 0.0
        
        # Count character frequencies
        freq = {}
        for char in self.password:
            freq[char] = freq.get(char, 0) + 1
        
        # Calculate entropy
        entropy = 0.0
        for count in freq.values():
            probability = count / self.length
            entropy -= probability * math.log2(probability)
        
        return entropy * self.length
    
    def check_length(self) -> int:
        """Award points based on password length."""
        if self.length < 6:
            self.feedback.append("❌ Too short (minimum 8 characters recommended)")
            return 0
        elif self.length < 8:
            self.feedback.append("⚠️  Short (consider using 12+ characters)")
            return 10
        elif self.length < 12:
            self.feedback.append("✓ Good length")
            return 20
        else:
            self.feedback.append("✓ Excellent length")
            return 30
    
    def check_character_diversity(self) -> int:
        """Check for different character types."""
        points = 0
        
        if re.search(r'[a-z]', self.password):
            points += 10
        else:
            self.feedback.append("⚠️  Add lowercase letters")
        
        if re.search(r'[A-Z]', self.password):
            points += 10
        else:
            self.feedback.append("⚠️  Add uppercase letters")
        
        if re.search(r'\d', self.password):
            points += 10
        else:
            self.feedback.append("⚠️  Add numbers")
        
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'"\\|,.<>/?]', self.password):
            points += 15
            self.feedback.append("✓ Contains special characters")
        else:
            self.feedback.append("⚠️  Add special characters (!@#$%^&*)")
        
        return points
    
    def check_patterns(self) -> int:
        """Check for common weak patterns."""
        penalty = 0
        
        # Check for common passwords
        if self.password.lower() in self.COMMON_PASSWORDS:
            self.feedback.append("❌ This is a commonly used password")
            penalty += 30
        
        # Check for sequential characters
        if re.search(r'(012|123|234|345|456|567|678|789|abc|bcd|cde)', 
                    self.password.lower()):
            self.feedback.append("⚠️  Contains sequential characters")
            penalty += 10
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', self.password):
            self.feedback.append("⚠️  Contains repeated characters")
            penalty += 10
        
        return -penalty
    
    def analyze(self) -> Tuple[int, str, List[str]]:
        """Perform complete password analysis."""
        # Calculate base score
        self.score += self.check_length()
        self.score += self.check_character_diversity()
        self.score += self.check_patterns()
        
        # Add entropy bonus
        entropy = self.calculate_entropy()
        entropy_bonus = min(15, int(entropy / 4))
        self.score += entropy_bonus
        
        # Ensure score is within bounds
        self.score = max(0, min(100, self.score))
        
        # Determine strength rating
        if self.score < 30:
            rating = "Very Weak 💀"
        elif self.score < 50:
            rating = "Weak 😟"
        elif self.score < 70:
            rating = "Moderate 😐"
        elif self.score < 85:
            rating = "Strong 😊"
        else:
            rating = "Very Strong 💪"
        
        return self.score, rating, self.feedback


def check_password_strength(password: str) -> None:
    """Check and display password strength analysis."""
    print("\n" + "="*50)
    print("    PASSWORD STRENGTH ANALYZER")
    print("="*50 + "\n")
    
    checker = PasswordStrengthChecker(password)
    score, rating, feedback = checker.analyze()
    entropy = checker.calculate_entropy()
    
    print(f"Password: {'*' * len(password)}")
    print(f"Length: {len(password)} characters\n")
    
    print(f"Strength Score: {score}/100")
    print(f"Rating: {rating}\n")
    
    print(f"Entropy: {entropy:.2f} bits\n")
    
    print("Feedback:")
    for item in feedback:
        print(f"  {item}")
    
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    # Interactive mode
    print("\n🔐 Welcome to Password Strength Checker!\n")
    
    while True:
        password = input("Enter password to check (or 'quit' to exit): ")
        
        if password.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using Password Strength Checker!\n")
            break
        
        if not password:
            print("⚠️  Please enter a password.\n")
            continue
        
        check_password_strength(password)
        
        # Ask for another check
        again = input("Check another password? (y/n): ")
        if again.lower() not in ['y', 'yes']:
            print("\nThank you for using Password Strength Checker!\n")
            break
