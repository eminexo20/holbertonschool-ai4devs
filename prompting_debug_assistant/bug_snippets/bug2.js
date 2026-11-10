// Bug Snippet 2 - JavaScript Array Loop & Average
// Intended behavior: Calculate average of an array of numbers.
// -------------------------------------------------------------

function calculateAverage(numbers) {
    // Uninitialized variable bug (starts as undefined)
    let total;
    
    // Loop boundary bug (i <= numbers.length goes out of bounds)
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    
    return total / numbers.length;
}

// Example Usage:
// const data = [10, 20, 30, 40];
// console.log(calculateAverage(data));
