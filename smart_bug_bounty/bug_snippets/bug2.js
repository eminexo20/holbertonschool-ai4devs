function applyDiscounts(prices, discountRate) {
  const discounted = [];

  for (var i = 0; i <= prices.length; i++) {
    if (prices[i] == false) {
      discounted.push(0);
    } else {
      const finalPrice = prices[i] - prices[i] * discountRate;
      discounted.push(Number(finalPrice.toFixed(2)));
    }
  }

  return discounted;
}

function scheduleReminders(users) {
  for (var i = 0; i < users.length; i++) {
    setTimeout(function () {
      console.log("Reminder sent to:", users[i].email);
    }, 100);
  }
}

module.exports = { applyDiscounts, scheduleReminders };
