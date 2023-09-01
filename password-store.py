#!/usr/bin/env python3

import subprocess


def create_multiline_pass_entry(website, user_type):
    try:
        # Prompt the user for password, URL, and username
        password = input("Enter password: ")
        print("\033[F\033[KEnter password:", end="")

        # Validate website, user_type, and password are not blank
        if not website.strip():
            print("Website cannot be blank.")
            return
        if not user_type.strip():
            print("User type cannot be blank.")
            return
        if not password.strip():
            print("\nPassword cannot be blank.")
            return

        url = input("\nURL: ")
        username = input("Username: ")

        # Replace empty URL and username with "(none)"
        url = url if url else "(none)"
        username = username if username else "(none)"

        # Construct the multiline entry
        multiline_entry = f"{password}\nURL: {url}\nUsername: {username}"

        # Generate the command to insert the multiline entry into pass
        insert_command = (
            f'echo "{multiline_entry}" | pass insert --multiline {website}/{user_type}'
        )
        subprocess.run(insert_command, shell=True, check=True)
        print("Password entry created successfully.")
    except subprocess.CalledProcessError:
        print("An error occurred while creating the password entry.")


if __name__ == "__main__":
    website = input("Enter website name: ")
    user_type = input("Enter user type (ericngigi/work): ")
    create_multiline_pass_entry(website, user_type)
