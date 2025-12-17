<<<<<<< HEAD
def url_length(url):
    return len(url)

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def count_digits(url):
    return sum(c.isdigit() for c in url)

def has_at_symbol(url):
    return 1 if '@' in url else 0

def extract_features(url):
    return [
        url_length(url),
        count_dots(url),
        count_hyphens(url),
        count_digits(url),
        has_at_symbol(url)
    ]
=======
def url_length(url):
    return len(url)

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def count_digits(url):
    return sum(c.isdigit() for c in url)

def has_at_symbol(url):
    return 1 if '@' in url else 0

def extract_features(url):
    return [
        url_length(url),
        count_dots(url),
        count_hyphens(url),
        count_digits(url),
        has_at_symbol(url)
    ]
>>>>>>> 6be99264d218af05c6ed951ba699d97a6e295199
    