import logger
import main

def test1():
    # given
    n = 10000
    devider = 4242

    # when
    s1 = main.Summer(n, devider)

    # then
    file1 = open("logger.log", "r+")
    assert file1.read().splitlines()[17].split()[8] == str(8988)



def test2():
    # given
    n = 10000
    devider = 4242

    n2 = 50000
    devider2 = 4433

    n3 = 10000

    # when
    s1 = main.Summer(n, devider)
    s2 = main.Summer(n2, devider2)
    f1 = main.FibNum(n3)

    # then
    assert logger.Logger.instances == 1

test1()
test2()
