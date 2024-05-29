# Dummy data for battery information (replace with actual data)
battery_data = {
    "123": {
        "Manufacturing Date": "2022-04-15",
        "Manufacturer": "XYZ Batteries",
        "Model Number": "PowerCell 5000",
        "Serial Number": "SN123",
        "Weight": 150,
        "Operating Temperature Range": "-10°C to 50°C",
        "Storage Temperature": "-20°C to 60°C",
        "Humidity": "30% to 80%",
        "Charge Cycles": 100,
        "Health Percentage": 96,
        "Last Communication Timestamp": "2024-05-28T10:30:00Z"
    }
}

def get_battery_info(access_token,bike_id=None):
    # MAKE REQUEST to get battery info api Api on batteryserver
    #   Define the URL for your API endpoint
    #   batteryerver_url = "http://localhost:8800/info"

    # Set the authorization header with the bearer token
    #    headers = {
    #            "Authorization": f"Bearer {access_token}"
    #    }

    # Make the POST request
    #    response = requests.post(url, headers=headers)
    #    return response.json()

    return battery_data['123']



battery_stats = { 
    "123": {
        "Capacity (mAh or Ah)": 5000,
        "Voltage (V)": 3.7,
        "Energy Density (Wh/kg)": 150,
        "Specific Energy (Wh/L)": 300,
        "Cycle Life": 1000,
        "Depth of Discharge (DoD)": 80,
        "Self-Discharge Rate": 1,
        "Internal Resistance (Ohms)": 0.02,
        "Remaining Capacity": 4800,
        "Cloud Connectivity (MQTT status)": "Connected",
        "Battery Location (GPS coordinates)": {
            "latitude": 37.7749,
            "longitude": -122.4194
            }
    }
}

def get_battery_stats(access_token=None,bike_id=None):
    # MAKE REQUEST to get battery info api Api on batteryserver
    #   Define the URL for your API endpoint
    #   batteryerver_url = "http://localhost:8800/stats"

    # Set the authorization header with the bearer token
    #    headers = {
    #            "Authorization": f"Bearer {access_token}"
    #    }

    # Make the POST request
    #    response = requests.post(url, headers=headers)
    #    return response.json()

    return battery_stats['123']


battery_contorl_param = {    
    "123":{
        "Start/Stop Charging": "start",  # Example value (options: "start", "stop")
        "Adjust Charging Rate": 50,  # Example value (percentage)
        "Discharge Limit": 30,  # Example value (percentage)
        "SoC Target": 80,  # Example value (percentage)
        "SoC Balancing": True,
        "Cooling/Heating": "auto",  # Example value (options: "auto", "on", "off")
        "Grid Connection/Isolation": False,
        "Grid Frequency Regulation": "adaptive",  # Example value (options: "adaptive", "fixed")
        "Emergency Shutdown": False,
        "Fault Handling": "alert",  # Example value (options: "alert", "ignore")
        "Remote Firmware Updates": True,
        "Load Scheduling": "peak_hours",  # Example value (options: "peak_hours", "off_peak")
        "Critical Load Support": True,
        "Health Monitoring": "good",  # Example value (options: "good", "warning", "critical")
        "Scheduled Maintenance": "monthly"  # Example value (options: "daily", "weekly", "monthly")
    }
}

def set_battery_settings(access_token,params,bike_id=None):
    # MAKE REQUEST to get battery info api Api on batteryserver
    #   Define the URL for your API endpoint
    #   batteryerver_url = "http://localhost:8800/control"

    # Set the authorization header with the bearer token
    #    headers = {
    #            "Authorization": f"Bearer {access_token}"
    #    }

    # Make the POST request
    #    response = requests.post(url, headers=headers,payload=params)
    #    return response.json()
    battery_contorl_param['123'] = params
    return {'error': 'success'}

def get_battery_settings(access_token,bike_id=None):
    # MAKE REQUEST to get battery info api Api on batteryserver
    #   Define the URL for your API endpoint
    #   batteryerver_url = "http://localhost:8800/control"

    # Set the authorization header with the bearer token
    #    headers = {
    #            "Authorization": f"Bearer {access_token}"
    #    }

    # Make the POST request
    #    response = requests.get(url, headers=headers)
    #    return response.json()
    return battery_contorl_param['123']