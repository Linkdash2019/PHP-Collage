// Cameron McClellan
// 10/18/25
// TBD
// TBD

import javax.swing.JOptionPane;

public class CameronAssignment2
{
    public static void main(String[] args)
    {
        //User Variables
        int shares;
        double pricePerShare;
        double commissionPercent;
        //Caculated Variables
        double stockPaid;
        double commissionPaid;
        double totalPaid;
        
        
        //-----DEBUG!!-----
        shares = 600;
        pricePerShare = 21.77;
        commissionPercent = 2;
        System.out.println(shares+" "+pricePerShare+" "+ commissionPercent);
        //-----------------
        
        //User input
        shares = Integer.parseInt(JOptionPane.showInputDialog(null, "How many shares did you buy?"));
        pricePerShare = Float.parseFloat(JOptionPane.showInputDialog(null, "How much did one share cost? (USD)"));
        commissionPercent = Float.parseFloat(JOptionPane.showInputDialog(null, "What is the commission percent?"));
        
        //Calculate
        stockPaid = shares*pricePerShare;
        commissionPaid = (commissionPercent/100)*stockPaid;
        totalPaid = commissionPaid+stockPaid;
        
        //Round to the 2nd decimal place
        stockPaid = Math.round(stockPaid*100);
        stockPaid = stockPaid/100;
        
        commissionPaid = Math.round(commissionPaid*100);
        commissionPaid = commissionPaid/100;
        
        totalPaid = Math.round(totalPaid*100);
        totalPaid = totalPaid/100;
        
        //Output
        JOptionPane.showMessageDialog(null, "Amount paid for stock alone: $"+stockPaid+"\nAmount paid for commission alone: $"+commissionPaid+"\nTotal Paid: $"+totalPaid, "Stats",JOptionPane.INFORMATION_MESSAGE);        
    }
}