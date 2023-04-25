/**
 * @param {number} millis
 */
async function sleep(millis) {
    return await new Promise(function(resolve,reject){
        setTimeout(function(){
            resolve(100)
         },millis)
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */