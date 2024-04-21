from trainer import get_objectives_QA

def generate_menu(options_list):
    """
    Returns a list of options passed as arguments. 

    Args:
        options_list ([{str:str}]): a list of strings. Elements are the keys of a list of dictionaries

    Returns:
        [str]: a list of strings
    """
    return [questions['Question']for questions in options_list]

def generate_all_menus(): 
    """
    Generates all options menu for each objective

    Returns:
        _type_: _description_
    """    
    objective_1,objective_2,objective_3,objective_4 = get_objectives_QA()
    menu_objective_1 = generate_menu(objective_1)
    menu_objective_2 = generate_menu(objective_2)
    menu_objective_3 = generate_menu(objective_3)
    menu_objective_4 = generate_menu(objective_4)
    return menu_objective_1,menu_objective_2,menu_objective_3,menu_objective_4