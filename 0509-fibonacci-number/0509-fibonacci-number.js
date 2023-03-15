/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    var stack = [0,1]
    if (n == 0 || n == 1){
        return stack[n]
    }else{
        for (let i = 2; i < n+1; i++){
            curr = stack[i-1] + stack[i-2]
            stack.push(curr)
        }
    }return stack[n]
};