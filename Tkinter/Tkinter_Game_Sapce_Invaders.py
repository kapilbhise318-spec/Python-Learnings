import tkinter as tk
import random
import time

# ── Constants ──────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 800, 600
BG = "#0a0a1a"
PLAYER_COLOR = "#00ffcc"
BULLET_COLOR = "#ffff00"
ENEMY_BULLET_COLOR = "#ff4444"
BARRIER_COLOR = "#44ff44"
FPS = 60

ALIEN_ROWS = 4
ALIEN_COLS = 10
ALIEN_W, ALIEN_H = 36, 24
ALIEN_PAD_X, ALIEN_PAD_Y = 14, 14

PLAYER_W, PLAYER_H = 50, 24
PLAYER_SPEED = 6
BULLET_SPEED = 10
ENEMY_BULLET_SPEED = 5

ALIEN_COLORS = ["#ff6ec7", "#ff6ec7", "#c67cff", "#c67cff", "#7cffec", "#7cffec", "#ffca7c", "#ffca7c"]


class SpaceInvaders:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
        self.canvas.pack()

        self.keys = {}
        self.root.bind("<KeyPress>", lambda e: self.keys.update({e.keysym: True}))
        self.root.bind("<KeyRelease>", lambda e: self.keys.update({e.keysym: False}))
        self.root.bind("<space>", lambda e: self.shoot())
        self.root.bind("<r>", lambda e: self.restart())
        self.root.bind("<R>", lambda e: self.restart())

        self.init_game()
        self.loop()

    # ── Setup ──────────────────────────────────────────────────────────────────
    def init_game(self):
        self.canvas.delete("all")
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.won = False
        self.shoot_cooldown = 0
        self.enemy_shoot_timer = 0
        self.enemy_shoot_interval = 90   # frames
        self.alien_move_timer = 0
        self.alien_move_interval = 40
        self.alien_direction = 1          # 1 = right, -1 = left
        self.alien_drop = False
        self.player_bullets = []
        self.enemy_bullets = []
        self.explosions = []

        # Stars
        self.stars = []
        for _ in range(120):
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            r = random.random()
            c = self.canvas.create_oval(x, y, x+1, y+1,
                fill=random.choice(["#ffffff","#aaaaff","#ffddff"]), outline="")
            self.stars.append((c, r))

        # Player
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - 50
        self.player_id = self._draw_player(self.player_x, self.player_y)

        # Aliens
        self.aliens = []
        self._spawn_aliens()

        # Barriers
        self.barriers = []
        self._create_barriers()

        # HUD
        self.score_text = self.canvas.create_text(
            10, 10, anchor="nw", text="SCORE: 0",
            fill="#ffffff", font=("Courier", 14, "bold"))
        self.lives_text = self.canvas.create_text(
            WIDTH-10, 10, anchor="ne", text="LIVES: ♥♥♥",
            fill="#ff6e6e", font=("Courier", 14, "bold"))
        self.level_text = self.canvas.create_text(
            WIDTH//2, 10, anchor="n", text="LEVEL 1",
            fill="#aaaaff", font=("Courier", 14, "bold"))

    def _draw_player(self, x, y):
        pts = [
            x, y - PLAYER_H//2,
            x - 8, y - PLAYER_H//2 + 10,
            x - PLAYER_W//2, y + PLAYER_H//2,
            x + PLAYER_W//2, y + PLAYER_H//2,
            x + 8, y - PLAYER_H//2 + 10,
        ]
        return self.canvas.create_polygon(pts, fill=PLAYER_COLOR, outline="#00ffff", width=1)

    def _spawn_aliens(self):
        start_x = 80
        start_y = 80
        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                x = start_x + col * (ALIEN_W + ALIEN_PAD_X)
                y = start_y + row * (ALIEN_H + ALIEN_PAD_Y)
                color = ALIEN_COLORS[row % len(ALIEN_COLORS)]
                ids = self._draw_alien(x, y, color, row)
                self.aliens.append({
                    "x": x, "y": y, "color": color,
                    "row": row, "ids": ids, "alive": True
                })

    def _draw_alien(self, x, y, color, row):
        ids = []
        hw, hh = ALIEN_W//2, ALIEN_H//2
        # Body
        ids.append(self.canvas.create_rectangle(
            x-hw+4, y-hh, x+hw-4, y+hh, fill=color, outline=color))
        # Eyes
        ids.append(self.canvas.create_oval(
            x-hw+8, y-hh+4, x-hw+14, y-hh+10, fill="white", outline=""))
        ids.append(self.canvas.create_oval(
            x+hw-14, y-hh+4, x+hw-8, y-hh+10, fill="white", outline=""))
        # Legs
        for lx in [x-hw+2, x-hw+10, x+hw-10, x+hw-2]:
            ids.append(self.canvas.create_line(lx, y+hh, lx, y+hh+5, fill=color, width=2))
        # Antennae
        ids.append(self.canvas.create_line(x-8, y-hh, x-14, y-hh-7, fill=color, width=2))
        ids.append(self.canvas.create_line(x+8, y-hh, x+14, y-hh-7, fill=color, width=2))
        return ids

    def _create_barriers(self):
        positions = [140, 280, 420, 560, 700]
        for bx in positions:
            by = HEIGHT - 110
            blocks = []
            for r in range(4):
                for c in range(6):
                    bk = self.canvas.create_rectangle(
                        bx + c*9, by + r*9,
                        bx + c*9 + 8, by + r*9 + 8,
                        fill=BARRIER_COLOR, outline="")
                    blocks.append({"id": bk, "x": bx+c*9, "y": by+r*9, "hp": 3})
            self.barriers.extend(blocks)

    # ── Main Loop ─────────────────────────────────────────────────────────────
    def loop(self):
        if not self.game_over and not self.won:
            self.update()
        self.root.after(1000 // FPS, self.loop)

    def update(self):
        self._scroll_stars()
        self._move_player()
        self._move_bullets()
        self._move_aliens()
        self._enemy_shoot()
        self._check_collisions()
        self._update_explosions()
        self._update_hud()
        self.shoot_cooldown = max(0, self.shoot_cooldown - 1)
        self.alien_move_timer += 1
        self.enemy_shoot_timer += 1

    def _scroll_stars(self):
        for c, speed in self.stars:
            self.canvas.move(c, 0, speed * 0.3)
            coords = self.canvas.coords(c)
            if coords[1] > HEIGHT:
                self.canvas.coords(c, random.randint(0, WIDTH), 0,
                                   random.randint(0, WIDTH)+1, 1)

    def _move_player(self):
        dx = 0
        if self.keys.get("Left") or self.keys.get("a"):
            dx = -PLAYER_SPEED
        if self.keys.get("Right") or self.keys.get("d"):
            dx = PLAYER_SPEED
        self.player_x = max(PLAYER_W//2, min(WIDTH - PLAYER_W//2, self.player_x + dx))
        self.canvas.coords(self.player_id,
            self.player_x, self.player_y - PLAYER_H//2,
            self.player_x - 8, self.player_y - PLAYER_H//2 + 10,
            self.player_x - PLAYER_W//2, self.player_y + PLAYER_H//2,
            self.player_x + PLAYER_W//2, self.player_y + PLAYER_H//2,
            self.player_x + 8, self.player_y - PLAYER_H//2 + 10)

    def shoot(self):
        if self.game_over or self.won:
            return
        if self.shoot_cooldown <= 0:
            bx, by = self.player_x, self.player_y - PLAYER_H//2
            bid = self.canvas.create_rectangle(
                bx-3, by-12, bx+3, by, fill=BULLET_COLOR, outline="")
            self.player_bullets.append({"id": bid, "x": bx, "y": by})
            self.shoot_cooldown = 20

    def _move_bullets(self):
        for b in self.player_bullets[:]:
            b["y"] -= BULLET_SPEED
            self.canvas.move(b["id"], 0, -BULLET_SPEED)
            if b["y"] < 0:
                self.canvas.delete(b["id"])
                self.player_bullets.remove(b)

        for b in self.enemy_bullets[:]:
            b["y"] += ENEMY_BULLET_SPEED
            self.canvas.move(b["id"], 0, ENEMY_BULLET_SPEED)
            if b["y"] > HEIGHT:
                self.canvas.delete(b["id"])
                self.enemy_bullets.remove(b)

    def _move_aliens(self):
        speed = max(4, 4 + self.level * 2)
        interval = max(8, self.alien_move_interval - self.level * 3 -
                       (ALIEN_ROWS * ALIEN_COLS - sum(1 for a in self.aliens if a["alive"])) * 2)

        if self.alien_move_timer < interval:
            return
        self.alien_move_timer = 0

        alive = [a for a in self.aliens if a["alive"]]
        if not alive:
            return

        dx = speed * self.alien_direction
        dy = 0

        # Check edges
        xs = [a["x"] for a in alive]
        if self.alien_direction == 1 and max(xs) + ALIEN_W//2 + dx > WIDTH - 20:
            self.alien_direction = -1
            dy = 18
            dx = 0
        elif self.alien_direction == -1 and min(xs) - ALIEN_W//2 + dx < 20:
            self.alien_direction = 1
            dy = 18
            dx = 0

        for a in alive:
            a["x"] += dx
            a["y"] += dy
            for iid in a["ids"]:
                self.canvas.move(iid, dx, dy)

            # Aliens reached bottom
            if a["y"] + ALIEN_H//2 >= self.player_y - PLAYER_H//2:
                self._end_game(won=False)
                return

    def _enemy_shoot(self):
        interval = max(30, self.enemy_shoot_interval - self.level * 10)
        if self.enemy_shoot_timer < interval:
            return
        self.enemy_shoot_timer = 0

        alive = [a for a in self.aliens if a["alive"]]
        if not alive:
            return
        shooter = random.choice(alive)
        bx, by = shooter["x"], shooter["y"] + ALIEN_H//2
        bid = self.canvas.create_oval(
            bx-4, by, bx+4, by+10, fill=ENEMY_BULLET_COLOR, outline="")
        self.enemy_bullets.append({"id": bid, "x": bx, "y": by})

    def _check_collisions(self):
        # Player bullets vs aliens
        for b in self.player_bullets[:]:
            bx, by = b["x"], b["y"]
            for a in self.aliens:
                if not a["alive"]:
                    continue
                if (abs(bx - a["x"]) < ALIEN_W//2 + 3 and
                        abs(by - a["y"]) < ALIEN_H//2 + 6):
                    # Kill alien
                    for iid in a["ids"]:
                        self.canvas.delete(iid)
                    a["alive"] = False
                    self.canvas.delete(b["id"])
                    self.player_bullets.remove(b)
                    self.score += (ALIEN_ROWS - a["row"]) * 10
                    self._explode(a["x"], a["y"], a["color"])
                    break

        # Player bullets vs barriers
        for b in self.player_bullets[:]:
            for blk in self.barriers:
                if blk["hp"] <= 0:
                    continue
                bx2, by2 = b["x"], b["y"]
                if (blk["x"] <= bx2 <= blk["x"]+8 and blk["y"] <= by2 <= blk["y"]+8):
                    blk["hp"] -= 1
                    if blk["hp"] <= 0:
                        self.canvas.delete(blk["id"])
                    else:
                        shade = ["#44ff44","#88aa44","#aa6644"][3 - blk["hp"]]
                        self.canvas.itemconfig(blk["id"], fill=shade)
                    self.canvas.delete(b["id"])
                    if b in self.player_bullets:
                        self.player_bullets.remove(b)
                    break

        # Enemy bullets vs barriers
        for b in self.enemy_bullets[:]:
            for blk in self.barriers:
                if blk["hp"] <= 0:
                    continue
                bx2, by2 = b["x"], b["y"]
                if (blk["x"] <= bx2 <= blk["x"]+8 and blk["y"] <= by2+10 <= blk["y"]+8):
                    blk["hp"] -= 1
                    if blk["hp"] <= 0:
                        self.canvas.delete(blk["id"])
                    else:
                        shade = ["#44ff44","#88aa44","#aa6644"][3 - blk["hp"]]
                        self.canvas.itemconfig(blk["id"], fill=shade)
                    self.canvas.delete(b["id"])
                    if b in self.enemy_bullets:
                        self.enemy_bullets.remove(b)
                    break

        # Enemy bullets vs player
        for b in self.enemy_bullets[:]:
            bx, by = b["x"], b["y"]
            if (abs(bx - self.player_x) < PLAYER_W//2 and
                    abs(by - self.player_y) < PLAYER_H//2 + 5):
                self.canvas.delete(b["id"])
                self.enemy_bullets.remove(b)
                self._explode(self.player_x, self.player_y, PLAYER_COLOR)
                self.lives -= 1
                if self.lives <= 0:
                    self._end_game(won=False)
                else:
                    self._flash_player()

        # All aliens dead → next level
        if all(not a["alive"] for a in self.aliens):
            self._next_level()

    def _explode(self, x, y, color):
        particles = []
        for _ in range(8):
            dx = random.uniform(-4, 4)
            dy = random.uniform(-4, 4)
            pid = self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=color, outline="")
            particles.append({"id": pid, "dx": dx, "dy": dy, "life": 12})
        self.explosions.append(particles)

    def _update_explosions(self):
        for group in self.explosions[:]:
            all_dead = True
            for p in group:
                if p["life"] > 0:
                    self.canvas.move(p["id"], p["dx"], p["dy"])
                    p["life"] -= 1
                    all_dead = False
                else:
                    self.canvas.delete(p["id"])
            if all_dead:
                self.explosions.remove(group)

    def _flash_player(self):
        def toggle(n):
            if n > 0:
                c = BG if n % 2 == 0 else PLAYER_COLOR
                self.canvas.itemconfig(self.player_id, fill=c)
                self.root.after(100, lambda: toggle(n-1))
        toggle(6)

    def _next_level(self):
        self.level += 1
        for b in self.player_bullets + self.enemy_bullets:
            self.canvas.delete(b["id"])
        self.player_bullets.clear()
        self.enemy_bullets.clear()
        self.aliens.clear()
        self._spawn_aliens()
        self.canvas.itemconfig(self.level_text, text=f"LEVEL {self.level}")
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2, text=f"LEVEL {self.level}!",
            fill="#ffffff", font=("Courier", 36, "bold"), tags="levelup")
        self.root.after(1200, lambda: self.canvas.delete("levelup"))

    def _update_hud(self):
        self.canvas.itemconfig(self.score_text, text=f"SCORE: {self.score}")
        hearts = "♥" * self.lives + "♡" * (3 - self.lives)
        self.canvas.itemconfig(self.lives_text, text=f"LIVES: {hearts}")

    def _end_game(self, won=False):
        self.game_over = not won
        self.won = won
        msg = "YOU WIN! 🎉" if won else "GAME OVER"
        color = "#ffff00" if won else "#ff4444"
        self.canvas.create_rectangle(
            WIDTH//2-200, HEIGHT//2-80, WIDTH//2+200, HEIGHT//2+80,
            fill="#000033", outline=color, width=3)
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2 - 30, text=msg,
            fill=color, font=("Courier", 36, "bold"))
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2 + 10, text=f"FINAL SCORE: {self.score}",
            fill="#ffffff", font=("Courier", 18))
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2 + 45, text="Press R to restart",
            fill="#aaaaaa", font=("Courier", 14))

    def restart(self):
        self.init_game()


# ── Entry Point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)

    # Center window
    root.update_idletasks()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root.geometry(f"{WIDTH}x{HEIGHT}+{(sw-WIDTH)//2}+{(sh-HEIGHT)//2}")

    root.mainloop()