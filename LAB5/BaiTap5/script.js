async function getWeather() {
  const selected = document.getElementById("citySelect").value;
  const apiKey = "14cfe9cd1ff007209e39fffd5372779d";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${selected}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("City not found");

    const data = await response.json();
    document.getElementById("weather").innerHTML = `
      <p><strong>${data.name}, ${data.sys.country}</strong></p>
      <p>🌡️ Temp: ${data.main.temp}°C</p>
      <p>☁️ Weather: ${data.weather[0].description}</p>
      <p>💧 Humidity: ${data.main.humidity}%</p>
      <p>🌬️ Wind: ${data.wind.speed} m/s</p>
    `;
  } catch (error) {
    document.getElementById("weather").innerHTML = `<p style="color:red;">${error.message}</p>`;
  }
}
