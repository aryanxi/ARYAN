import javax.lang.model.util.ElementScanner14;

// Your First Program

// class HelloWorld {
//     public static void main(String[] args) {
//         System.out.println("Hello, World!"); 
//     }
// }

public class test {
    public static void main(String[] args) {
        System.out.print("the grade is" + getGrade(90.0));
        System.out.print("the grade is" + getGrade(10.0));

    }

public static   getGrade( double score ) {
if (score >= 90.0 )
return 'A';
    else if(score >=70.0)
    return 'B';
    else if(score >=60.0)
    return 'c';
    else 
    return 'F';
    
}
}