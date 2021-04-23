data_list = {
    'tanggal':'2021-04-20',
    'driver_list':[
        {'nama':'Eko', 'jarak':10},
        {'nama':'Dwi', 'jarak':30},
        {'nama':'Tri', 'jarak':50},
        {'nama':'Catur', 'jarak':100}
    ]
}

print(data_list)
print(f"Driver sekitar sini {data_list['driver_list']}")
print(f"Driver #1 {data_list['driver_list'][0]}")
print(f"Driver #4 {data_list['driver_list'][3]}")
print(f"Jarak Driver terdekat {data_list['driver_list'][0]['jarak']}")