# Audio-Compression
Audio Cpmpression using deep learning. 

## Paper Idea

###  Objective
The objective is to represent audio files in such a format which is easier to send when there is a data bottleneck. This evolves representation of audio files in a better format.
.flac/.mp3 files contain alot of information that is repeating. Which is a very inefficient way to transfer music over data. 

### How I'm trying to solve this.
Break alot of songs in a similar genre and break them into "Deltas"(Parts of song of very small length)
Pass this delta through a "Siamese Network" or similar and make a database of deltas and their scores from the "Siamese Network". Hence a song can be represented as a list of scores and is a much better representation sending through a network.

### Construction of Audio from list of scores.
Since, the problem is a network bottleneck and not a processing bottleneck and we can essentaially store a tiny database of audio and scores. You recieve a list of scores/an array and you construct a song and listen it. Instead of you getting thr complete file through the internet. The size of the database can also be adjusted by using a reccomender system because songs of similar genre may share alot of same tones. 

### Processing the constructed Audio
To be Worked/Commented on after the model construction works.

Good Resources to learn from/Reading Material.<br>
* [How audio is stored in computers](https://www.youtube.com/watch?v=1RIA9U5oXro)
* [Digital Audio Article](http://sites.music.columbia.edu/cmc/MusicAndComputers/chapter2/02_01.php)
* [eli5 on Digital Audio](https://www.reddit.com/r/explainlikeimfive/comments/9j7vag/eli5_how_do_computers_store_audio/)
* [Youtube Video](https://www.youtube.com/watch?v=10Xnek9rWzI)
* [Youtube Video](https://www.youtube.com/watch?v=1FyqFqAN9UM)
* [Youtube Video](https://www.youtube.com/watch?v=HlOTuCFtuV8)
* [Youtube Video](https://www.youtube.com/watch?v=g3tfly9mKhY)
