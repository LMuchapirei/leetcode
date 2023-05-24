// /**
//  * @param {Array} arr
//  * @return {Matrix}
//  */
// var jsonToMatrix = function(arr) {
//     // Object.keys(arr[i])
//     // find all the keys in the objects
//     // 3 objects, each have say 2 keys,1 key,1 key
//     // matrixResult = [4,4]
//     // first row should have all the keys
//     // for obj in array -> get the keys in obj and then add each key as the first row
//     // filling the items
//     let res = []
//     for(let i=0;i<arr.length;i++){
//         const currObj = arr[i]
//         Object.keys(currObj).forEach(key=>res.push(key))
//     }
//     res = Array.from(new Set(res)).sort()
//     let result = [[...res]]
//         for(let indx=0;indx<arr.length;indx++){
//             const obj = arr[indx];
//             let rowResult=[]
//             for(let key=0;key<res.length;key++){
//                 const currKey = res[key]
//                 if(Object.keys(obj).includes(currKey)){
//                     rowResult.push(obj[currKey])
//                 }else{
//                     rowResult.push("")
//                 }
//             }
//         result.push(rowResult)
//     }
//     return result
// };

// let arr = [
//     {"b": 1, "a": 2},
//     {"b": 3, "a": 4}
//   ]

// let arr = [
//     {"a": 1, "b": 2},
//     {"c": 3, "d": 4},
//     {}
//   ]
// jsonToMatrix(arr)



/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    // Recursion
    const keySet = new Set();
    for(const obj of arr){
        getKeys(obj,"");
    }
    const keys = Array.from(keySet).sort();
    const res  = [keys]; //
    for (const obj of arr){
        const keyToVal = {};
        getValues(obj,"",keyToVal);
        let row = [];
        for (const key of keys){
            if(key in keyToVal){
                row.push(keyToVal[key]);
            }else{
                row.push("");
            }
        }
        res.push(row);
    }
    return res;
    function getKeys(obj,path){
        for (const key in obj){
            const newPath = path? `${path}.${key}`:key;
            if(isObject(obj[key])){
                // recursive
                getKeys(obj[key],newPath);
            }else{
                keySet.add(newPath);
            }
        }
    }

    function isObject(obj){
        return obj !== null && typeof obj === "object";
    }

    function getValues(obj,path,keyToVal){
        for(const key in obj){
            const newPath = path ?`${path}.${key}`:key;
            if(isObject(obj[key])){
                getValues(obj[key],newPath,keyToVal);
            }else{
                keyToVal[newPath]=obj[key];
            }
        }
    }
};
