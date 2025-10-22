#COT Prompt
# Write a function that checks whether every element in the list l is less than the threshold t.  
# If all numbers are below t, return True; otherwise, return False.  

# Reason step-by-step about how to solve this before writing the final code.
# Finally, provide the Python function implementation.

def gemini_cot_pass1(l:list, t: int):
    return all(item < t for item in l)

def gemini_cot_pass2(l,t):
    for item in l:
        # Check for the failure condition (not strictly less than t)
        if item >= t:
            return False
    
    # If the loop completes without finding any failures, all items passed.
    return True

def gemini_cot_pass3(l,t):
    return sum(item < t for item in l) == len(l)

def claude_cot_pass1(l, t):
    return all(x < t for x in l)

def claude_cot_pass2(l,t):
    for element in l:
        if element >= t:
            return False
    return True

def claude_cot_pass3(l,t):
    return not any(x >= t for x in l)


#SD Prompt
# Write a function that checks whether every element in the list l is less than the threshold t. 
# If all numbers are below t, return True; otherwise, return False. Review the approach. Critique that approach
# by consideing an alternative method, and finally conclude by selelcting the most effective solution. After the 
# self debate, provide the python implementation of the function alone.

def gemini_sd_pass1(l:list, t: int):
    return all(num < t for num in l)

def gemini_sd_pass2(l,t):
    for element in l:
        if element >= t:
            # Found an element that is NOT less than the threshold
            return False
    # If the loop completes without returning False, all elements satisfy the condition
    return True

def gemini_sd_pass3(l,t):
    fails_condition = any(element >= t for element in l)
    
    # If no element fails, the condition (all elements < t) is True
    return not fails_condition

def claude_sd_pass1(l,t):
    return all(x < t for x in l)

def claude_sd_pass2(l,t):
    for element in l:
        if element >= t:
            return False
    return True

def claude_sd_pass3(l,t):
    return not any(element >= t for element in l)