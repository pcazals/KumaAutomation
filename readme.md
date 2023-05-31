README

Description

This Python script is designed to interact with the Uptime Kuma API. It allows you to add or delete HTTP monitors for domain names either manually or from a CSV file.

Prerequisites

To use this script, you will need:

Python 3.6 or higher installed on your machine.
The uptime_kuma_api Python package installed. You can install it using pip:
Copy code
pip install uptime_kuma_api
Access to an instance of Uptime Kuma, with the URL and login credentials available.
Usage

Import the UptimeKumaApi and MonitorType from the uptime_kuma_api package.
The script contains several functions:
add_monitors_from_csv(api, filename): This function reads a CSV file and adds HTTP monitors for each domain name listed in the file.
add_monitors_manually(api): This function allows you to manually input domain names for which HTTP monitors will be added.
delete_all_monitors(api): This function deletes all existing monitors.
main(): This function runs the script, prompting you to choose between adding or deleting monitors, and between manually inputting domain names or reading them from a CSV file.
To run the script, simply execute it in your Python environment. You will be prompted to enter your choice of operation (add or delete monitors) and your choice of input method (manual or CSV file).
Copy code
python your_script_name.py
If you choose to add monitors from a CSV file, make sure the CSV file contains one domain name per line, with no header row.
If you choose to add monitors manually, you will be prompted to enter each domain name individually. Enter 'quit' when you are finished.
If you choose to delete monitors, all existing monitors will be deleted without further confirmation.
Note

Please replace the api_url, username, and password in the main() function with your own Uptime Kuma URL and login credentials.

Disclaimer

Use this script responsibly. Adding or deleting monitors can affect the operation of your Uptime Kuma instance. Always ensure you have the necessary permissions and that you understand the implications of your actions.