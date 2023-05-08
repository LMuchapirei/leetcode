/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    for(let idx=0;idx<arr.length;idx++)
        arr[idx]=fn(arr[idx],idx)
    return arr
};