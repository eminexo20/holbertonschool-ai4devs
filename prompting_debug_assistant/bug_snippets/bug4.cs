using System;

namespace BugSnippets
{
    public class UserAccess
    {
        public static string CheckAccess(string role)
        {
            // BUG: Assignment operator '=' used instead of comparison '=='
            if (role = "admin")
            {
                return "Access Granted";
            }
            return "Access Denied";
        }
    }
}
