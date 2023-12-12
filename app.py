#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import requests
import json
import time

def get_air_quality_data(location):
    """Pobiera dane o jakości powietrza dla podanej lokalizacji z API OpenAQ."""
    url = "https://api.openaq.org/v2/measurements?location_id=10566&parameter=o3&parameter=pm25&parameter=bc&parameter=co&parameter=so2&parameter=no2&parameter=pm10&limit=7"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    else:
        return None

def main():
    """Główna funkcja modułu."""
    location = "Wroclaw, Lower Silesian Voivodeship, Poland"
    while True:
        data = get_air_quality_data(location)
        if data is not None:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            values = []
            for measurement in data["results"]:
                values.append({"nazwa-pomiaru": measurement["parameter"], "wartosc [ug/m^3]": measurement["value"]})
            message = {"location": location, "timestamp": timestamp, "values": values}
            print(json.dumps(message, indent=4))
            time.sleep(30)

if __name__ == "__main__":
    main()