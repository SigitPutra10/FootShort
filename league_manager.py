from data_handler import load_data, save_data

class LeagueManager:
    def __init__(self):
        self.teams = load_data()  # dictionary: tim -> stats

    def add_team(self, name):
        name = name.strip()
        if not name:
            print("Nama tim tidak boleh kosong!")
            return
        if name in self.teams:
            print("Tim sudah ada!")
            return
        self.teams[name] = {
            "pts": 0, "win":0, "draw":0, "loss":0, "gf":0, "ga":0
        }
        print(f"Tim '{name}' berhasil ditambahkan!")
        self.save()

    def update_team_name(self, old_name, new_name):
        old_name = old_name.strip()
        new_name = new_name.strip()
        
        if old_name not in self.teams:
            print(f"Tim '{old_name}' tidak ditemukan!")
            return
        if not new_name:
            print("Nama tim baru tidak boleh kosong!")
            return
        if new_name in self.teams:
            print(f"Tim '{new_name}' sudah ada!")
            return

        # ganti nama tim, statistik tetap sama
        self.teams[new_name] = self.teams.pop(old_name)
        print(f"Nama tim '{old_name}' berhasil diubah menjadi '{new_name}'")
        self.save()

    def delete_team(self, name):
        if name in self.teams:
            del self.teams[name]
            print(f"Tim '{name}' dihapus.")
            self.save()
        else:
            print("Tim tidak ditemukan!")

    def list_teams(self):
        if not self.teams:
            print("Belum ada tim.")
            return
        print("Daftar Tim:")
        for t in self.teams:
            print(f"- {t}")

    def input_match(self, home, away, home_goals, away_goals):
        if home not in self.teams or away not in self.teams:
            print("Salah satu tim tidak ada!")
            return
        h = self.teams[home]
        a = self.teams[away]

        h["gf"] += home_goals
        h["ga"] += away_goals
        a["gf"] += away_goals
        a["ga"] += home_goals

        if home_goals > away_goals:
            h["pts"] += 3
            h["win"] += 1
            a["loss"] += 1
        elif home_goals < away_goals:
            a["pts"] += 3
            a["win"] += 1
            h["loss"] += 1
        else:
            h["pts"] += 1
            a["pts"] += 1
            h["draw"] += 1
            a["draw"] += 1

        print(f"Pertandingan '{home} {home_goals}-{away_goals} {away}' berhasil dicatat!")
        self.save()

    def show_leaderboard(self):
        if not self.teams:
            print("Belum ada tim.")
            return
        
        leaderboard = sorted(
            self.teams.items(),
            key=lambda x: (x[1]["pts"], x[1]["gf"]-x[1]["ga"], x[1]["gf"]),
            reverse=True
        )

        # header
        print("\n--- Klasemen ---")
        print(f"{'No':<3} {'Tim':<20} {'Pts':<4} {'W':<2} {'D':<2} {'L':<2} {'GF':<3} {'GA':<3} {'GD':<3}")
        print("-" * 50)
        
        for idx, (name, stats) in enumerate(leaderboard, 1):
            gd = stats["gf"] - stats["ga"]
            print(f"{idx:<3} {name:<20} {stats['pts']:<4} {stats['win']:<2} {stats['draw']:<2} {stats['loss']:<2} {stats['gf']:<3} {stats['ga']:<3} {gd:<3}")

        print("-" * 50 + "\n")

    def save(self):
        save_data(self.teams)