function calculateAverage(numbers) {
    let total;
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    return total / numbers.length;
}
