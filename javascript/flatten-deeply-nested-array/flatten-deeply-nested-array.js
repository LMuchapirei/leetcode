// /**
//  * @param {any[]} arr
//  * @param {number} depth
//  * @return {any[]}
//  */
// var flat = function (arr, n) {
//     // maintan a res array

//     // given the depth n
//     // go over the array taking each element at given position and then inserting spreading the results over it at the appropriate index

//     const res = [];
//     for(let idx=0;idx < n;idx++){
//         for(let jdx=0;jdx<arr.length;jdx++){
//             if(Array.isArray(arr[jdx])){
//                 const currArray = arr[jdx]
//                 res.push(flat(currArray,n))
//             }else{
//                 res.push(arr[jdx])
//             }
//         }    
//     }
//     return res 
// };

// let arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]//[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

// console.log(flat(arr,2))


/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    const res = [];
    function helper(arr,depth){
        for(const val of arr){
            if(typeof val ==="object" && depth < n ){
                helper(val,depth + 1)
            }else{
                res.push(val);
            }
        }
        return res;
    }
    return helper(arr,0);
};

let arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]//[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

console.log(flat(arr,2))