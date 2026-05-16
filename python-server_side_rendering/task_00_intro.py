#!/usr/bin/python3
import os

"""
    Generate invitations based on a template and a list of attendees.

    Args:
    template (str): The invitation template as a string.
    attendees (list): A list of dictionaries.

    Raises:
    ValueError: If the template is not a string, if the attendees list
    is not a list, if any item in the attendees list is not a dictionary,
    or if the template is empty.
"""


def generate_invitations(template, attendees):

    # Several checks...
    try:
        if not isinstance(template, str):
            raise ValueError("[ERROR] - Template should be a string.")

        if not template.strip():
            raise ValueError(
                "[ERROR] - Template string should not be empty or just spaces."
            )

        if not isinstance(attendees, list):
            raise ValueError("[ERROR] - Template should be a string.")

        if not attendees:
            raise ValueError("[ERROR] - Attendees list should not be empty.")

        for item in attendees:
            if not isinstance(item, dict):
                raise ValueError(
                    "[ERROR] - Attendees should be a list of dictionaries."
                    )

        template_content = template

        if not template_content.strip():
            print("Template is empty, no output files generated.")
            return

    except ValueError as err:
        print(err)
        return

    # Check for missing keys in the attendees list and update them with "N/A"
    for item in attendees:
        if not item.get("name"):
            item.update({"name": "N/A"})
        if not item.get("event_title"):
            item.update({"event_title": "N/A"})
        if not item.get("event_date"):
            item.update({"event_date": "N/A"})
        if not item.get("event_location"):
            item.update({"event_location": "N/A"})

    counter = 1

    for item in attendees:
        invitation = template_content
        invitation = invitation.replace("{name}", item["name"])
        invitation = invitation.replace("{event_title}", item["event_title"])
        invitation = invitation.replace("{event_date}", item["event_date"])
        invitation = invitation.replace(
            "{event_location}", item["event_location"])

        output_filename = f"output_{counter}.txt"
        with open(output_filename, 'w') as file:
            file.write(invitation)

        counter += 1
