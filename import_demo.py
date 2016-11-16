# use separate namespace for "math" module
print('List of objects names in __main__ namespace:')
print (dir())
import math
print('List of object names in __main__ namespace', end=' ')
print('after "import math" has executed:')
print(dir())
print('The value of pi is', math.pi)
print('The value of 1 is', math.tan(1))
del (math)

# use separate aliased namespace for "math" module
print('List of objects names in __main__ namespace:')
print (dir())
import math as fun
print('List of object names in __main__ namespace', end=' ')
print('after "import math as fun" has executed:')
print(dir())
print('The value of pi is', fun.pi)
print('The value of 1 is', fun.tan(1))
del (fun)


# use selectively the data attributes for "math" module
print('List of objects names in __main__ namespace:')
print (dir())
from math import pi, tan
print('List of object names in __main__ namespace', end=' ')
print('"from math import pi as Pie, tan as tangent" has executed:')
print(dir())
print('The value of pi is', pi)
print('The value of 1 is', tan(1))
del(pi)
del(tan)


# use selectively the data attributes for "math" module
print('List of objects names in __main__ namespace:')
print (dir())
from math import pi as pie, tan as tangent
print('List of object names in __main__ namespace', end=' ')
print('"from math import pi as Pie, tan as tangent" has executed:')
print(dir())
print('The value of pi is', pie)
print('The value of 1 is', tangent(1))
del(pie)
del(tangent)

#wildcard usage of module namespace

from math import *
print('you want to avoid using this:')
print (dir())
