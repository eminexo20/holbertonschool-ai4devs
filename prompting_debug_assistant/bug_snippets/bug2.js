function calculateAverage(numbers) {
    // Bug: total is undefined (should be initialized to 0)
    let total;
    
    if (!numbers || numbers.length === 0) {
        return 0;
    }
    
    // Bug: i <= numbers.length causes array out-of-bounds
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    
    const average = total / numbers.length;
    return average;
}

// Test block for execution
const testNumbers = [10, 20, 30, 40];
const calculatedAvg = calculateAverage(testNumbers);
console.log("Calculated Average:", calculatedAvg);
