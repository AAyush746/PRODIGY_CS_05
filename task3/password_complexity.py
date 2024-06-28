import re
common_words = [
    "password", "123456", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123",
    "football", "monkey", "letmein", "dragon", "iloveyou", "admin", "welcome", "1234",
    "master", "sunshine", "photoshop", "1qaz2wsx", "princess", "azerty", "000000", "passw0rd",
    "123123", "654321", "superman", "qazwsx", "michael", "ashley", "q1w2e3r4", "baseball",
    "shadow", "mickey", "password1", "internet", "cheese", "matrix", "secret", "mustang",
    "111111", "2000", "access", "letmein1", "1234567890", "987654321", "whatever", "1111",
    "123", "test", "root", "summer", "hello", "freedom", "charlie", "donald", "123qwe",
    "qwertyuiop", "1212", "login", "123321", "dragon1", "loveme", "flower", "tigger",
    "killer", "pepper", "ginger", "batman", "maggie", "sparky", "cookie", "bailey", "apple",
    "banana", "chocolate", "coffee", "music", "password123", "admin123", "pass", "iloveyou1",
    "monkey1", "starwars", "jordan", "thomas", "asdfgh", "samsung", "hunter", "buster",
    "soccer", "killer1", "superman1", "fishing", "pepper1", "ginger1", "shadow1", "mickey1"
]
def remove_num_char(username):
    cleaned_String=re.sub(r'[^a-zA-Z]','',username)
    return cleaned_String

def passchecker(password,username):
    if len(password)<12:
        return "not strong:password is less than 12 words"
    
    if not re.search(r"[a-z]",password):
        return "not strong:password must contain at least one uppercase letter"
    if not re.search(r"[A-Z]",password):
        return "not strong:password must contain at least one uppercaase"
    if not re.search(r"[0-9]",password):
        return "not strong:password must contain at least one digit"
    if not re.search(r"[!@#$%^&*()]",password):
        return "not strong:password must contain at least one special character"
    if ((username.lower() in password.lower()) or (remove_num_char(username).lower() in password.lower())) :
        return "not strong :password starts with your username"
    for word in common_words:
        if word in password:
            return "not strong:password contains common word " 
            
            
    return "password is strong"
