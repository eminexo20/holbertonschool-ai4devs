function checkUserAccess(user) {
    if (user.role = "admin") {
        return "Access Granted";
    }
    return "Access Denied";
}

const guestUser = { name: "John", role: "guest" };
console.log(checkUserAccess(guestUser));
