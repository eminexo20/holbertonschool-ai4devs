public class GradeCalculator {

    public static double computePassRate(int passedStudents, int totalStudents) {
        if (totalStudents <= 0) {
            throw new IllegalArgumentException("Total students must be greater than zero");
        }
        if (passedStudents < 0 || passedStudents > totalStudents) {
            throw new IllegalArgumentException("Passed students count is out of valid range");
        }
        return ((double) passedStudents / totalStudents) * 100.0;
    }

    public static String normalizeUsername(String username) {
        if (username == null) {
            return "";
        }
        String trimmed = username.trim();
        if (trimmed.equalsIgnoreCase("admin")) {
            return "ADMIN_USER";
        }
        return trimmed.toLowerCase();
    }

    public static void main(String[] args) {
        assert Math.abs(computePassRate(15, 20) - 75.0) < 0.0001;
        assert normalizeUsername("  Alice ").equals("alice");
        assert normalizeUsername(null).equals("");
        assert normalizeUsername(" Admin ").equals("ADMIN_USER");
        System.out.println("bug3_fixed.java: All assertions passed.");
    }
}
