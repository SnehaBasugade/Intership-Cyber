<<<<<<< HEAD
#  Heuristic-based scoring 
def calculate_phishing_score(url):
    """
    Returns phishing probability (0-100%) based on URL features.
    """
    score = 0
    url_lower = url.lower()

    # Rules for phishing
    if "@" in url: score += 30
    if "-" in url: score += 10
    if any(word in url_lower for word in ["login", "update", "secure", "verify", "account", "free", "money"]):
        score += 25
    if url_lower.startswith("http://"): score += 10  # Not HTTPS
    if len(url) > 50: score += 10  # Long URL
    if url.count('.') > 3: score += 10  # Too many subdomains
    if any(char.isdigit() for char in url.split("//")[-1]): score += 5  # digits in domain/path

    # Clamp score to 1-100
    score = max(0, min(score, 100))
    return score

#  Prediction function 
def predict_url(url):
    """
    Predict if a URL is phishing or legitimate.
    Uses 50% threshold.
    """
    score = calculate_phishing_score(url)

    #  Change threshold here if needed
    threshold = 50
    prediction = "Phishing 🚨" if score >= threshold else "Legitimate ✅"
    return score, prediction

#  Console test 
if __name__ == "__main__":
    while True:
        url = input("Enter URL (or 'exit'): ")
        if url.lower() == "exit": break
        score, pred = predict_url(url)
=======
#  Heuristic-based scoring 
def calculate_phishing_score(url):
    """
    Returns phishing probability (0-100%) based on URL features.
    """
    score = 0
    url_lower = url.lower()

    # Rules for phishing
    if "@" in url: score += 30
    if "-" in url: score += 10
    if any(word in url_lower for word in ["login", "update", "secure", "verify", "account", "free", "money"]):
        score += 25
    if url_lower.startswith("http://"): score += 10  # Not HTTPS
    if len(url) > 50: score += 10  # Long URL
    if url.count('.') > 3: score += 10  # Too many subdomains
    if any(char.isdigit() for char in url.split("//")[-1]): score += 5  # digits in domain/path

    # Clamp score to 1-100
    score = max(0, min(score, 100))
    return score

#  Prediction function 
def predict_url(url):
    """
    Predict if a URL is phishing or legitimate.
    Uses 50% threshold.
    """
    score = calculate_phishing_score(url)

    #  Change threshold here if needed
    threshold = 50
    prediction = "Phishing 🚨" if score >= threshold else "Legitimate ✅"
    return score, prediction

#  Console test 
if __name__ == "__main__":
    while True:
        url = input("Enter URL (or 'exit'): ")
        if url.lower() == "exit": break
        score, pred = predict_url(url)
>>>>>>> 6be99264d218af05c6ed951ba699d97a6e295199
        print(f"Phishing probability: {score:.2f}% | Prediction: {pred}")