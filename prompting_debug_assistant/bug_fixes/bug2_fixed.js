function calculateAverage(numbers) {
    if (!numbers || numbers.length === 0) {
        return 0;
    }

    let total = 0;
    
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    
    return total / numbers.length;
}

// Example Usage:
const data = [10, 20, 30, 40];
console.log(calculateAverage(data));
