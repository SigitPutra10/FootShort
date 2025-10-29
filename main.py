from league_manager import LeagueManager

def main():
    lm = LeagueManager()
    print("=== Selamat datang di Manajemen Liga Sepak Bola ===")

    while True:
        print("\nMenu:")
        print("1. Lihat Daftar Tim")
        print("2. Tambah Tim")
        print("3. Ubah Nama Tim")
        print("4. Hapus Tim")
        print("5. Input Hasil Pertandingan")
        print("6. Lihat Klasemen / Leaderboard")
        print("7. Keluar")

        choice = input("Pilih menu (1-7): ").strip()

        if choice == "1":
            lm.list_teams()

        elif choice == "2":
            name = input("Nama Tim: ")
            lm.add_team(name)

        elif choice == "3":
            lm.list_teams()
            old_name = input("Nama Tim Lama: ")
            new_name = input("Nama Tim Baru: ")
            lm.update_team_name(old_name, new_name)

        elif choice == "4":
            lm.list_teams()
            name = input("Nama Tim yang akan dihapus: ")
            lm.delete_team(name)

        elif choice == "5":
            lm.list_teams()
            home = input("Tim Home: ")
            away = input("Tim Away: ")
            try:
                hg = int(input(f"Skor {home}: "))
                ag = int(input(f"Skor {away}: "))
                lm.input_match(home, away, hg, ag)
            except ValueError:
                print("Skor harus berupa angka!")

        elif choice == "6":
            lm.show_leaderboard()

        elif choice == "7":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
