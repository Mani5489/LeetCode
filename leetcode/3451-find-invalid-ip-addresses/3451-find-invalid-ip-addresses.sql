SELECT 
    ip, 
    COUNT(1) AS invalid_count
FROM logs
GROUP BY ip
HAVING 
    (LENGTH(ip) - LENGTH(REPLACE(ip, '.', ''))) + 1 != 4
    OR INET_ATON(ip) IS NULL
    OR ip != INET_NTOA(INET_ATON(ip))
order by invalid_count desc,ip desc