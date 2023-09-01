# Password Storage Utility with Pass

This Python script is a simple utility for securely storing passwords using the [pass](https://www.passwordstore.org/) password manager. The script allows users to create and store password entries for different websites and user types. It also provides features for editing passwords (to be implemented in future updates).

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3
- [pass](https://www.passwordstore.org/) password manager installed and configured

## Getting Started

Follow these steps to use the password storage utility:

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory containing the script.

3. Make the script executable by running the following command:

   ```shell
   chmod +x password_storage_utility.py
   ```

4. Run the script:

   ```shell
   ./password_storage_utility.py
   ```

## Usage

1. When you run the script, it will prompt you for the following information:

   - Website name: Enter the name of the website for which you want to store the password.

   - User type (e.g., ericngigi/work): Specify the user type or category for the password. This can help organize your passwords if you have multiple accounts for the same website.

2. Next, you will be prompted to enter the following information:

   - Password: Enter the password you want to store securely.

   - URL (optional): You can optionally provide the URL associated with the website. If not provided, it will be stored as "(none)".

   - Username (optional): You can optionally provide your username for the website. If not provided, it will be stored as "(none)".

3. Once you have entered all the required information, the script will create a multiline password entry and store it using the `pass` password manager.

4. You will receive a confirmation message indicating that the password entry has been created successfully.

## Features to Come

Future updates to this script will include the ability to edit stored passwords.

## Important Notes

- Make sure you have configured `pass` properly and have set up your GPG key before using this utility.

- Ensure that you have a good understanding of how `pass` works, especially if you plan to use this utility to manage sensitive passwords.

- This script does not handle password generation; you should create strong, unique passwords using a password manager or generator before running the script.

- Always ensure the security of your system and passwords, and regularly back up your `pass` password store.

- Use this script responsibly and in compliance with any applicable laws and regulations.

**Disclaimer:** This utility is provided as-is and without warranty. Use it at your own risk.
