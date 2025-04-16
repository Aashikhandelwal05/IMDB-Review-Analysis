async function analyzeReview() {
    const review = document.getElementById("review").value;
    if (!review.trim()) return alert("Please enter a review.");
  
    const response = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ review: review })
    });
  
    const data = await response.json();
  
    document.getElementById("overall").innerText = data.overall_sentiment;
    
    // Aspects
    const aspectList = document.getElementById("aspects");
    aspectList.innerHTML = "";
    for (const [aspect, sentiment] of Object.entries(data.aspect_sentiments)) {
      const li = document.createElement("li");
      li.textContent = `${aspect}: ${sentiment}`;
      aspectList.appendChild(li);
    }
  
    // Emojis
    const emojiList = document.getElementById("emotions");
    emojiList.innerHTML = "";
    data.emojis.forEach((emoji, idx) => {
      const li = document.createElement("li");
      li.textContent = `${emoji}: ${data.emotions[idx]}`;
      emojiList.appendChild(li);
    });
  
    // Summary
    document.getElementById("summary").innerText = data.summary;
  }
  