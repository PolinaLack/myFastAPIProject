
CREATE OR REPLACE FUNCTION check_intervals() RETURNS TRIGGER AS $$
DECLARE
    max_vacation_allowed INT;
    point date;
    qty INT;
BEGIN
    max_vacation_allowed := 3;

    WITH rng(s, e) AS (
      SELECT NEW.start, NEW.end_date
      UNION ALL
      SELECT start, end_date FROM holis_table 
    ),
     points AS (
      SELECT s AS p, +1 AS v FROM rng
      UNION ALL
      SELECT e AS p, -1 AS v FROM rng
    )
    SELECT DISTINCT ON(p) p, sum(v) OVER (ORDER BY p) qty
    INTO point, qty
    FROM points
    ORDER BY p;
    
    IF qty > max_vacation_allowed THEN
        RAISE EXCEPTION 'Too many overlapping intervals' USING ERRCODE = 'P0001';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER before_insert_check
BEFORE INSERT ON holis_table 
FOR EACH ROW
EXECUTE FUNCTION check_intervals();
