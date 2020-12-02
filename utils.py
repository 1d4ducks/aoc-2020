def int_input_reader(task_input):
    '''
    Reads integers from lines of a txt file and returns a list of integers.
    '''
    with open(task_input) as f:
        task_input_as_list_of_ints = []
        for line in f:
            task_input_as_list_of_ints.append(int(line.strip()))
    return task_input_as_list_of_ints

def input_reader(task_input):
    '''
    Reads generic lines of a txt file and returns a list containing each line.
    '''
    with open(task_input) as f:
        task_input_as_list= []
        for line in f:
            task_input_as_list.append(line.strip())
    return task_input_as_list