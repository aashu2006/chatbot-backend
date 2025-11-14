async function sendMsg() {
  const input = document.getElementById("input");
  const message = input.value.trim();

  if (!message) return;

  addMessage(message, "me");
  input.value = "";

  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  addMessage(data.reply, "bot");
}

function addMessage(text, type) {
  const chat = document.getElementById("chat");
  chat.innerHTML += `<div class="msg ${type}">${text}</div>`;
  chat.scrollTop = chat.scrollHeight;
}
