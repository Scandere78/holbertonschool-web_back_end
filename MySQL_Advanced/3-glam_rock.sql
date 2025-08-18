-- Script: 3-glam_rock.sql
-- Objectif: Lister les groupes dont le style principal est Glam rock, classés par durée d'activité (lifespan)

SELECT
    band_name,
    -- Calcul de la durée en années à partir des colonnes formed et split
    CASE 
        WHEN split IS NULL OR split = 0 THEN YEAR(CURDATE()) - formed
        ELSE split - formed
    END AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
