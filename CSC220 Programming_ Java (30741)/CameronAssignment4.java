// Cameron McClellan
// 10/23/25
// Ask user what type of scoring they want then begin rolling dice
// 1 hour

import javax.swing.JOptionPane;
import java.util.Random;

public class CameronAssignment4
{
    public static void main(String[] args)
    {
        //Variables
        int gamemode;
        gamemode = JOptionPane.showOptionDialog(null, 
                "Click OK to continue", 
                "Warning", 
                JOptionPane.DEFAULT_OPTION, 
                JOptionPane.WARNING_MESSAGE, 
                null, 
                new Object[]{ "Total Amount", "Total Wins" }, 
                "Total Amount");
        int loopCount = 10;
        int myRoll;
        int cpuRoll;
        int myTotal = 0;
        int cpuTotal = 0;
        Random randomNumbers = new Random();
        
        //Main loop
        while (loopCount > 0)
        {
            myRoll = randomNumbers.nextInt(6)+1;
            cpuRoll = randomNumbers.nextInt(6)+1;
            if (gamemode == 0)
            {
                myTotal = myRoll+myTotal;
                cpuTotal = cpuRoll+cpuTotal;
            }
            else if (gamemode == 1)
            {
                if (myRoll < cpuRoll) { cpuTotal ++; }
                else if (myRoll > cpuRoll) { myTotal ++; }
            }
            
            JOptionPane.showMessageDialog(null , "You rolled: " + myRoll + "\nCPU rolled: " + cpuRoll + "\n\nScore: " + myTotal + " - " + cpuTotal);
            
            loopCount --;
        }
        
        //Conclusion
        if (cpuTotal == myTotal) { JOptionPane.showMessageDialog(null , "It's a TIE\n\nScore: " + myTotal + " - " + cpuTotal); }
        else if (cpuTotal > myTotal) { JOptionPane.showMessageDialog(null , "CPU WINS\n\nScore: " + myTotal + " - " + cpuTotal); }
        else if (cpuTotal < myTotal) { JOptionPane.showMessageDialog(null , "Player WINS\n\nScore: " + myTotal + " - " + cpuTotal); }
        else { JOptionPane.showMessageDialog(null , "An error has occured..."); }
    }
}