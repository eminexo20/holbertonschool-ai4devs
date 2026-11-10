// Bug Snippet 4 - JavaScript Equality Operator Misuse
// Intended behavior: Check user role permissions.

function checkUserAccess(user) {
    // BUG: Single equals '=' assignment used instead of strict comparison '==='
    if (user.role = "admin") {
        return "Access Granted";
    }
    
    return "Access Denied";
}

// Example Usage:
const guestUser = { name: "John", role: "guest" };
console.log(checkUserAccess(guestUser));
