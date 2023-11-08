import requests
import json

url_api = "http://18.218.244.166:8080/api/v2/import-scan/"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def upload_report():
    headers = {
        'accept': 'application/json',
        'Authorization': api_key
    }

    reports = {
        'file': open('/home/kali/report-trivy.json', 'rb')
        'product_name': 'Prueba',
        'engagement_name': 'Prueba',
        'product_type_name': 'Prueba',
        'auto_create_context': 'auto_create_context',
        'active': True,
        'verify': True,
        'scan_type': 'Trivy-scan'

    }

        r = requests.post(url_api format(method = 'import-scan'), headers=headers, data=data, verify=False)

        if r.status_code == 201:
            print("Informe cargado exitosamente.")
        else:
            print("Error al cargar el informe. Código de estado:", r.status_code)
            print("Respuesta del servidor:", r.text)
    except FileNotFoundError:
        print("El archivo 'report.trivy.json' no se encontró. Asegúrate de que el archivo esté en la ubicación correcta.")

if __name__ == '__main':
    upload_report()

"""
import requests
import json

url_api = "http://18.218.244.166:8080/api/v2/import-scan/"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def upload_report():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': api_key
    }

    body = {
        'file': open('/home/kali/Lab-DSO/report.trivy.json', 'rb'),
        'active': True,
        'verfied': True
        'scan_type': Trivy-scan
    }

    with open('/home/kali/Lab-DSO/report-trivy.json', 'rb') as report:
        r = requests.post(url_api.format(method = 'import-scan'), files = report, headers = headers) 

    if r.status_code = 201:
            print(json.dumps(r.json(), indent=4))

if __name__ == '__main':
    upload_report()
"""

"""
    try:
        with open('report.json', 'rb') as report_file:
            files = {'file': ('report.json', report_file, 'application/json')}
            r = requests.post(url_api, headers=headers, files=files, verify=False)
            if r.status_code == 201:
                print("Todo bien.")
            else:
                print("Error: ", r.status_code)

    except FileNotFoundError:
        print("El archivo no existe.")
"""