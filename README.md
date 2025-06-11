# ✈️ Jet Survival Game — Pygame Arcade Mini-Project

Fly your jet, dodge rockets, survive as long as possible, and track your time!  
This mini-game is created using **Pygame** and features dynamic sprites, a survival timer, lives (hearts), and a replayable end screen.

---

🎮 FEATURES

- ✈️ Playable Jet with WASD Controls  
- 🚀 Incoming rockets with randomized speeds and spawn locations  
- ☁️ Floating clouds for aesthetic background motion  
- ❤️ 3-Heart health system that visually updates  
- ⏱️ Survival timer display  
- 🔁 Replay system after game over  
- 💨 120 FPS for a smooth experience  

---

📁 FILES NEEDED

- `jet.png` — player sprite  
- `missile.png` — enemy sprite  
- `cloud.png` — background cloud sprite  
- `1heart.png`, `2hearts.png`, `3hearts.png` — life indicators  

---

⚙️ REQUIREMENTS

- Python 3.7+  
- Pygame (Install with: `pip install pygame`)  

---

🕹️ CONTROLS

- `W` = Move Up  
- `S` = Move Down  
- `A` = Move Left  
- `D` = Move Right  
- `ESC` = Quit  
- `R` = Restart (after game over)  

---

🚀 HOW TO PLAY

1. Make sure all required image files are in the same directory as the script.
2. Run the script with:
   python your_script_name.py
3. Use WASD to avoid incoming rockets.
4. Each hit removes one heart. Survive as long as possible!
5. After you lose all 3 hearts, you can restart or quit.

---

📌 GAME LOOP LOGIC

- Real-time event handling for movement, quitting, and spawning.
- Clouds and rockets are spawned every 1 second via timers.
- Collision detection is done with `pygame.sprite.spritecollideany()`.
- When hearts reach 0, survival time is displayed and game pauses.
- Restarting the game resets sprites, timer, and health.

---

🖼️ VISUAL EXAMPLES

✔️ Health HUD is drawn at top-right using `1heart.png`, `2hearts.png`, and `3hearts.png`.  
⏱️ Timer is rendered in real-time at the top-left.  
🪂 Sprites are transformed and scaled for consistency and performance.  

---

📄 LICENSE

This project is licensed for personal and educational use.  
Make sure to credit asset authors if you use this in public projects.

---

🙏 CREDITS

- Pygame — for the 2D game development library  
- Fonts: RobotoMono, Catamaran (used in `pygame.font.SysFont`)  
- You — for making this even better!

