/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (o1==null || o2==null){
        return o1===o2;
    }
    if(typeof o1 !== typeof o2){
        return false;
    }
    // Check for primitives
    if(typeof o1 !=='object'){
        return o1===o2;
    }
    // Array equality check
    if(Array.isArray(o1) || Array.isArray(o2)){
        // deal with [undefined] and {'a':1}
        // [undefined][0]==={'a':1}[0]
        if(String(o1)!==String(o2)){
            return false;
        }
        for(let i=0;i<o1.length;i++){
            if(!areDeeplyEqual(o1[i],o2[i])){
                return false;
            }
        }
    }else {
        // Object equality
        // Check key length
        if(Object.keys(o1).length !== Object.keys(o2).length){
            return false;
        }
        for(const key in o1){
            // do a deep equal check for each and every object seen thus far
            if(!areDeeplyEqual(o1[key],o2[key])){
                return false;
            }
        }
    }
    return true;
};