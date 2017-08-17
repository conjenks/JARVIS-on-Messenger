def process(input, entities=None):
    output = {}

    message = "This is the Word of the Day."

    output['input'] = input
    output['output'] = message
    output['success'] = True

    return output