import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load the CSV datasets
df_students = pd.read_csv("students_master.csv")
df_skills = pd.read_csv("skill_gap_matrix.csv")

# 2. Configure Custom Styling & Dark Theme Palette
plt.style.use("dark_background")
fig = plt.figure(figsize=(16, 10), facecolor="#0f172a")

# Create a clean grid layout for 4 key quadrants
gs = fig.add_gridspec(2, 2, hspace=0.38, wspace=0.25)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

# Main Dashboard Title & Subtitle Banner
fig.suptitle(
    "COLLEGE PLACEMENT & SKILL-GAP ANALYTICS DASHBOARD",
    fontsize=16,
    fontweight="bold",
    color="#f8fafc",
    y=0.96,
)
fig.text(
    0.5,
    0.91,
    "Work Recruitment Insights | Placement Rate: 70.0% | Avg Package: 8.2 LPA",
    ha="center",
    fontsize=11,
    color="#94a3b8",
)

# --- Quadrant 1: CGPA vs. Tech Interview Score Correlation ---
sns.scatterplot(
    data=df_students,
    x="CGPA",
    y="Tech_Interview_Score",
    hue="Placement_Status",
    palette={"Placed": "#10b981", "Not Placed": "#ef4444"},
    s=150,
    ax=ax1,
    edgecolor="white",
    linewidth=1.2,
)
ax1.set_title(
    "CGPA vs. Tech Interview Score Correlation",
    fontsize=13,
    fontweight="bold",
    color="#f1f5f9",
)
ax1.set_facecolor("#1e293b")
ax1.grid(color="#334155", linestyle="--", linewidth=0.5)
ax1.legend(loc="upper left", facecolor="#0f172a", edgecolor="#334155")

# --- Quadrant 2: Placement Success Rate by Internships ---
internship_group = (
    df_students.groupby("Internships")["Placement_Status"]
    .apply(lambda x: (x == "Placed").mean() * 100)
    .reset_index(name="Placement_Rate_%")
)
sns.barplot(
    data=internship_group,
    x="Internships",
    y="Placement_Rate_%",
    palette="mako",
    ax=ax2,
)
ax2.set_title(
    "Placement Success Rate (%) by Internships",
    fontsize=13,
    fontweight="bold",
    color="#f1f5f9",
)
ax2.set_facecolor("#1e293b")
ax2.grid(axis="y", color="#334155", linestyle="--", linewidth=0.5)
ax2.set_ylabel("Placement Rate (%)")
ax2.set_xlabel("Number of Internships")
ax2.set_ylim(0, 105)

# --- Quadrant 3: Unique Feature - Skill Gap Matrix ---
skills_melted = df_skills.melt(
    id_vars="Skill",
    value_vars=["Student_Availability_Pct", "Job_Demand_Pct"],
    var_name="Metric",
    value_name="Percentage",
)
skills_melted["Metric"] = skills_melted["Metric"].replace(
    {
        "Student_Availability_Pct": "Student Availability",
        "Job_Demand_Pct": "Job Market Demand",
    }
)
sns.barplot(
    data=skills_melted,
    y="Skill",
    x="Percentage",
    hue="Metric",
    palette=["#38bdf8", "#f43f5e"],
    ax=ax3,
)
ax3.set_title(
    "Skill Gap Matrix: Student Availability vs. Market Demand",
    fontsize=13,
    fontweight="bold",
    color="#f1f5f9",
)
ax3.set_facecolor("#1e293b")
ax3.grid(axis="x", color="#334155", linestyle="--", linewidth=0.5)
ax3.set_xlabel("Ratio")
ax3.set_ylabel("Core Skill")
ax3.legend(loc="lower right", facecolor="#0f172a", edgecolor="#334155")
ax3.set_xlim(0, 1.1)

# --- Quadrant 4: Salary Packages (LPA) by Primary Technical Skill ---
placed_data = df_students[df_students["Placement_Status"] == "Placed"]
sns.boxplot(
    data=placed_data,
    x="Primary_Skill",
    y="Salary_LPA",
    color="#60a5fa",
    ax=ax4,
    boxprops=dict(alpha=0.8),
)
ax4.set_title(
    "Salary Packages (LPA) by Primary Technical Skill",
    fontsize=13,
    fontweight="bold",
    color="#f1f5f9",
)
ax4.set_facecolor("#1e293b")
ax4.grid(axis="y", color="#334155", linestyle="--", linewidth=0.5)
ax4.set_xlabel("Primary Technical Skill")
ax4.set_ylabel("Salary (LPA)")

# 3. Export and Render High-Resolution Image
plt.tight_layout(rect=[0, 0, 1, 0.90])
plt.savefig(
    "college_placement_dashboard.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor(),
    edgecolor="none",
)
plt.show()