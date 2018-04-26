final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name+"销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key+"销量统计完成！！.")

def main():
    data_sets = {
        "oo牌面膜": [1200, 1500, 3000],
        "oo牌手机": [28,55,98,108 ],
        "oo牌大衣": [280,560,778,70],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None) # 预激middle协程
        for value in data_set:
            m.send(value)   # 给协程传递每一组的值,这里send给了sales_sum
        m.send(None)
    print("final_result:", final_result)

if __name__ == '__main__':
    main()

"""
main:调用方
middle:委托生成器
sales_sum:子生成器
"""