// Bug Snippet 2 - JavaScript Array Loop & Average
// Intended behavior: Calculate average of an array of numbers.

function calculateAverage(numbers) {
    // BUG 1: Uninitialized variable (starts as undefined)
    let total;
    
    // BUG 2: Loop condition 'i <= numbers.length' accesses out-of-bounds index
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    
    return total / numbers.length;
}

// Example Usage:
const data = [10, 20, 30, 40];
console.log(calculateAverage(data));
