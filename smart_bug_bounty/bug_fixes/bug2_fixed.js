function applyDiscounts(prices, discountRate) {
  const discounted = [];

  for (let i = 0; i < prices.length; i++) {
    const price = prices[i];
    if (typeof price !== "number" || price <= 0) {
      discounted.push(0);
    } else {
      const finalPrice = price - price * discountRate;
      discounted.push(Number(finalPrice.toFixed(2)));
    }
  }

  return discounted;
}

function scheduleReminders(users) {
  for (let i = 0; i < users.length; i++) {
    const user = users[i];
    setTimeout(function () {
      console.log("Reminder sent to:", user.email);
    }, 100);
  }
}

if (require.main === module) {
  const res = applyDiscounts([100, 0, 50], 0.2);
  console.assert(JSON.stringify(res) === JSON.stringify([80, 0, 40]), "Discount test failed");
  scheduleReminders([{ email: "a@test.com" }, { email: "b@test.com" }]);
  console.log("bug2_fixed.js: All assertions passed.");
}

module.exports = { applyDiscounts, scheduleReminders };
