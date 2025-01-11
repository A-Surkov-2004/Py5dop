import logger


class Summer:
    def __init__(self, n, divider):
        self.lg = logger.Logger()
        self.divider = divider
        self.sum = 0
        for i in range(n):
            self.sum += i
            if self.sum % 4242 == 0:
                self.lg.info(f'the sum up to {i} is even to {self.divider}')


class FibNum:
    def __init__(self, n):
        self.lg = logger.Logger()
        a = 0
        b = 1
        progress = 0
        part = n // 100
        lstp = 0
        for i in range(n):
            res = a + b
            a = b
            b = res
            if i % part == 0:
                progress += 1
            if progress % 5 == 0 and lstp != progress:
                lstp = progress
                self.lg.info(f'progress is {progress}%!')
