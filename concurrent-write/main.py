import sys
import time

if __name__ == '__main__':

    for arg in sys.argv:
        print arg

    f = open('test.log', 'w')

    for i in range(3):
        time.sleep(1)
        f.write('This is a test ' + str(sys.argv[1]) + '\n')
        print 'This is a test ' + str(sys.argv[1]) + '\n'


    f.close()

