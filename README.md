# Musicbot

## Intro

Musicbot uses pytube to download youtube audio into video folder. It uses threading to play music and request for commands simultaneously.

## Example of how it works on terminal
![Example_of_how_it_works_on_terminal](https://github.com/BluePjCookies/Musicbot/blob/main/examples/intro.png)

## Commands

- queue/q
    - Underlines the song that is currently playing.
- skip
    - skips the song and deletes it if loop is set to False
    - just skips the song if loop is set to true
- loop
    - Allow one to loop through the queue
    - if loop is set to False (which is the default), it will delete the audio after the audio has finished playing
- remove xx
    - replace xx with the song number provided by the queue
    - You cannot remove the song which you are currently playing, but you can skip it
- pause
    - pause the song
- play
    - play the song after a pause
- clear
    - remove all the songs except for the song that is currently playing
