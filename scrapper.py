
import requests
from bs4 import BeautifulSoup
from decimal import *

r = requests.get('https://www.cambioschaco.com.py') #Url de donde obtener los datos
soup = BeautifulSoup(r.text, 'html.parser')


#tbody id="main-exchange-content"
#Dolar: id="exchange-usd" , venta: class="sale"
cotizaciones = soup.find_all('span', class_="sale", limit = 4) #Sector de la estructura html donde se encuentran los datos

monedas = ["Dolar", "Real", "Peso", "Euro"]
i = 0
ch = []
#Printeo de las monedas del dia obtenidas
for moneda in cotizaciones:
    print(f"{i+1}.- {monedas[i]}: {moneda.text}")
    ch.append(float(moneda.text))
    i += 1
#Convertor
a = 0
while a <= 0 or a > 4:
    a = int(input("Cual deseas convertir: "))
b = (input(f"Cuantos {monedas[a-1]}: "))
b = float(b.replace(",",'.'))
getcontext().prec = 6
r = Decimal(b) * Decimal(ch[a-1])
print("Resultados:")
print(f"{b} {monedas[a-1]} son {r} Guaranies")