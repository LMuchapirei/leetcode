/**
 *  @param {any} object 
 *  @return {string}
 */

// Happens to be the better code 
var jsonStringify = function(object){
    if(object == null || object === undefined ){
        return String(object);
    }
    // Arrays  []
    if(Array.isArray(object)){
        const values = object.map((obj)=>jsonStringify(obj))
        return `[${values.join(",")}]`
    }
    // Objects {}
    if(typeof object === "object"){
        const keys = Object.keys(object);
        const keyValPairs = keys.map((key)=>`"${key}":${jsonStringify(object[key])}`)
        return `{${keyValPairs.join(",")}}`;
    }
    // Strings ""
    if(typeof object === "string"){
        return `"${String(object)}"`
    }
    return String(object); // booleans or numbers
}