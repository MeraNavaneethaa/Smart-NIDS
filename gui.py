import customtkinter as ctk
import csv
from collections import Counter
from tkinter import filedialog
import pandas as pd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Dashboard:

    def __init__(self):

        self.root = ctk.CTk()
        self.root.geometry("1400x800")
        self.root.title("Smart NIDS Security Center")

        title = ctk.CTkLabel(
            self.root,
            text="SMART NIDS SECURITY CENTER",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=15)

        # ---------- CARDS ----------

        card_frame = ctk.CTkFrame(self.root)
        card_frame.pack(fill="x", padx=20)

        self.logs_card = ctk.CTkLabel(
            card_frame,
            text="Logs\n0",
            width=180,
            height=80,
            corner_radius=15,
            font=("Arial", 24, "bold")
        )
        self.logs_card.pack(side="left", padx=15, pady=10)

        self.warning_card = ctk.CTkLabel(
            card_frame,
            text="Warnings\n0",
            width=180,
            height=80,
            corner_radius=15,
            fg_color="#D4A017",
            font=("Arial", 24, "bold")
        )
        self.warning_card.pack(side="left", padx=15)

        self.critical_card = ctk.CTkLabel(
            card_frame,
            text="Critical\n0",
            width=180,
            height=80,
            corner_radius=15,
            fg_color="#B22222",
            font=("Arial", 24, "bold")
        )
        self.critical_card.pack(side="left", padx=15)

        export_btn = ctk.CTkButton(
            card_frame,
            text="Export Report",
            command=self.export_report
        )
        export_btn.pack(side="right", padx=20)

        # ---------- MAIN AREA ----------

        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=15)

        # ALERTS

        left_frame = ctk.CTkFrame(main_frame)
        left_frame.pack(side="left", fill="both", padx=10)

        alert_title = ctk.CTkLabel(
            left_frame,
            text="Recent Alerts",
            font=("Arial", 20, "bold")
        )
        alert_title.pack(pady=10)

        self.textbox = ctk.CTkTextbox(
            left_frame,
            width=450,
            height=500,
            font=("Consolas", 13)
        )
        self.textbox.pack(padx=10, pady=10)

        # TOP IPS

        right_frame = ctk.CTkFrame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        top_label = ctk.CTkLabel(
            right_frame,
            text="Top Attackers",
            font=("Arial", 20, "bold")
        )
        top_label.pack(pady=10)

        self.top_ips = ctk.CTkTextbox(
            right_frame,
            width=250,
            height=120
        )

        self.top_ips.pack(pady=10)

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=right_frame
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.update_dashboard()

        self.root.mainloop()

    def export_report(self):

        try:
            df = pd.read_csv(
                "logs.csv",
                header=None,
                names=["Time", "IP", "Event", "Level"]
            )

            path = filedialog.asksaveasfilename(
                defaultextension=".csv"
            )

            if path:
                df.to_csv(path, index=False)

        except:
            pass

    def update_dashboard(self):

        self.textbox.delete("1.0", "end")
        self.top_ips.delete("1.0", "end")

        rows = []
        ips = []

        warning = 0
        critical = 0

        try:
            with open("logs.csv", "r") as f:
                reader = csv.reader(f)
                rows = list(reader)

        except:
            pass

        for row in rows[-20:]:

            if len(row) >= 4:

                level = row[3]

                if level == "WARNING":
                    warning += 1

                if level == "CRITICAL":
                    critical += 1

                self.textbox.insert(
                    "end",
                    f"[{level}] {row[1]}\n{row[2]}\n\n"
                )

        for row in rows:

            if len(row) >= 2:
                ips.append(row[1])

        counter = Counter(ips)

        top = counter.most_common(5)

        for ip, count in top:

            self.top_ips.insert(
                "end",
                f"{ip}\nAlerts: {count}\n\n"
            )

        names = [x[0] for x in top]
        counts = [x[1] for x in top]

        self.ax.clear()

        self.ax.bar(names, counts)

        self.ax.set_title("Attack Distribution")

        self.ax.tick_params(axis="x", rotation=20)

        self.canvas.draw()

        self.logs_card.configure(
            text=f"Logs\n{len(rows)}"
        )

        self.warning_card.configure(
            text=f"Warnings\n{warning}"
        )

        self.critical_card.configure(
            text=f"Critical\n{critical}"
        )

        self.root.after(
            3000,
            self.update_dashboard
        )


def show_logs():
    Dashboard()