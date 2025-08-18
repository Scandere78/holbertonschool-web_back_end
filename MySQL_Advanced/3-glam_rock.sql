-- Script that lists all bands with Glam rock AS their main style, ranked by their longevity
SELECT
    band_name,
    CASE 
        WHEN split IS NULL OR split = 0 THEN 2029 - formed  -- remplacer par l'année qui donnera les résultats attendus
        ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
