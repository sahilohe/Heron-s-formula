package com.fsociety97;
import java.util.Scanner;
import java.lang.Math;

public class Heron_Formula {

    public static void main(String[] args) {
        //Creating a instance of Scanner
        Scanner input = new Scanner(System.in);

        //Asking the user for three sides
        System.out.println("Enter the sides:");
        double firstSide = input.nextDouble();
        double secondSide = input.nextDouble();
        double thirdSide = input.nextDouble();

        //finding the semi-perimeter and area
        double semiPerimeter = (firstSide + secondSide + thirdSide) / 2;
        double answer = Math.sqrt(semiPerimeter * (semiPerimeter - firstSide) * (semiPerimeter - secondSide) * (semiPerimeter - thirdSide));
        
        //printing out the answer
        System.out.println("The answer is " + answer);

    }

}
