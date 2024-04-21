def read_file(file_name):
    """
    Reads a file containing pairs of questions and answers and returns a list of dictionaries,
    where each dictionary contains a question and its corresponding answer.

    Args:
        file_name (str): The name of the file to be read.

    Returns:
        list: A list of dictionaries, each containing a "Question" key and an "Answer" key.
    """    
    dictionary_list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            question = lines[i].split(': ')[1].strip()
            answer = lines[i+1].split(': ')[1].strip()
            dictionary_list.append(
                {"Question": question, "Answer": answer})
    return dictionary_list
