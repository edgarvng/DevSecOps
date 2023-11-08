import requests
import json

url_api = "http://18.218.244.166:8080/api/v2/products"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def create_product():
    headers = {
        'Content-Type': 'application/json',
        'accept:': 'application/json',
        'Authorization': api_key
    }

    data = {
    "tags": ["electronicos", "tecnologia"],
    "name": "App Vulnerable",
    "description": "App.",
    "prod_numeric_grade": 2147483647,
    "business_criticality": "high",
    "platform": "Web",
    "lifecycle": "production",
    "origin": "Unknow",
    "user_records": 2147483647,
    "revenue": "5000",
    "external_audience": False,
    "internet_accessible": True,
    "enable_product_tag_inheritance": False,
    "enable_simple_risk_acceptance": True,
    "enable_full_risk_acceptance": False,
    "disable_sla_breach_notifications": False,
    "product_manager": 1,
    "technical_contact": 2,
    "team_manager": 3,
    "prod_type": 1,
    "sla_configuration": 2,
    "regulations": [0]
}

    r = requests.post(url_api, headers=headers, data=json.dumps(data), verify=False)
    
    if r.status_code == 200:
        print("Producto creado exitosamente.")
    else:
        print("Error: ", r.status_code)

if __name__ == '__main__':
    create_product()