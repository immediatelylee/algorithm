# import re
# def trans_id():

# new_id = dltnrlf321
# if len(new_id) < 3 or len(new_id) >15: #아이디 길이 제한
#     trans_id(new_id)
# elif #특수문자 제한 -> 정규 표현식


# import re

# def trans_id(nid):
#     nid.lower()
#     p = re.compile('[^a-z0-9_.-]')
#     a= re.sub('..','.') # .. -> .
#     re.sub('','a')

# new_id = "dltnrlf321##"
# p = re.compile('[^a-z0-9_.-]')
# m = p.search(new_id)
# if m != None:
#     trans_id(new_id)


##
import re


def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + \
        "".join([st[-1] for i in range(3-len(st))])
    return st
