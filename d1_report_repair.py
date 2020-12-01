from utils import int_input_reader

'''
Task-specific variables
'''
expenses = int_input_reader('d1_data.txt')
sum_target = 2020

def sum_of_two_terms(l, sum_target):
    '''
    Given a list of terms and a sum_target, finds two terms that sum up to sum_target.
    '''
    result = []
    for term in l:
        first_term = term 
        second_term = sum_target - first_term
        if second_term in l:
            result.append(first_term)
            result.append(second_term)
    return set(result)

def multiply_two_terms_of_a_set(set_of_two_terms):
    '''
    Takes the terms satisfying the conditions in sum_of_two_terms() and multiplies them.
    '''
    terms = list(set_of_two_terms)
    result = terms[0]*terms[1]
    return result

def multiply_terms_of_a_list(l, l_size, sum_target):
    '''
    Looks for three terms in a list that sum up to sum_target.
    If they are found, it multiplies them.
    '''
    for i in range(0, l_size-2):
        for j in range(i+1, l_size-1):
            for k in range(j+1, l_size):
                if l[i] + l[j] + l[k] == sum_target:
                    return l[i] * l[j] * l[k]
    return False

terms = sum_of_two_terms(expenses, sum_target)
multiply_two_terms_of_a_set(terms)
multiply_terms_of_a_list(expenses, len(expenses), sum_target)