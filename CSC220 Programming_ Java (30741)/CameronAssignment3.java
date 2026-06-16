// Cameron McClellan
// 10/23/25
// Ask user what was bought run some calculations and return price and discount amount
// 30 Minutes

import javax.swing.JOptionPane;

public class CameronAssignment3
{
    public static void main(String[] args)
    {
        //User Variables
        int boughtLicences;
        
        //Caculated Variables
        float licencePrice = 99;
        float discountAmount;
        String discountPercent;
        float totalPrice;
        float priceNoDiscount;
        
        

        
        //User input
        boughtLicences = Integer.parseInt(JOptionPane.showInputDialog(null, "How many software licensess do you want to buy?"));
       
        //Calculations
        if (boughtLicences >= 100)     
        { 
            discountPercent = "50%"; 
            discountAmount = licencePrice*boughtLicences*0.50f;
        }
        else if (boughtLicences >= 50) 
        { 
            discountPercent = "40%";
            discountAmount = licencePrice*boughtLicences*0.40f;
        }
        else if (boughtLicences >= 20) 
        { 
            discountPercent = "30%";
            discountAmount = licencePrice*boughtLicences*0.30f;
        }
        else if (boughtLicences >= 10) 
        { 
            discountPercent = "20%";
            discountAmount = licencePrice*boughtLicences*0.20f;
        }
        else                           
        { 
            discountPercent = "0%"; 
            discountAmount = 0.00f;
        }
        
        priceNoDiscount = boughtLicences*99;
        totalPrice = priceNoDiscount-discountAmount;
        
        //Output
        JOptionPane.showMessageDialog(null,
                "Software Licence(s) x"+boughtLicences+" ... $"+priceNoDiscount+
                "\nRecived Discount ...................... "+discountPercent+
                "\nAmount Saved ........................ -$"+discountAmount+
                "\nTotal Cost .................................. $"+totalPrice
        , "Receipt",JOptionPane.PLAIN_MESSAGE);        
    }
}