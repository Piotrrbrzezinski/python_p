import re

def find_all_authorizations(filename, url_params):
    # Wzorce regex do wyszukiwania Authorization
    auth_pattern = re.compile(r'"Authorization":\s*"([^"]+)"')
    
    results = {}
    
    for param in url_params:
        # Tworzenie wzorca URL dla każdego parametru
        url_pattern = re.compile(r'"url":\s*"https://abc/' + re.escape(param) + r'/')
        authorizations = []
        url_found = False
        
        with open(filename, 'r') as file:
            for line in file:
                if url_pattern.search(line):
                    url_found = True
                elif url_found and (match := auth_pattern.search(line)):
                    authorizations.append(match.group(1))
                    url_found = False  # Reset po znalezieniu, aby szukać kolejnych pasujących wzorców
        
        results[param] = authorizations
    
    return results

# Zahardkodowana lista parametrów qqq
url_params = ["qqq", "qqq2", "qqq3"]

# Nazwa pliku log
filename = 'test.log'

# Wywołaj funkcję i zapisz wyniki do słownika
auth_values = find_all_authorizations(filename, url_params)

# Wyświetl wszystkie znalezione wartości Authorization dla każdego parametru
for param, values in auth_values.items():
    if values:
        print(f"Wartości 'Authorization' dla '{param}':", values)
    else:
        print(f"Nie znaleziono URL-a lub wartości 'Authorization' dla parametru '{param}'.")
