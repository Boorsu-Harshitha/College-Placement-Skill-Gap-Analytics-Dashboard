-- ==========================================================
-- COLLEGE PLACEMENT & SKILL-GAP ANALYTICS: SQL PORTFOLIO QUERIES
-- ==========================================================

-- 1. Find the Minimum & Average CGPA required by Placed Students
SELECT 
    ROUND(MIN(CGPA), 2) AS Min_CGPA_Placed,
    ROUND(AVG(CGPA), 2) AS Avg_CGPA_Placed,
    ROUND(MAX(CGPA), 2) AS Max_CGPA_Placed
FROM students_master
WHERE Placement_Status = 'Placed';

-- 2. Calculate Placement Success Rate Boost by Number of Internships
SELECT 
    Internships,
    COUNT(*) AS Total_Students,
    SUM(CASE WHEN Placement_Status = 'Placed' THEN 1 ELSE 0 END) AS Placed_Count,
    ROUND((SUM(CASE WHEN Placement_Status = 'Placed' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS Placement_Rate_Pct
FROM students_master
GROUP BY Internships
ORDER BY Internships;

-- 3. Average Salary Package (LPA) Mapped Against Primary Technical Stack
SELECT 
    Primary_Skill,
    COUNT(Student_ID) AS Hired_Count,
    ROUND(AVG(Salary_LPA), 2) AS Avg_Salary_LPA
FROM students_master
WHERE Placement_Status = 'Placed'
GROUP BY Primary_Skill
ORDER BY Avg_Salary_LPA DESC;

-- 4. Identify High Skill Gaps (Demand vs Student Availability)
SELECT 
    Skill,
    (Student_Availability_Pct * 100) AS Student_Availability_Pct,
    (Job_Demand_Pct * 100) AS Job_Demand_Pct,
    (Gap_Percentage * 100) AS Gap_Percentage,
    Gap_Status
FROM skill_gap_matrix
ORDER BY Gap_Percentage DESC;
