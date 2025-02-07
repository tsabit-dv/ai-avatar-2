async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatbox = document.getElementById("chatbox");

    if (!userInput.trim()) return;

    chatbox.innerHTML += `<p class="user"><strong>Anda:</strong> ${userInput}</p>`;

    let startTime = Date.now();  // Catat waktu mulai

    let response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    let data = await response.json();
    let responseTime = Date.now() - startTime;  // Hitung waktu respons

    let classType = data.source === "NLP" ? "nlp" : "ai";
    chatbox.innerHTML += `<p class="${classType}"><strong>${data.source}:</strong> ${data.response} <em>(${responseTime} ms)</em></p>`;

    // Gunakan text-to-speech untuk membaca jawaban AI
    let speech = new SpeechSynthesisUtterance(data.response);
    speech.lang = "id-ID";  // Bahasa Indonesia
    window.speechSynthesis.speak(speech);

    document.getElementById("userInput").value = "";
    chatbox.scrollTop = chatbox.scrollHeight;
}
