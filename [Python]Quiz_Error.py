def foo(s):
    # 이곳에 들어갈 코드는?
    try:
        s += '1'
    except UnboundLocalError:
        print('wow')
    except:
        print('owo')


foo('abc')

# 출력:
# wow
