// Cameron McClellan
// 11/4/25
// Desc
// 40 min +45 min

import javax.swing.JOptionPane;

public class CameronAssignment5
{
    public static void main(String[] args)
    {  
        int hWidth = Integer.parseInt(JOptionPane.showInputDialog(null, "Head width?"));
        int hHeight = Integer.parseInt(JOptionPane.showInputDialog(null, "Head height?"));
        
        int nWidth = Integer.parseInt(JOptionPane.showInputDialog(null, "Neck width?"));
        int nHeight = Integer.parseInt(JOptionPane.showInputDialog(null, "Neck height?"));
        
        
        int bWidth = Integer.parseInt(JOptionPane.showInputDialog(null, "Body width?"));
        int bHeight = Integer.parseInt(JOptionPane.showInputDialog(null, "Body height?"));
        
        
        //int lWidth = Integer.parseInt(JOptionPane.showInputDialog(null, "Legs width?"));
        int lHeight = Integer.parseInt(JOptionPane.showInputDialog(null, "Legs height?"));
       
        
        int fWidth = Integer.parseInt(JOptionPane.showInputDialog(null, "Feet width?"));
        //int fHeight = Integer.parseInt(JOptionPane.showInputDialog(null, "Feet height?"));
        
        int hpadding = (int) (bWidth - hWidth) / 2;
        int npadding = (int) (bWidth - nWidth) / 2;
        
        head(hWidth, hHeight, hpadding);
        neck(nWidth, nHeight, npadding);
        body(bWidth, bHeight);
        legs(lHeight, bWidth);
        feet(fWidth, bWidth);
    }
    
    public static void head(int width, int height, int padding)
    {
        int ogWidth = width;
        int ogHeight = height;
        int ogPadding = padding;
        
        while (height != 0)
        {
            //Make Padding
            padding = ogPadding;
            while (padding != 0)
            {
                System.out.print(" ");
                padding --;
            }
            
            //Print Line
            while (width != 0)
            {
                if (width == 1 || width == ogWidth) { System.out.print("#"); }
                else if (height == 1 || height == ogHeight) { System.out.print("#"); }
                else { System.out.print(" "); }
                width --;
            }
            System.out.println();
            width = ogWidth;
            height--;
        }   
    }
    
    public static void neck(int width, int height, int padding)
    {
        int ogWidth = width;
        int ogPadding = padding;
        
        while (height != 0)
        {
            //Make Padding
            padding = ogPadding;
            while (padding != 0)
            {
                System.out.print(" ");
                padding --;
            }
            
            //Print Line
            while (width != 0)
            {
                if (width == 1 || width == ogWidth) { System.out.print("|"); }
                else { System.out.print(" "); }
                width --;
            }
            System.out.println();
            width = ogWidth;
            height--;
        }   
    }
    
    public static void body(int width, int height)
    {
        int ogWidth = width;
        
        while (height != 0)
        {
            while (width != 0)
            {
                System.out.print("\u2588");
                width --;
            }
            System.out.println();
            width = ogWidth;
            height--;
        }   
    }
    
    public static void legs(int height, int bWidth)
    {
        int ogWidth = bWidth;
        int padding = (int) (bWidth / 3)+2;
        int width = ogWidth;

        
        while (height != 0)
        {
            //Print Line
            while (width != 0)
            {
                if (width == padding || width == padding*2) { System.out.print("| |"); }
                else { System.out.print(" "); }
                width --;
            }
            System.out.println();
            width = ogWidth;
            height--;
        }   
    }
    
    public static void feet(int width, int bWidth)
    {
        int ogWidth = bWidth;
        int padding = (int)(bWidth/3)+1;
        int count1 = width;
        int count2 = ((bWidth / 3))-width;
          
        //Print Line
        while (bWidth != 0)
        {
            if (bWidth < padding) 
            { 
                if (count1 == 0){System.out.print(" ");}
                else {System.out.print("-"); count1--;}
            }
            else if (bWidth > padding*2) 
            { 
                if (count2 == 0){System.out.print("-");}
                else {System.out.print('-');count2--;}
            }
            else { System.out.print(" ");}
            bWidth --;
        }
    }
}