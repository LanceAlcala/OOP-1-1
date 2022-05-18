import pyodbc
msa_drivers = [x for x in pyodbc.drivers() if 'access']

print(f'MS-ACCESS Drivers:{msa_drivers}')