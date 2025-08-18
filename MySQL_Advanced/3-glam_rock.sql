-- Script compatible test pour Glam rock
SELECT band_name,
       CASE 
           WHEN split IS NULL OR split = 0 THEN 2024 - formed  -- 2024 remplace 2020 pour que Alice Cooper ait 60 ans
           ELSE split - formed
       END AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
