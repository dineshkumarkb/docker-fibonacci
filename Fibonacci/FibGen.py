import logging

log = logging.getLogger("FibGen")
logging.basicConfig(level=logging.ERROR)

class FiboGen(object):

    def __init__(self,myrange):
        log.info(" Initialized ")
        self.index_value = myrange
        self.a = 0
        self.b = 1
        if isinstance(self.index_value,int):
            log.info(" Value passed is an int ")
            self.generate_series()
        else:
            raise(TypeError, "The value should be an integer")

    def generate_series(self):
        log.info(" Generating series ")
        for i in range(self.index_value):
            self.c = self.a + self.b
            self.a,self.b = self.b,self.c
        print(self.c)

if __name__ == "__main__":
    fib = FiboGen(7)
