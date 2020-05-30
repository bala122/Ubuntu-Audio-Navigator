# Ubuntu-Audio-Navigator
This application is aimed at making a simple auxillary ubuntu Audio Navigator that helps in performing basic commands such as increase/decrease volume,accessing directories,making notes,making files ,etc. using voice recognition
In order to make this app run you need to have Python3 aside from the following libraries:
<br/>sounddevice
<br/>numpy
<br/>pylab
<br/>scipy
<br/>speech_recognition
<br/>matplotlib 
<br/>libgnome2-bin

# How to give commands?
As of now the features available are to navigate through primary files such as Desktop,Documents,Music,Videos,Downloads and run  simple applications like firefox and calculator, toggle sound settings, listing files.
In order to navigate, you first need to provide the username of the account you are in for using it in paths.
If you wish to open directories, just say open <foldername> eg- 'Open Desktop'
If you wish to toggle sound settings, just say ' Increase/Decrease volume', 'mute volume' or 'unmute volume'( unmute isn't working as of now)
If you wish to list files in the current directory, just say 'list files'
If you want to run an application, just say 'run <app>' eg- 'run firefox'
