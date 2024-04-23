from licensing.fetch_licenses import fetch_licenses
import json

if __name__ == '__main__':
    data = fetch_licenses()
    print(json.dumps(data, indent=4))


