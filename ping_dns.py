#pip install ping3 para instalar o pacote
from ping3 import ping

#Colocar entre " " os endereços de ip dos dns
hostnames = ["208.67.222.222",
             "208.67.220.220",
             "1.1.1.1",
             "1.0.0.1",
             "8.8.8.8",
             "8.8.4.4",
             "9.9.9.9",
             "149.112.112.112",
             "176.103.130.130",
             "176.103.130.131",
             "185.228.168.9",
             "185.228.169.9",
            ]

#lista com os valores do ping
resp_list = []

#Para cada IP ele faz o ping
for name in hostnames:
    response = ping(name)
    if response == False:
        resp_list.append(1000)
    else:
        resp_list.append(response)
        
#Transforma um dict e ordenar ele pelo menor valor do ping
host_resp = dict(zip(resp_list,hostnames))
min_resp = sorted(host_resp.keys())

#Mostra na tela os valores em ordem crescente
print("Sorted by best time response ping:")
print("{:<15}\t-\t{:<25}".format("HostName","Ping"))
print("_______________________________________")
for time in min_resp:
    print("{:<15}\t-\t{:<18}".format(host_resp[time],time))
