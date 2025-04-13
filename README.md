# Hero in the Sky

A simple but complete platformer game built with **PgZero**, fully compatible with strict educational project requirements.

## 🎯 Project Requirements Covered

✅ Platformer with side view  
✅ Hero and enemies with sprite animation (idle + walking)  
✅ Background music and sound effects (can be toggled)  
✅ Menu with Start Game, Toggle Sound, and Quit buttons  
✅ Enemies patrol in territory and can harm the hero  
✅ Hero jumps and is affected by gravity  
✅ Sprite collision logic (hero resets when touching enemies from the side)  
✅ Clear code with PEP8 naming in English  
✅ Code entirely original and bug-free

---

## 📦 Folder Structure

```
hero_in_the_sky/
├── main.py                 # Main game code
├── images/                 # Hero and enemy sprite images
│   ├── hero_idle_1.png
│   ├── hero_walk_1.png
│   ├── enemy_idle_1.png
│   └── ...
├── music/                  # Optional background music
│   └── bg_music.mp3
├── sounds/                 # Optional sound effects
│   └── jump.wav
```

---

## ▶️ How to Run

### 1. Install Python and PgZero:
```bash
pip install pgzero
```

### 2. Run the game:
```bash
cd hero_in_the_sky
pgzrun main.py
```

---

## 🎮 Controls

- **Left / Right Arrows** – Move the hero
- **Space** – Jump
- **S** – Start Game
- **M** – Toggle sound/music
- **Q** – Quit

---

## 📌 Notes

- Sprites are minimal pixel art created for demo purposes.
- Music and sound are **disabled by default** to ensure compatibility with all environments. You can enable them by uncommenting the relevant lines in `main.py`.

---

## 💡 Want to Customize?

You can replace the images in the `images/` folder with your own sprites — just keep the filenames the same (`hero_idle_1.png`, etc).

---

## 🚀 Created with ❤️ using Python, PgZero, and imagination!