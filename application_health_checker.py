import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Application is UP!")
        else:
            print(f"⚠️ Application might have issues. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Application is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    app_url = input("Enter the application URL: ")
    check_application_health(app_url)
