SELECT user_id, email 
FROM users 
WHERE (LENGTH(email) - LENGTH(REPLACE(email, '@', ''))) = 1 -- Exactly one @
  AND RIGHT(email, 4) = '.com'                               -- Ends in .com
  -- 1. Check part before @ (Alphanumeric + Underscore)
  AND REGEXP_LIKE(SUBSTR(email, 1, INSTR(email, '@') - 1), '^[a-zA-Z0-9_]+$')
  -- 2. Check part between @ and . (Only Letters)
  AND REGEXP_LIKE(SUBSTR(email, INSTR(email, '@') + 1), '^[a-zA-Z]+\.com$')
  order by user_id
  ;
