import re

def clean_text(text):
    reg_exp_handle = re.compile('W+')
    result = reg_exp_handle.sub(' ', text).strip()
    return result