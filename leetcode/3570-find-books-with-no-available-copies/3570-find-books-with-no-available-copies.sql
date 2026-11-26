with src as (
    select l.book_id,l.title,l.author,l.genre,l.publication_year,count(b.borrower_name) as current_borrowers,total_copies
from library_books l
left join borrowing_records b on l.book_id = b.book_id where b.return_date is null 
group by l.book_id,l.title,l.author,l.genre,l.publication_year
having total_copies - count(b.borrower_name) = 0
)
select book_id,title,author,genre,publication_year,current_borrowers
from src
order by current_borrowers desc,title