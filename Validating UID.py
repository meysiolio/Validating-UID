import re

for _ in range(int(input())):
    UID = input()
    try:
        assert re.fullmatch(r'[A-Za-z0-9]{10}',UID)
        assert re.fullmatch(r'([a-z0-9]*[A-Z]+[a-z0-9]*){2,}',UID)
        assert re.fullmatch(r'([a-zA-Z]*[0-9]+[a-zA-Z]*){3,}',UID)
        assert not(re.search(r'(.).*?\1',UID))
            
    except AssertionError:
        print('Invalid')
    else:
        print('Valid')