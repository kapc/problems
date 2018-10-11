#! /usr/env/python

def replace_space(str1):
    if not str1:
        return str1
    str_list = list(str1)
    str_list = ["%20" if c == " " else c for c in str1]
    return "".join(str_list)

if __name__ == "__main__":
    assert "chandresh%20kapadia" == replace_space("chandresh kapadia")
    assert "%20%20%20%20" == replace_space("    ")
    assert  "" == replace_space("")