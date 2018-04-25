def gen_func():
    # 当yield在表达式右边的时候，有两个作用，1.返回值，2，接收值
    html = yield "http://www.baidu.com/"
    print(html)
    yield 1
    yield 2

if __name__ == "__main__":
    gen = gen_func()
    # print(next(gen))  # 这里可以使用gen.send(None)代替
    print(gen.send(None))
    print(gen.send("<html></html>"))
    print(next(gen))

