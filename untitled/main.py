
if __name__ == '__main__':
    print(12)

    def test():
        print('xxxxxx')
    test()


    class Complex:
        def __init__(self,realpart,imagpart):
            self.r = realpart
            self.i = imagpart
    x=Complex(3.0,-4.5)
    print(x.r,x.i)

    f = open('D:\ITA\phython\ClassTest\Test.txt', 'w')  # r只读，w可写，a追加
    for i in range(0, 10): f.write(str(i) + '\n')
    f.close()

    f = open('D:\ITA\phython\ClassTest\Test.txt', 'r')  # r只读，w可写，a追加
    t = f.readlines()
    print(t)
    f.close()




