company_info = {
    'Company': 'Mini Solutions LLC',
    'Address': {
        'Bangalore': {'koramangla': "Raheja Arcade", "Indiranagar": 'Bagmane tech part'}
    },
    'Departments': {
        'IT': {
            'Team Lead': 'Alice Johnson',
            'Members': {
                'Employee1': 'Bob Smith',
                'Employee2': 'Charlie Davis'
            }
        },
        'HR': {
            'Team Lead': 'Diana Adams',
            'Members': {
                'Employee1': 'Eva Green',
                'Employee2': 'Frank Harris'
            }
        }
    }
}

def fetch_data(dct:dict):
    for i,j in dct.items():

        if isinstance(j,dict) == True:
            print(f"{i}>>>",end  = " ")
            fetch_data(j)
        elif isinstance(j,str):
            print(f"{i}>>",j)

re = fetch_data(company_info)
