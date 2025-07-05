const questions = [
  { q: "What is 2 + 2?", choices: ["3", "4", "5"], answer: "4" },
  { q: "Capital of Vietnam?", choices: ["Hanoi", "HCM", "Hue"], answer: "Hanoi" }
];

let score = 0;
const quizEl = document.getElementById("quiz");

questions.forEach((q) => {
  const div = document.createElement("div");
  div.innerHTML = `<p>${q.q}</p>`;
  q.choices.forEach(c => {
    const btn = document.createElement("button");
    btn.innerText = c;
    btn.onclick = () => {
      if (c === q.answer) {
        score++;
        document.getElementById("score").innerText = score;
      }
      div.remove();
    };
    div.appendChild(btn);
  });
  quizEl.appendChild(div);
});
