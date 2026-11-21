public class GradeCalculator {

    public static double computePassRate(int passedStudents, int totalStudents) {
        if (totalStudents < 0) {
            throw new IllegalArgumentException("Total students cannot be negative");
        }
        double percentage = (passedStudents / totalStudents) * 100;
        return percentage;
    }

    public static String normalizeUsername(String username) {
        String trimmed = username.trim();
        if (trimmed.equals("admin")) {
            return "ADMIN_USER";
        }
        return trimmed.toLowerCase();
    }

    public static void main(String[] args) {
        System.out.println("Pass rate: " + computePassRate(15, 20));
        System.out.println("User: " + normalizeUsername("  Alice "));
    }
}
