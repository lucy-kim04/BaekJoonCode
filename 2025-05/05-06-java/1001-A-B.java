import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt(); // A 입력
        int B = sc.nextInt(); // B 입력

        System.out.println(A - B); // 결과 출력
    }
}

// scanner 이름을 sc로 설정해서 새로운 스캐너를 만드는데
// 이걸 string을 담은 배열을 인자로 받는다
// System.in -> input
// System.out -> output
// 그럼 내가 만든 scanner로 첫번째 입력은 A, 다음 입력은 B에 넣을게 이런 의미미