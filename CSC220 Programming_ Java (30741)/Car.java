package com.cameron.cameronassignment7;

public class Car {
    
    int yearModel;
    String make;
    int speed;
    
    public Car() {
        yearModel = 1900;
        make = "None";
        speed = 0;
    }
    
    public Car(int year, String maker) {
        yearModel = year;
        make = maker;
        speed = 0;
    }
    
    public Car(int year) {
        yearModel = year;
        make = "None";
        speed = 0;
    }
    
    public Car(String maker) {
        yearModel = 1900;
        make = maker;
        speed = 0;
    }
    
    public int getYearModel(){
       return yearModel; 
    }
    
    public String getMake(){
       return make; 
    }
    
    public int getSpeed(){
       return speed; 
    }
    
    public void accelerate(){
        speed = speed + 5;
    }
    
    public void brake(){
        speed = speed - 5;
        if(speed < 0){speed = 0;}
    }
}
