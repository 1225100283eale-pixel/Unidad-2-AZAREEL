inventario = [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]


#imprmir todos los Hostname
print("Hostnames:")
for equipo in inventario:
	print(equipo["hostname"])

#imprimir todas las IPS
print("ip:")
for I in inventario:
	print(I["ip"])

#imprimir todos los que  esten en down
print("status:")
for D in inventario:
	print(D["status"])
