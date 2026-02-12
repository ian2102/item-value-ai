# Item Value AI: In Active Development

Item Value AI predicts the value of high-end items in **Dark and Darker** that are not listed on the in-game marketplace due to price limits. These items are commonly traded through the Trade Post, where pricing is less transparent.

This project uses trade message parsing, machine learning, and OCR to estimate fair market values.

---

## How It Works (Simplified)

### 1. Trade Data Collection + LLM Parsing
- Capture Trade Post network data  
- Extract player trade items and messages  
- Parse messages using an LLM  
- Convert listings into:
  - Structured item data  
  - Normalized price in a common currency  

---

### 2. Model Training
- Use parsed trade data to train a machine learning model  
- Features include:
  - Item type
  - Rarity
  - Attributes
  - Parsed price  

---

### 3. Web App + OCR Pipeline
Users can upload a screenshot of their item.

The system:
1. Uses a custom OCR model trained on the Dark and Darker UI  
2. Extracts item stats and attributes  
3. Formats the data for the prediction model  
4. Returns an estimated trade value  

---

## Goal

To provide accurate pricing insights for high-value items that are not visible on the official marketplace, helping players:

- Avoid underpricing  
- Prevent overpaying  
- Make informed trade decisions  
- Better understand true market demand  

---

## Disclaimer

This project is not affiliated with or endorsed by Ironmace or Dark and Darker.  
Use responsibly and in accordance with the game's terms of service.

