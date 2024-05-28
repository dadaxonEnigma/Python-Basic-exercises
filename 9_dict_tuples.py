#First method
info = {
    'China': 143,
    'India':136,
    'Usa':32,
    'Pakistan':21
}

user_requests = input('Info, Add, Remove, Get: ').lower()

if user_requests == 'info':
    for key,val in info.items():
        print(f'{key}==>{val}')
if user_requests == 'add':
    user_requests = input('Which county you want add: ').title()
    if user_requests in info:
        print("This country has in our table")
    else:
        info[f'{user_requests}'] = int(input('Populations: '))
        info.update()
        print(info.items())
if user_requests == 'remove':
    user_requests = input('Which country you want remove: ').title()
    if user_requests in info:
        del info[f'{user_requests}']
        info.update()
        print(info.items())
    else:
        print('This country have not in our table')
if user_requests == 'get':
    user_requests = input('Which country you want to show: ').title()
    if user_requests in info:
        print(info[f'{user_requests}'])
    else:
        print('This country have not in our table')
        
        
#Second method
population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()
