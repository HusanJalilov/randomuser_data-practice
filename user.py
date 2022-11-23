import json
def get_users_by_country(data: dict, country: str) -> list[dict]:
    '''get users by country
    
    Args:
        data (dict): users data
        country (str): country name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
   
    user=[]
    for i in data['results']:

        if i['location']['country']==country:
            user.append({
                'full_name':f"{i['name']['title']} {i['name']['first']} {i['name']['last']}",
                'age':f"{i['dob']['age']}"
                })
    return user
    


def get_users_by_age(data: dict, age: int) -> list[dict]:
    '''get users by age
    
    Args:
        data (dict): users data
        age (int): age

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    age1=[]
    for i in data['results']:
       
        if i['dob']['age']==age:
            
            age1.append({
                'full_name':f"{i['name']['title']} {i['name']['first']} {i['name']['last']}",
                'age':f"{i['dob']['age']}"
                })
    return age1


def get_users_by_city(data: dict, city: str) -> list[dict]:
    '''get users by city
    
    Args:
        data (dict): users data
        city (str): city name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    ct=[]
    for i in data['results']:
       
        if i['location']['city']==city:
            
            ct.append({
                'full_name':f"{i['name']['title']} {i['name']['first']} {i['name']['last']}",
                'age':f"{i['dob']['age']}"
                })
    return ct


def get_users_by_nat(data: dict, nat: str) -> list[dict]:
    '''get users by nat
    
    Args:
        data (dict): users data
        nat (str): user nat

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    nt=[]
    for i in data['results']:
        
       
        if i['nat']==nat:
            
            nt.append({
                'full_name':f"{i['name']['title']} {i['name']['first']} {i['name']['last']}",
                'age':f"{i['dob']['age']}"
                })
    return nt
