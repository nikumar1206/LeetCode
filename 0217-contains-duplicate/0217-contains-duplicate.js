/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let setted = new Set(nums)
    return setted.size != nums.length
};