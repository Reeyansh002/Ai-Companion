const sendBtn = document.getElementById("sendBtn");
const messageInput = document.getElementById("messageInput");
const replyText = document.getElementById("replyText");
const replyAudio = document.getElementById("replyAudio");

sendBtn.addEventListener("click", async () => {
  const message = messageInput.value;

  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await res.json();
  replyText.textContent = data.reply;

  // Cache-bust so the browser doesn't reuse an old audio file
  replyAudio.src = `http://localhost:8000${data.audio_url}?t=${Date.now()}`;
  replyAudio.play();
});