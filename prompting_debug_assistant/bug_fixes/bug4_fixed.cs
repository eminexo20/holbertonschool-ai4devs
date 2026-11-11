using System;

namespace BugSnippets
{
    public class UserAccess
    {
        public static string CheckAccess(string role)
        {
            if (role == "admin")
            {
                return "Access Granted";
            }
            return "Access Denied";
        }
    }
}
