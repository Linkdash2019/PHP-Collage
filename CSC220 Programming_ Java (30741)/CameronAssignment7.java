package com.cameron.cameronassignment7;
import com.cameron.cameronassignment7.Car;

public class CameronAssignment7 {

    public static void main(String[] args) {
    Car obj = new Car(2006, "Mitsubishi Lancer");
    System.out.println(obj.getYearModel()+" "+obj.getMake());
    System.out.println(obj.getSpeed());
    obj.accelerate();
    System.out.println(obj.getSpeed());
    obj.accelerate();
    System.out.println(obj.getSpeed());
    obj.accelerate();
    System.out.println(obj.getSpeed());
    obj.accelerate();
    System.out.println(obj.getSpeed());
    obj.accelerate();
    System.out.println(obj.getSpeed());
    obj.brake();
    System.out.println(obj.getSpeed());
    obj.brake();
    System.out.println(obj.getSpeed());
    obj.brake();
    System.out.println(obj.getSpeed());
    obj.brake();
    System.out.println(obj.getSpeed());
    obj.brake();
    System.out.println(obj.getSpeed());
    obj.brake();
    System.out.println(obj.getSpeed());
    }
}
