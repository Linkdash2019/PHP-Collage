package com.mycompany.mavenproject1;
import com.mycompany.mavenproject1.month;


public class Mavenproject1
{
    public static void main()
    {
        month month1 = new month();
        month month2 = new month(5);
        month month3 = new month("December");
        
        System.out.println("-------- Test 1 ---------");
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(2);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(3);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(4);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(5);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(6);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(7);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(8);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(9);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(10);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(11);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        month1.setMonthNumber(12);
        System.out.println(month1.getMonthNumber());
        System.out.println(month1.getMonthName());
        
        System.out.println("\n-------- Test 2 ---------");
        System.out.println(month2.getMonthNumber());
        System.out.println(month2.getMonthName());
        System.out.println(month2.equals(3));
        System.out.println(month2.greaterThan(8));
        System.out.println(month2.greaterThan(4));
        System.out.println(month2.lessThan(8));
        System.out.println(month2.lessThan(4));  
        
        System.out.println("\n-------- Test 3 ---------");
        System.out.println(month3.getMonthNumber());
        System.out.println(month3.getMonthName());
        
    }
}