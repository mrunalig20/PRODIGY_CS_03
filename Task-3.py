import re

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))
    
    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Assess the strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback
    feedback = {
        'length': length_criteria,
        'uppercase': uppercase_criteria,
        'lowercase': lowercase_criteria,
        'numbers': number_criteria,
        'special_characters': special_char_criteria
    }
    
    return strength, feedback

# Example usage
print("password's strength checker✅")
password = input("Enter the Password: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
print("Feedback on criteria met:")
for criterion, met in feedback.items():
    print(f"  {criterion}: {'Yes' if met else 'no'}")
