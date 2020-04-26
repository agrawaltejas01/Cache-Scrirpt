# Cache-Scrirpt
## Description : 
A low level caching script in python 2.7
## Functionality : 
1. **add(key, value, TTL = -1)** : <br>
 Returns True if added successfully, otherwise False <br>
 TTL = Time to Live<br>
 TTL is in seconds and optional parameter.<br>
 data will persist till end if TTL is not provided or provided negative<br>
 TTL = 0 not stored<br>

2. **get(key, default = "Not_Available")** :<br>
 If key is not present in cache, will return default value<br>
 Otherwise will return value of given key

3. **delete(key)** :<br>
 Returns True if deleted successfully, otherwise False <br>

4. **clear()** :<br>
 Clears whole of cache.<br>
 Returns void
 
## Usage :
1. Copy script in source folder
2. Import Cache class as : from cache import Cache



