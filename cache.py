import sys
import time
from datetime import datetime
from threading import Timer

cache = {}
availableMemory = 6.4e+7
# availableMemory = 24 * 3

def insertInCache(key, value, requiredSize, TTL):    

    global cache    

    keyInfo = {}

    keyInfo['valid'] = True
    keyInfo['value'] = value
    keyInfo['requiredSize'] = requiredSize    
    keyInfo['timeStamp'] = datetime.now() 
    keyInfo['TTL'] = TTL  

    cache[key] = keyInfo

    if TTL >= 0:
        c = Cache()
        t = Timer(TTL, c.delete, args=[key])
        t.start()



    

class Cache:
    
    def add(self, key, value, TTL = -1):
        requiredSize = sys.getsizeof(value)
        # print(requiredSize)

        global availableMemory        
        global cache

        # Check if memory is available
        if availableMemory < requiredSize:
            # LRU
            sortedCache = sorted(cache.items(), 
                          key=lambda keyInfo: keyInfo[1]['timeStamp'])
            print(sortedCache)

            # free up memory till required size is met
            for i in sortedCache:

                if availableMemory >= requiredSize:
                    break
                
                del cache[i[0]]
                availableMemory = availableMemory + i[1]['requiredSize']

                insertInCache(key, value, requiredSize, TTL)             
                      

            return True

        # Reduce available memory
        availableMemory = availableMemory - requiredSize

        # Store
        insertInCache(key, value, requiredSize, TTL)        

        return True
    
    def get(self, key, default = "Not_Available"):

        global cache

        # print(default)
        value = cache.get(key, default)

        # Check if key exists
        if value == default:
            return default
        
        elif not value['valid']:            
            return default
        
        else:
            return value['value']
    
    def delete(self, key, default = "Not_Available"):

        global cache

        # Check if key exists
        if self.get(key) != "Not_Available":
            del cache[key]
            return True
        
        else:
            return False
    
    def clear(self):
        cache.clear()
        return

    
c = Cache()
print(c.add("a", 8, 8))
print(c.add("b", 2, 2))
print(c.add("c", 7, 7))

print(c.get("b"))
print(c.get("c"))

print(c.add("d", "Hello", 1))
print(c.add("e", "World", 2))

# print(c.delete("a"))
# print(c.delete("a"))

time.sleep(5)
print(c.get("b"))
print(c.get("a"))


# c.clear()
print(cache)