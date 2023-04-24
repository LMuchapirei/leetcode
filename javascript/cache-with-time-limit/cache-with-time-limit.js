var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // check if the value is already in the cache
    let found = this.cache.has(key)
    // clear the value by accessing the ref of its timeout
    if(found) clearTimeout(this.cache.get(key).ref)
    // set a new vakue in the cache specifying the key , value and reference to its timeout
    this.cache.set(key,{
        value,
        ref:setTimeout(()=>this.cache.delete(key),duration)
    });
    // return flag indicating whether this is a new value or it was the same previously set value
    return found;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.cache.has(key) ? this.cache.get(key).value:-1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */

/*
The global clearTimeout() method cancels a timeout previously established by calling setTimeout().
clearTimeout(timeoutID)

timeOutID
-is the identifier of the timeout you want to cancel
-this ID is returned by a correponding call to setTimeout()

*/