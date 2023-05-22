/**
 * @param {any} object
 * @return {string}
 */

// My own solution for this question
var jsonStringify = function (object) {
    let strRepr = "{";
    if (object == null || object === undefined || typeof object === "boolean"  || typeof object === "number" || typeof object === "string") {
        return  typeof object === "string" ? `"${object}"`: object
    }
    const objectKeys = Object.keys(object);
    if (objectKeys.length === 0 ) {
        if(Array.isArray(object)){
            return "[]"
        }
        return "{}";
    }
    if(Array.isArray(object)){
          const arrayRepr = arrayStrRepr(object)
          return arrayRepr
    }
    for (let idx = 0; idx < objectKeys.length; idx++) {
        const value = object[objectKeys[idx]]
        const typeofValue = typeof value
        if (typeofValue === "object" && !Array.isArray(value)) {
            strRepr += (`"${objectKeys[idx]}":${jsonStringify(value)}`)
        }
        if (typeofValue === "string" || typeofValue === "number"
            || typeofValue === "boolean" || typeofValue === "undefined") {
            strRepr += (`"${objectKeys[idx]}":${typeofValue === "string" ? `"${value}"` : value}`)
        }
        if(Array.isArray(value)){
          const arrayRepr = arrayStrRepr(value)
          strRepr += (`"${objectKeys[idx]}":${arrayRepr}`)
        }
        if (idx + 1 !== objectKeys.length) {
            strRepr += ","
        }
    }
    strRepr += "}"
    return strRepr
};

const arrayStrRepr = (array) => {
            let arrayRepr = "["
            for (let jdx = 0; jdx < array.length; jdx++) {
                let arrayValue = array[jdx];
                let typeOfArrayValue = typeof arrayValue
                if (typeOfArrayValue === "object" && ! Array.isArray(arrayValue)){
                    arrayRepr += `${jsonStringify(arrayValue)}`
                }
                if(typeOfArrayValue === "object" && Array.isArray(arrayValue)){
                    arrayRepr += arrayStrRepr(arrayValue)
                }
                if (typeOfArrayValue === "string" || typeOfArrayValue === "number"
                    || typeOfArrayValue === "boolean" || typeOfArrayValue === "undefined") {
                    arrayRepr += (`${typeOfArrayValue === "string" ? `"${arrayValue}"` : arrayValue}`)
                }
                if (jdx + 1 < array.length) {
                        arrayRepr += ","
                }
            }
            arrayRepr += "]"
            return arrayRepr
}