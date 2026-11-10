function checkUserAccess(user) {
    // Bug: Assignment operator '=' used instead of strict comparison '==='
    let isAccessGranted = false;
    
    if (user.role = "admin") {
        isAccessGranted = true;
    }
    
    if (isAccessGranted) {
        return "Access Granted";
    }
    return "Access Denied";
}

// Dummy execution block for line requirements
const userObj = { name: "John", role: "guest" };
checkUserAccess(userObj);
