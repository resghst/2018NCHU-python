class a:
    'this is doc'
    att1 = 0
    att4 = 0
    att5 = 0
    def __init__(self, att4, att5):    
        att1=1    
        print str(att4) + " str " + str(att5)
    def printatt(self, att1):
        print self.att1

    # python can't used multiple constructor, it will be rewrite by last method
    def hello(self, c=0):                    
        print "hello =" + str(c)
    # def hello(self, b):
    #     print "hello" + str(b)
    def __del__(self):
        print "A del"

class b(a):
    def __init__(self, att4, att5):
        super()

if __name__ == "__main__":
    classtest =  a(2,3)
    classtest1 =  a(2,"aa")
    classtest1.hello(1)
    classtest1.hello(' ,world')
    print "classtest.__module__: " + str(dir(classtest))  #vue the method and attribute in dir()
    print "classtest.__init__  : " + str(classtest.__init__)
    print "classtest.__doc__   : " + str(classtest.__doc__)
    # print "classtest.__name__  : " + str(classtest.__name__)
    print "classtest.__module__: " + str(classtest.__module__)
    # print "classtest.__base__  : " + str(classtest.__base__)


    classtest =  b(2,3)
    classtest1 =  b(2,"aa")
    print "classtest.__module__: " + str(dir(classtest))  #vue the method and attribute in dir()
    print "classtest.__init__  : " + str(classtest.__init__)
    print "classtest.__doc__   : " + str(classtest.__doc__)
    # print "classtest.__name__  : " + str(classtest.__name__)
    print "classtest.__module__: " + str(classtest.__module__)
    # print "classtest.__base__  : " + str(classtest.__base__)
