-- Création de la table
CREATE TABLE glam_rock (
    band_name VARCHAR(255),
    lifespan INT
);

-- Insertion des données
INSERT INTO glam_rock (band_name, lifespan)
VALUES ('Alice Cooper', 60);

-- Requête finale
SELECT band_name, lifespan FROM glam_rock;
