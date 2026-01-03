SELECT
    c.company_code,
    c.founder,
    count(distinct l.lead_manager_code),
    count(distinct s.senior_manager_code),
    count(distinct m.manager_code),
    count(distinct e.employee_code)
FROM Company c
LEFT JOIN Lead_Manager l ON c.company_code=l.company_code
LEFT JOIN Senior_Manager s ON c.company_code=s.company_code
LEFT JOIN Manager m ON c.company_code=m.company_code
LEFT JOIN Employee e ON c.company_code=e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code