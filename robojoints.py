import requests
from requests.auth import HTTPDigestAuth
import time

# Robot Web Service configurations.
url_joint_positions = 'http://localhost:8081/rw/motionsystem/mechunits/ROB_1/jointtarget'
username = 'Default User'
password = 'robotics'

# endless loop (stop with Ctrl-C)
try:
    while True:
        params = {'json': '1'}
        response = requests.get(
            url_joint_positions,
            auth=HTTPDigestAuth(username, password),
            params=params
        )

        print(response.status_code)
        jointAngles = {'api_key': 'YBAFOM906CBFRBBA'}
        # Check that response is OK
        if response.status_code == 200:
            data = response.json()
            joint_data = data["_embedded"]["_state"][0]  # Information of the joints is here
            

            # Print the axis angles  
            for i in range(1, 7):
                print(f"Joint {i}: {joint_data[f'rax_{i}']}")
                jointAngles[f"field{i}"] = float(joint_data[f'rax_{i}'])

            print(jointAngles)

            print("-" * 30)  
        else:
            print(f"Error: {response.status_code}")

        time.sleep(10)  # Wait 1 second
        print(jointAngles)
        response = requests.post('http://localhost:3001/api/measurements',json=jointAngles)
        print(response.ok)
        print(response.json())

except KeyboardInterrupt:
    print("\nProgram stopped.")
