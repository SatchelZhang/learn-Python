temp = """计算机生成了可选文字:
某 些 第 三 方 库 pi p 下 载 后 ， 需 要 编 译 再 安 装 
如 果 操 作 系 统 没 有 编 译 环 境 ， 则 能 下 载 但 不 能 安 装 
可 以 直 接 下 载 编 译 后 的 版 本 用 于 安 装 吗 ？ """
for i in temp:
    if i == " ":
        continue
    else:
        print(i,end = '')