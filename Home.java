import java.util.Scanner;

public class Home {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        while(true){
            System.out.println("Enter the option below");
            System.out.println("1 .Insert the values");
            System.out.println("2 .View all values");
            System.out.println("3 .Search the values using date");
            System.out.println("4 .Exit");

            choice = sc.nextInt();

            switch (choice){
                case 1:
                    System.out.println("Enter the values");
                    break;
                case 2:
                    System.out.println("View all the values in the database");
                    break;
                case 3:
                    System.out.println("Search the details of the particular date ");
                    break;
                case 4:
                    System.exit(0);
            }
        }
    }
}
