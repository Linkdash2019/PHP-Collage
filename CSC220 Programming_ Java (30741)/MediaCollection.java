package com.cameronm.media;

abstract class MediaCollection 
{
    String mediaTitle;
    String mediaArtist;
    String mediaLength;
    String mediaType;
    String mediaSource;
    
    void playDisk()
    {
        System.out.println("Now playing " + mediaTitle+" by " + mediaArtist + " from source " + mediaSource);
    }
    
    void showInfo()
    {
        System.out.println("Title: " + mediaTitle);
        System.out.println("Artist: " + mediaArtist);
        System.out.println("Length: " + mediaLength);
        System.out.println("Media type: " + mediaType);
        System.out.println("Media source: " + mediaSource);
        System.out.println();
        
    }
    
    public String toString()
    {
        return("Title: " + mediaTitle + "\nArtist: " + mediaArtist + "\nMedia Length: " + mediaLength + "\nType: " + mediaType + "\nSource: " + mediaSource);
    }
    
    String getTitle()  { return mediaTitle; }
    String getArtist() { return mediaArtist; }
    String getLegnth() { return mediaLength; }
    String getType()   { return mediaType; }
    String getSource() { return mediaSource; }
}

//Video
abstract class video extends MediaCollection { video(){ mediaType = "VIDEO"; } }

class vhs extends video 
{ 
    vhs(String title, String artist, String length) 
    {
        mediaTitle = title;
        mediaArtist = artist;
        mediaLength = length;
        mediaSource = "VHS";
    }
}

class dvd extends video 
{ 
    dvd(String title, String artist, String length) 
    {
        mediaTitle = title;
        mediaArtist = artist;
        mediaLength = length;
        mediaSource = "DVD"; 
    } 
}

//Audio (Seems simple enough)

abstract class audio extends MediaCollection { audio(){ mediaType = "AUDIO"; } }

class cassette extends audio 
{ 
    cassette(String title, String artist, String length) 
    {
        mediaTitle = title;
        mediaArtist = artist;
        mediaLength = length;
        mediaSource = "Cassette";
    } 
}

class cd extends audio 
{ 
    cd(String title, String artist, String length) 
    {
        mediaTitle = title;
        mediaArtist = artist;
        mediaLength = length;
        mediaSource = "CD"; 
    } 
}