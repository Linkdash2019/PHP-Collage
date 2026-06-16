package com.mycompany.mavenproject1;

public class month
{
    int monthNumber;
    
    public month() 
    {
        monthNumber = 1;
    }
    
    public month(int num) 
    {
        monthNumber = num;
    }
    
    public month(String str) 
    {
        if("January".equals(str)){ monthNumber = 1; }
        else if("Febuary".equals(str)){ monthNumber = 2; }
        else if("March".equals(str)){ monthNumber = 3; }
        else if("April".equals(str)){ monthNumber = 4; }
        else if("May".equals(str)){ monthNumber = 5; }
        else if("June".equals(str)){ monthNumber = 6; }
        else if("July".equals(str)){ monthNumber = 7; }
        else if("Augest".equals(str)){ monthNumber = 8; }
        else if("Setember".equals(str)){ monthNumber = 9; }
        else if("October".equals(str)){ monthNumber = 10; }
        else if("November".equals(str)){ monthNumber = 11; }
        else if("December".equals(str)){ monthNumber = 12; }
        else { monthNumber = 1; }
    }
    
    public void setMonthNumber(int num)
    {
        monthNumber = num;
    }
    
    public int getMonthNumber()
    {
        return monthNumber;
    }
    
    public String getMonthName()
    {
        if(monthNumber == 1) {return("January");}
        else if(monthNumber == 2) {return("Febuary");}
        else if(monthNumber == 3) {return("March");}
        else if(monthNumber == 4) {return("April");}
        else if(monthNumber == 5) {return("May");}
        else if(monthNumber == 6) {return("June");}
        else if(monthNumber == 7) {return("July");}
        else if(monthNumber == 8) {return("Augest");}
        else if(monthNumber == 9) {return("Setember");}
        else if(monthNumber == 10) {return("October");}
        else if(monthNumber == 11) {return("November");}
        else if(monthNumber == 12) {return("December");}
        else{return("Error invalid month '"+monthNumber+"'");}
    }
    
    public String toString()
    {
        return getMonthName();
    }
    
    public boolean equals(int num)
    {
        return num == monthNumber;
    }
    
    public boolean greaterThan(int num)
    {
        return num > monthNumber;    
    }
    
    public boolean lessThan(int num)
    {
        return num < monthNumber;
 }
}