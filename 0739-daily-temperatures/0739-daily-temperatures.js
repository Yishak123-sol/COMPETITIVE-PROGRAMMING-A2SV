/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    var lengthh = temperatures.length;
    var answer = [];
    for(j=0; j < lengthh; j++){
        answer.push(0);
    }
    
    var monStack = [];
    
    for(i=0; i < lengthh; i++){
        while(monStack && temperatures[monStack[monStack.length-1] ]< temperatures[i]){
            let prev = monStack.pop();
            answer[prev] = (i - prev);
        }
        monStack.push(i);
    }
    return answer
};