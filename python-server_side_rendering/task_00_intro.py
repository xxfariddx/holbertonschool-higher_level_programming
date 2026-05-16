def generate_invitations(template_content, attendees):
    def empty_data(template, dictionary, element):
        try:
            placeholder = '{' + element + '}'
            return(template.replace(placeholder, check_el(dictionary[element])))
        except KeyError:
            return(template.replace(placeholder, 'N/A'))
    
    def check_el(element):
        if element == None:
            return ('N/A')
        return (element)

    n = 1

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i in attendees:
        template = template_content

        if not isinstance(template, str):
            print(f"Error: template must be a string, got {type(template)}")
            return
        
        if not isinstance(attendees, list):
            print(f"Error: attendees must be a list, got {type(attendees)}")
            return
        
        if not isinstance(i, dict):
            print(f"Error: list must contain dictionaries, got {type(item)}")
            return

        if len(template) == 0:
            print("Template is empty, no output files generated.")
            return

        template = empty_data(template, i, 'name')
        template = empty_data(template, i, 'event_title')
        template = empty_data(template, i, 'event_date')
        template = empty_data(template, i, 'event_location')

        output = 'output_' + str(n) + '.txt'
        with open(output, 'w') as file:
            file.write(template)

        n += 1
