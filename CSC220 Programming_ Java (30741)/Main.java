package com.cameronm.media;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) 
    {
        vhs objVHS1 = new vhs("Dummy Tape 1", "The Internet", "935 Days 16 Hours, 59 Minutes, 24 Seconds");
        vhs objVHS2 = new vhs("Dummy Tape 2", "Test Subject 101", "20 Minutes");
        dvd objDVD1 = new dvd("Dummy Disk 1", "Someone", "Infinite");
        dvd objDVD2 = new dvd("Dummy Disk 2", "Linkdash", "2 Hours, 10 Minutes, 37 Seconds");
        cassette objCass = new cassette("Dummy Cassette 1", "Unkown", "10 Seconds");
        cd objCD = new cd("Dummy CD 1", "Yoda", "3 Minutes 57 Seconds");
        
        ArrayList<MediaCollection> mediaList = new ArrayList<>();
        
        mediaList.add(objVHS1);
        mediaList.add(objVHS2);
        mediaList.add(objDVD1);
        mediaList.add(objDVD2);
        mediaList.add(objCass);
        mediaList.add(objCD);
        
        for(int loopCnt = 0; loopCnt < mediaList.size(); loopCnt++)
        {
            System.out.println("\n"+mediaList.get(loopCnt).toString());
            mediaList.get(loopCnt).playDisk();
            //Maybe later make length int's and pause for the duration of the song.
        }
    }
}
