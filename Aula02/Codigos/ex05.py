#!/usr/bin/python
import random

print 'random(): ', random.random()
print 'uniform(3.56,72.1): ', random.uniform(3.56,7.1)
print 'randrange(10): ', random.randrange(10)
print '1->randrange(13,79,10): ', random.randrange(13,79,10)
print '2->randrange(13,79,10): ', random.randrange(13,79,10)

seq = [1,2,3,4,5,6,7,8,9,10]
print 'seq:', seq
print 'choice(seq): ', random.choice(seq)
print 'shuffle(seq): ', random.shuffle(seq)
print 'seq:', seq
