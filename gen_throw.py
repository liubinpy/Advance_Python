def gen_func():
    html = yield "http://www.baidu.com/"
    print(html)
    print("1")
    yield 1
    print("2")
    yield 2

if __name__ == "__main__":
    gen = gen_func()
    print(gen.send(None))
    print(gen.send("<html></html>"))
    gen.throw(Exception, "error")

