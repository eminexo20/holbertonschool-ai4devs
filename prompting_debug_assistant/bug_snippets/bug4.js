function checkUserAccess(user) {
    // Bug: Assignment operator '=' used instead of strict comparison '==='
    let isAccessGranted = false;
    
    if (!user) {
        return "No user provided";
    }
    
    if (user.role = "admin") {
        isAccessGranted = true;
    }
    
    if (isAccessGranted) {
        return "Access Granted";
    }
    return "Access Denied";
}

// Execution block for test
const sampleUser = { name: "John", role: "guest" };
const accessStatus = checkUserAccess(sampleUser);
console.log("Status:", accessStatus);
