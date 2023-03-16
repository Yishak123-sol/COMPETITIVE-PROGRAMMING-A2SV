/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function(nums, threshold) {
    var right = Math.max(...nums);
    var minval = right + 1;
    var left = 1;
    
    while (left <= right){
        var mid = left + Math.floor((right - left)/2);
        var total = 0;
        for (let i = 0; i < nums.length; i++){
            var num = nums[i]/mid
            total += Math.ceil(num)
            if(total > threshold){
                break;
            }
        }
        if (total > threshold){
            left = mid + 1
        }else{
            minval = Math.min(minval, mid);
            console.log(total)
            right = mid - 1;
        }
    }
    return minval
};