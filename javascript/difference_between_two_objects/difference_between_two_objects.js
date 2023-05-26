// /**
//  * @param {object} obj1
//  * @param {object} obj2
//  * @return {object}
//  */
// function objDiff(obj1, obj2) {
//     const combinedKeys = [...new Set([...Object.keys(obj1),...Object.keys(obj2)])]
//     const res = {};
//     for(const key of combinedKeys){
//         if(obj1[key] && obj2[key]){
//             // check if its primitives
//             if(typeof obj1[key] != object || typeof obj2[key] != object){
//                 res[key]=[obj1[key],obj2[key]]
//              }
//             // check one of the type is an array
//              else if((typeof obj1[key] == object && typeof obj2[key] == object) && (Array.isArray(obj1) && Array.isArray(obj2)) ){
                 
//              }

//             // check if one of the types is object

            
//         }
//     }
//     console.log({res})
// };


// let obj1 = {
//     "a": 1,
//     "v": 3,
//     "x": [],
//     "z": {
//       "a": null
//     }
//   }
// let obj2 = {
//     "a": 2,
//     "v": 4,
//     "x": [],
//     "z": {
//       "a": 2
//     }
//   }

// objDiff(obj1,obj2)


/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */
function objDiff(o1, o2) {
    // Only care about common keys


    // if both primitive and diff, then diff

    // If one is obj and other isn't, then diff

    // If one is array and one is obj, then diff

    // If both arr or both obj, then recursion


        if(!isObject(o1) && !isObject(o2)){
            return o1 === o2 ? {}:[o1,o2]
        }
        if(!isObject(o1) || !isObject(o2)){
            return [o1,o2]
        }
        if(Array.isArray(o1) !== Array.isArray(o2)){
            return [o1,o2]
        }
        const diff = {};
        for (const key in o1){
            if(o2.hasOwnProperty(key)){
                const res = objDiff(o1[key],o2[key])
                if(Object.keys(res).length > 0){
                    diff[key]=res;
                }
            }
        }


    function isObject(obj){
        return typeof obj === "object" && obj !==null;
    }
};