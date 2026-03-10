const words = [
{english:"Hello", tamil:"வணக்கம்"},
{english:"Thank You", tamil:"நன்றி"},
{english:"Water", tamil:"தண்ணீர்"},
{english:"Food", tamil:"உணவு"},
{english:"Friend", tamil:"நண்பன்"},
{english:"Book", tamil:"புத்தகம்"}
];

let index = 0;

function nextWord(){
index++;
if(index >= words.length){
index = 0;
}

document.getElementById("english").innerText = words[index].english;
document.getElementById("tamil").innerText = words[index].tamil;
}

function speakWord(){
let word = words[index].english;
let speech = new SpeechSynthesisUtterance(word);
speech.lang = "en-US";
speechSynthesis.speak(speech);
}
