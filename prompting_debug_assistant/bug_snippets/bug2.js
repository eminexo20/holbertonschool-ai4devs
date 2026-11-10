function calculateAverage(numbers) {
    // Bug: total is undefined (should be initialized to 0)
    let total;
    
    // Bug: i <= numbers.length causes array out-of-bounds
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    
    return total / numbers.length;
}

// Test snippet for line count requirement
const inputData = [10, 20, 30, 40];
const avgResult = calculateAverage(inputData);
