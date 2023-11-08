import requests

url_api = "http://18.218.244.166:8080/api/v2/import-scan"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def upload_and_import_report(product_name, engagement_name, product_type_name=None, auto_create_context=True):
    headers = {
        'Authorization': api_key
    }

    
        with open('report.json', 'rb') as report_file:
            files = {'file': ('report.json', report_file, 'application/json')}
            data = {
                "product_name": product_name,
                "engagement_name": engagement_name,
                "product_type_name": product_type_name,
                "auto_create_context": auto_create_context
            }
            r = requests.post(url_api, headers=headers, data=data, files=files, verify=False)
            if r.status_code == 201:
                print("Reporte cargado")
            else:
                print("Error: ", r.status_code)
                print("Respuesta del servidor:", r.text)
    except FileNotFoundError:
        print("El archivo no existe.")

if __name__ == '__main':
    product_name = "Escaneo con Trivy"  
    engagement_name = "Trivy"  
    product_type_name = "Reporte"  
    upload_and_import_report(product_name, engagement_name, product_type_name)
