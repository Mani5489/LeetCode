select distinct a.author_id as id from views a
where a.author_id = a.viewer_id order by a.author_id