import json

def get_input(prompt, default=None):
    value = input(prompt).strip()
    return value if value else default

def add_new_app(data):
    # Get user input for the new app
    name = get_input("Enter app name: ")
    bundle_identifier = get_input("Enter bundle identifier: ")
    developer_name = get_input("Enter developer name: ")
    subtitle = get_input("Enter subtitle: ")
    localized_description = get_input("Enter localized description: ")
    icon_url = get_input("Enter icon URL: ")
    screenshot_urls = get_input("Enter screenshot URLs (comma-separated): ").split(',')
    
    # Create new app entry
    new_app = {
        "name": name,
        "bundleIdentifier": bundle_identifier,
        "developerName": developer_name,
        "subtitle": subtitle,
        "localizedDescription": localized_description,
        "iconURL": icon_url,
        "screenshotURLs": [url.strip() for url in screenshot_urls],
        "versions": []
    }

    # Add the new app to the apps list
    if 'apps' not in data:
        data['apps'] = []
    data['apps'].append(new_app)

    # Ask to add versions to the new app
    while True:
        add_version = get_input("Do you want to add a version to the new app? (yes/no): ")
        if add_version.lower() == 'yes':
            add_version_to_app(new_app)
        else:
            break

def add_version_to_app(app):
    while True:
        # Get user input for the new version entry
        version = get_input("Enter version: ")
        date = get_input("Enter date (YYYY-MM-DD): ")
        localized_description = get_input("Enter localized description: ")
        download_url = get_input("Enter download URL: ")
        size = int(get_input("Enter size (in bytes): "))
        min_os_version = get_input("Enter minimum OS version: ")
        max_os_version = get_input("Enter maximum OS version: ")

        # Create new version entry
        new_version = {
            "version": version,
            "date": date,
            "localizedDescription": localized_description,
            "downloadURL": download_url,
            "size": size,
            "minOSVersion": min_os_version,
            "maxOSVersion": max_os_version
        }

        # Append the new version to the app
        app['versions'].append(new_version)

        # Ask if user wants to add another version
        cont = get_input("Do you want to add another version? (yes/no): ")
        if cont.lower() != 'yes':
            break

def update_existing_app(data):
    # Display available apps
    if 'apps' not in data or not data['apps']:
        print("No apps found in the JSON file.")
        return

    for index, app in enumerate(data['apps']):
        print(f"{index + 1}: {app.get('name', 'Unknown')}")

    # Choose which app to update
    choice = int(get_input("Enter the number of the app you want to update: ")) - 1

    if choice < 0 or choice >= len(data['apps']):
        print("Invalid choice.")
        return

    app = data['apps'][choice]

    while True:
        # Get user input for the new version entry
        version = get_input("Enter version: ")
        date = get_input("Enter date (YYYY-MM-DD): ")
        localized_description = get_input("Enter localized description: ")
        download_url = get_input("Enter download URL: ")
        size = int(get_input("Enter size (in bytes): "))
        min_os_version = get_input("Enter minimum OS version: ")
        max_os_version = get_input("Enter maximum OS version: ")

        # Create new version entry
        new_version = {
            "version": version,
            "date": date,
            "localizedDescription": localized_description,
            "downloadURL": download_url,
            "size": size,
            "minOSVersion": min_os_version,
            "maxOSVersion": max_os_version
        }

        # Append the new version to the selected app
        if 'versions' not in app:
            app['versions'] = []
        app['versions'].append(new_version)

        # Save the updated JSON data
        with open('input.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Ask if user wants to add another version
        cont = get_input("Do you want to add another version? (yes/no): ")
        if cont.lower() != 'yes':
            break

def remove_app(data):
    # Display available apps
    if 'apps' not in data or not data['apps']:
        print("No apps found in the JSON file.")
        return

    for index, app in enumerate(data['apps']):
        print(f"{index + 1}: {app.get('name', 'Unknown')}")

    # Choose which app to remove
    choice = int(get_input("Enter the number of the app you want to remove: ")) - 1

    if choice < 0 or choice >= len(data['apps']):
        print("Invalid choice.")
        return

    # Remove the selected app
    del data['apps'][choice]

def update_app_details(data):
    # Display available apps
    if 'apps' not in data or not data['apps']:
        print("No apps found in the JSON file.")
        return

    for index, app in enumerate(data['apps']):
        print(f"{index + 1}: {app.get('name', 'Unknown')}")

    # Choose which app to update
    choice = int(get_input("Enter the number of the app you want to update details for: ")) - 1

    if choice < 0 or choice >= len(data['apps']):
        print("Invalid choice.")
        return

    app = data['apps'][choice]

    # Update app details
    app['name'] = get_input(f"Enter new name (current: {app.get('name')}): ", app.get('name'))
    app['bundleIdentifier'] = get_input(f"Enter new bundle identifier (current: {app.get('bundleIdentifier')}): ", app.get('bundleIdentifier'))
    app['developerName'] = get_input(f"Enter new developer name (current: {app.get('developerName')}): ", app.get('developerName'))
    app['subtitle'] = get_input(f"Enter new subtitle (current: {app.get('subtitle')}): ", app.get('subtitle'))
    app['localizedDescription'] = get_input(f"Enter new localized description (current: {app.get('localizedDescription')}): ", app.get('localizedDescription'))
    app['iconURL'] = get_input(f"Enter new icon URL (current: {app.get('iconURL')}): ", app.get('iconURL'))
    screenshot_urls = get_input(f"Enter new screenshot URLs (comma-separated, current: {', '.join(app.get('screenshotURLs', []))}): ", ', '.join(app.get('screenshotURLs', []))).split(',')
    app['screenshotURLs'] = [url.strip() for url in screenshot_urls]

def main():
    # Load existing JSON data
    with open('input.json', 'r') as file:
        data = json.load(file)

    while True:
        # Provide options to the user
        action = get_input("Choose:\n1: Add a new app\n2: Add a new update to an existing app\n3: Remove an app\n4: Update app details\nEnter your choice: ")

        if action == '1':
            add_new_app(data)
        elif action == '2':
            update_existing_app(data)
        elif action == '3':
            remove_app(data)
        elif action == '4':
            update_app_details(data)
        else:
            print("Invalid choice.")
            continue

        # Save the updated JSON data
        with open('input.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Ask if user wants to perform another action
        cont = get_input("Do you want to perform another action? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

