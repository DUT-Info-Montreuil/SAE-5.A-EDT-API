delete FROM university.students;

INSERT INTO university.students (last_name, first_name, user_id, department_id, group_id, subgroup_id)
VALUES
    ---------------------------------
    --INFO
    ---------------------------------
    
    --Groupes A

    --1ère année
    --A1
    ('Lucas', 'Martin', (SELECT id FROM university.users WHERE username = 'hcohen'), 1, 1, 1),
    ('Emma', 'Bernard', (SELECT id FROM university.users WHERE username = 'bhanma'), 1, 1, 1),
    ('Léa', 'Dubois', (SELECT id FROM university.users WHERE username = 'cbrown1'), 1, 1, 1), 
    -- A2
    ('Gabriel', 'Thomas', (SELECT id FROM university.users WHERE username = 'jgross'), 1, 1, 2),
    ('Jade', 'Robert', (SELECT id FROM university.users WHERE username = 'crussell'), 1, 1, 2),
    ('Enzo', 'Richard', (SELECT id FROM university.users WHERE username = 'lgregory'), 1, 1, 2),
    -- 2ème année
    -- A1
    ('Louise', 'Petit', (SELECT id FROM university.users WHERE username = 'vfisher'), 1, 2, 3),
    ('Louis', 'Durand', (SELECT id FROM university.users WHERE username = 'avasquez1'), 1, 2, 3),
    ('Anna', 'Leroy', (SELECT id FROM university.users WHERE username = 'lmiller'), 1, 2, 3),
    --A2
    ('Hugo', 'Moreau', (SELECT id FROM university.users WHERE username = 'jjackson3'), 1, 2, 4),
    ('Manon', 'Simon', (SELECT id FROM university.users WHERE username = 'ahamilton'), 1, 2, 4),
    ('Jules', 'Laurent', (SELECT id FROM university.users WHERE username = 'krobinson1'), 1, 2, 4)
    ,--3ème année
    --A1
    ('Chloé', 'Lefevre', (SELECT id FROM university.users WHERE username = 'gsmith'), 1, 3, 5),
    ('Nathan', 'Garcia', (SELECT id FROM university.users WHERE username = 'bnelson'), 1, 3, 5),
    ('Camille', 'Michel', (SELECT id FROM university.users WHERE username = 'lolson'), 1, 3, 5),
    --A2
    ('Maël', 'Rodriguez', (SELECT id FROM university.users WHERE username = 'ssmith1'), 1, 3, 6),
    ('Lina', 'Martinez', (SELECT id FROM university.users WHERE username = 'dwarner'), 1, 3, 6),
    ('Raphaël', 'Boucher', (SELECT id FROM university.users WHERE username = 'kstewart'), 1, 3, 6),

    --Groupes B

    --1ère année
    --B1
    ('Zoé', 'Dupont', (SELECT id FROM university.users WHERE username = 'jbrown2'), 1, 4, 7),
    ('Noah', 'Lambert', (SELECT id FROM university.users WHERE username = 'jmitchell'), 1, 4, 7),
    ('Alice', 'Bonnet', (SELECT id FROM university.users WHERE username = 'mbradley'), 1, 4, 7),
    --B2
    ('Théo', 'Fernandez', (SELECT id FROM university.users WHERE username = 'kward'), 1, 4, 8),
    ('Eva', 'Lemoine', (SELECT id FROM university.users WHERE username = 'jzamora'), 1, 4, 8),
    ('Liam', 'Roussel', (SELECT id FROM university.users WHERE username = 'mhumphrey'), 1, 4, 8),
    --2ème année
    --B1
    ('Inès', 'Girard', (SELECT id FROM university.users WHERE username = 'mjohnson2'), 1, 5, 9),
    ('Tom', 'Brun', (SELECT id FROM university.users WHERE username = 'thopkins'), 1, 5, 9),
    ('Clara', 'Guillaume', (SELECT id FROM university.users WHERE username = 'bcobb'), 1, 5, 9),
    --B2
    ('Timéo', 'Lucas', (SELECT id FROM university.users WHERE username = 'zsimmons'), 1, 5, 10),
    ('Rose', 'Faure', (SELECT id FROM university.users WHERE username = 'swhite1'), 1, 5, 10),
    ('Leo', 'Henry', (SELECT id FROM university.users WHERE username = 'lbeard'), 1, 5, 10),
    --3ème année
    --B1
    ('Juliett', 'Robin', (SELECT id FROM university.users WHERE username = 'tbauer'), 1, 6, 11),
    ('Ethan', 'Roux', (SELECT id FROM university.users WHERE username = 'jstevens'), 1, 6, 11),
    ('Eléna', 'David', (SELECT id FROM university.users WHERE username = 'mgarcia1'), 1, 6, 11),
    --B2
    ('Arthur', 'Bertrand', (SELECT id FROM university.users WHERE username = 'dgriffith1'), 1, 6, 12),
    ('Lou', 'Perrin', (SELECT id FROM university.users WHERE username = 'pmiller1'), 1, 6, 12),
    ('Samuel', 'Lambert', (SELECT id FROM university.users WHERE username = 'cscott'), 1, 6, 12),

    --Groupes C

    --1ère année
    --C1
    ('Océane', 'Gauthier', (SELECT id FROM university.users WHERE username = 'awhite1'), 1, 7, 13),
    ('Yanis', 'Morel', (SELECT id FROM university.users WHERE username = 'sball'), 1, 7, 13),
    ('Sarah', 'Simon', (SELECT id FROM university.users WHERE username = 'mjennings'), 1, 7, 13),
    --C2
    ('Milo', 'Caron', (SELECT id FROM university.users WHERE username = 'aroth'), 1, 7, 14),
    ('Charlot', 'Lefevre', (SELECT id FROM university.users WHERE username = 'rrivera'), 1, 7, 14),
    ('Adam', 'Andre', (SELECT id FROM university.users WHERE username = 'erichard'), 1, 7, 14),
    --2ème année
    --C1
    ('Maëlys', 'Fournier', (SELECT id FROM university.users WHERE username = 'mgutierrez1'), 1, 8, 15),
    ('Rayan', 'Vincent', (SELECT id FROM university.users WHERE username = 'dstein'), 1, 8, 15),
    ('Manuela', 'Vidal', (SELECT id FROM university.users WHERE username = 'mpatel'), 1, 8, 15),
    --C2
    ('Maëlle', 'Henry', (SELECT id FROM university.users WHERE username = 'cgray'), 1, 8, 16),
    ('Martin', 'Roussel', (SELECT id FROM university.users WHERE username = 'lwilliams1'), 1, 8, 16),
    ('Elsa', 'Lucas', (SELECT id FROM university.users WHERE username = 'shall'), 1, 8, 16),
    --3ème année--C1
    ('Lucas', 'Philippe', (SELECT id FROM university.users WHERE username = 'mwatson1'), 1, 9, 17),
    ('Léna', 'Renaud', (SELECT id FROM university.users WHERE username = 'dgonzalez'), 1, 9, 17),
    ('Paul', 'Leroux', (SELECT id FROM university.users WHERE username = 'arobinson'), 1, 9, 17),
    --C2
    ('Louane', 'Noel', (SELECT id FROM university.users WHERE username = 'dkane'), 1, 9, 18),
    ('Théa', 'Muller', (SELECT id FROM university.users WHERE username = 'aklein1'), 1, 9, 18),
    ('Axel', 'Chevalier', (SELECT id FROM university.users WHERE username = 'pobrien'), 1, 9, 18),
    --Groupes App
    --2ème année
    ('Elise', 'Blanche', (SELECT id FROM university.users WHERE username = 'cfoley'), 1, 11, 19),
    ('Noah', 'Renard', (SELECT id FROM university.users WHERE username = 'jgarcia1'), 1, 11, 19),
    ('Margaux', 'Picard', (SELECT id FROM university.users WHERE username = 'sbrown'), 1, 11, 19),
    --3ème année
    ('Lucas', 'Legrand', (SELECT id FROM university.users WHERE username = 'mskinner'), 1, 11, 20),
    ('Romane', 'Giraud', (SELECT id FROM university.users WHERE username = 'mfowler'), 1, 11, 20),
    ('Sacha', 'Lefevre', (SELECT id FROM university.users WHERE username = 'dmorrison'), 1, 11, 20),
    

    ---------------------------------
    --QLIO
    ---------------------------------
    
    --Groupes A

    --1ère année
    --A1
    ('Zoé', 'Nicolas', (SELECT id FROM university.users WHERE username = 'nwhite'), 2, 12, 21),
    ('Jules', 'Rolland', (SELECT id FROM university.users WHERE username = 'kjohnson1'), 2, 12, 21),
    ('Léa', 'Gallet', (SELECT id FROM university.users WHERE username = 'dsantos'), 2, 12, 21),
    --A2
    ('Maxime', 'Joly', (SELECT id FROM university.users WHERE username = 'dfoster'), 2, 12, 22),
    ('Clara', 'Rousseau', (SELECT id FROM university.users WHERE username = 'jsmith4'), 2, 12, 22),
    ('Ethan', 'Morin', (SELECT id FROM university.users WHERE username = 'jsantiago'), 2, 12, 22),
    --2ème année
    --A1
    ('Lily', 'Leger', (SELECT id FROM university.users WHERE username = 'gmartin'), 2, 13, 23),
    ('Tom', 'Remy', (SELECT id FROM university.users WHERE username = 'kwilliams'), 2, 13, 23),
    ('Ambre', 'Hebert', (SELECT id FROM university.users WHERE username = 'mhenry'), 2, 13, 23),
    --A2
    ('Théo', 'Julien', (SELECT id FROM university.users WHERE username = 'svelez1'), 2, 13, 24),
    ('Zoé', 'Prevost', (SELECT id FROM university.users WHERE username = 'ljennings'), 2, 13, 24),
    ('Robin', 'Renard', (SELECT id FROM university.users WHERE username = 'mdavis2'), 2, 13, 24),
    --3ème année
    --A1
    ('Manon', 'Leclerc', (SELECT id FROM university.users WHERE username = 'rreeves'), 2, 14, 25),
    ('Maxime', 'Gerard', (SELECT id FROM university.users WHERE username = 'jjackson2'), 2, 14, 25),
    ('Lou', 'Lebrun', (SELECT id FROM university.users WHERE username = 'skemp'), 2, 14, 25),
    --A2
    ('Raphaël', 'Michel', (SELECT id FROM university.users WHERE username = 'jpeters'), 2, 14, 26),
    ('Jade', 'Faure', (SELECT id FROM university.users WHERE username = 'khunt'), 2, 14, 26),
    ('Léo', 'Fournier', (SELECT id FROM university.users WHERE username = 'mdudley'), 2, 14, 26),

    --Groupes B

    --1ère année
    --B1
    ('Nina', 'Perrin', (SELECT id FROM university.users WHERE username = 'avasquez'), 2, 15, 27),
    ('Paul', 'Roy', (SELECT id FROM university.users WHERE username = 'kdoyle'), 2, 15, 27),
    ('Margaux', 'Mathieu', (SELECT id FROM university.users WHERE username = 'rclarke'), 2, 15, 27),
    --B2
    ('Gabriel', 'Caron', (SELECT id FROM university.users WHERE username = 'hmoore1'), 2, 15, 28),
    ('Sarah', 'Masson', (SELECT id FROM university.users WHERE username = 'kcox'), 2, 15, 28),
    ('Thomas', 'Guerin', (SELECT id FROM university.users WHERE username = 'awillis1'), 2, 15, 28),
    --2ème année--B1
    ('Juliett', 'Julien', (SELECT id FROM university.users WHERE username = 'jskinner'), 2, 16, 29),
    ('Matéo', 'Marchand', (SELECT id FROM university.users WHERE username = 'ajames'), 2, 16, 29),
    ('Camille', 'Denis', (SELECT id FROM university.users WHERE username = 'jmaddox'), 2, 16, 29),
    --B2
    ('Emma', 'Perrin', (SELECT id FROM university.users WHERE username = 'jcooley'), 2, 16, 30),
    ('Baptist', 'Lambert', (SELECT id FROM university.users WHERE username = 'sgould'), 2, 16, 30),
    ('Manon', 'Michel', (SELECT id FROM university.users WHERE username = 'rpeters'), 2, 16, 30),
    --3ème année
    --B1
    ('Alexand', 'Renard', (SELECT id FROM university.users WHERE username = 'lwhite1'), 2, 17, 31),
    ('Emma', 'Joly', (SELECT id FROM university.users WHERE username = 'cgonzalez'), 2, 17, 31),
    ('Liam', 'Giraud', (SELECT id FROM university.users WHERE username = 'sjordan1'), 2, 17, 31),
    --B2
    ('Lilou', 'Nicolas', (SELECT id FROM university.users WHERE username = 'jlove'), 2, 17, 32),
    ('Noah', 'Renault', (SELECT id FROM university.users WHERE username = 'lheath'), 2, 17, 32),
    ('Lola', 'Lucas', (SELECT id FROM university.users WHERE username = 'bramos'), 2, 17, 32),
    
    --Groupes C
    
    --1ère année
    --C1
    ('Lucas', 'Faure', (SELECT id FROM university.users WHERE username = 'dbrown1'), 2, 18, 33),
    ('Emma', 'Lambert', (SELECT id FROM university.users WHERE username = 'mphillips'), 2, 18, 33),
    ('Hugo', 'Bernard', (SELECT id FROM university.users WHERE username = 'ljackson'), 2, 18, 33),
    --C2
    ('Léa', 'Durand', (SELECT id FROM university.users WHERE username = 'dsmith2'), 2, 18, 34),
    ('Adam', 'Thomas', (SELECT id FROM university.users WHERE username = 'pklein'), 2, 18, 34),
    ('Lucie', 'Robert', (SELECT id FROM university.users WHERE username = 'jmartinez'), 2, 18, 34),
    --2ème année
    --C1
    ('Nathan', 'Richard', (SELECT id FROM university.users WHERE username = 'jreynolds'), 2, 19, 35),
    ('Julia', 'Petit', (SELECT id FROM university.users WHERE username = 'cjarvis'), 2, 19, 35),
    ('Gabriel', 'Moreau', (SELECT id FROM university.users WHERE username = 'acook'), 2, 19, 35),
    --C2
    ('Emma', 'Simon', (SELECT id FROM university.users WHERE username = 'rgonzales'), 2, 19, 36),
    ('Louis', 'Laurent', (SELECT id FROM university.users WHERE username = 'lcampbell1'), 2, 19, 36),
    ('Juliett', 'Lefevre', (SELECT id FROM university.users WHERE username = 'aperry1'), 2, 19, 36),
    --3ème année
    --C1
    ('Sacha', 'Garcia', (SELECT id FROM university.users WHERE username = 'jjohnston'), 2, 20, 37),
    ('Chloé', 'Michel', (SELECT id FROM university.users WHERE username = 'sgordon'), 2, 20, 37),
    ('Arthur', 'Rodriguez', (SELECT id FROM university.users WHERE username = 'csanchez'), 2, 20, 37),
    --C2
    ('Louise', 'Martinez', (SELECT id FROM university.users WHERE username = 'lshelton'), 2, 20, 38),
    ('Raphaël', 'Boucher', (SELECT id FROM university.users WHERE username = 'aadams2'), 2, 20, 38),
    ('Lina', 'Dupont', (SELECT id FROM university.users WHERE username = 'rwilliams'), 2, 20, 38),
    --Groupes App
    --2ème année
    ('Liam', 'Lambert', (SELECT id FROM university.users WHERE username = 'lmcdonald'), 2, 21, 39),
    ('Eva', 'Bonnet', (SELECT id FROM university.users WHERE username = 'cjohnston'), 2, 21, 39),
    ('Tom', 'Fernandez', (SELECT id FROM university.users WHERE username = 'jsmith3'), 2, 21, 39),
    --3ème année
    ('Zoé', 'Lemoine', (SELECT id FROM university.users WHERE username = 'bcoffey'), 2, 22, 40),
    ('Ethan', 'Roussel', (SELECT id FROM university.users WHERE username = 'redwards'), 2, 22, 40),
    ('Jade', 'Girard', (SELECT id FROM university.users WHERE username = 'ssanders'), 2, 22, 40),
    

    ---------------------------------
    --INFOCOM
    ---------------------------------
    
    --Groupes A
    
    --1ère année
    --A1
    ('Théo', 'Brun', (SELECT id FROM university.users WHERE username = 'jluna'), 3, 23, 41),
    ('Léa', 'Guillaume', (SELECT id FROM university.users WHERE username = 'agoodwin'), 3, 23, 41),
    ('Noah', 'Lucas', (SELECT id FROM university.users WHERE username = 'drodriguez1'), 3, 23, 41),
    --A2
    ('Camille', 'Faure', (SELECT id FROM university.users WHERE username = 'jstewart2'), 3, 23, 42),
    ('Louis', 'Henry', (SELECT id FROM university.users WHERE username = 'tbradford'), 3, 23, 42),
    ('Emma', 'Robin', (SELECT id FROM university.users WHERE username = 'sschroeder'), 3, 23, 42),
    --2ème année
    --A1
    ('Hugo', 'Roux', (SELECT id FROM university.users WHERE username = 'lwilkerson'), 3, 24, 43),
    ('Clara', 'David', (SELECT id FROM university.users WHERE username = 'kthompson'), 3, 24, 43),
    ('Gabriel', 'Bertrand', (SELECT id FROM university.users WHERE username = 'cberry'), 3, 24, 43),
    --A2
    ('Juliett', 'Perrin', (SELECT id FROM university.users WHERE username = 'jmorales'), 3, 24, 44),
    ('Jules', 'Lambert', (SELECT id FROM university.users WHERE username = 'shoffman'), 3, 24, 44),
    ('Léa', 'Gauthier', (SELECT id FROM university.users WHERE username = 'jmeadows1'), 3, 24, 44),
    --3ème année
    --A1
    ('Chloé', 'Morel', (SELECT id FROM university.users WHERE username = 'cporter'), 3, 25, 45),
    ('Tom', 'Simon', (SELECT id FROM university.users WHERE username = 'mmiller3'), 3, 25, 45),
    ('Eva', 'Caron', (SELECT id FROM university.users WHERE username = 'jcampbell'), 3, 25, 45),
    --A2
    ('Nathan', 'Lefevre', (SELECT id FROM university.users WHERE username = 'jpalmer1'), 3, 25, 46),
    ('Lily', 'Andre', (SELECT id FROM university.users WHERE username = 'bphelps'), 3, 25, 46),
    ('Lucas', 'Fournier', (SELECT id FROM university.users WHERE username = 'dreed2'), 3, 25, 46),
    
    --Groupes B

    --1ère année
    --B1
    ('Sarah', 'Vincent', (SELECT id FROM university.users WHERE username = 'kwillis'), 3, 26, 47),
    ('Théo', 'Vidal', (SELECT id FROM university.users WHERE username = 'rgonzalez'), 3, 26, 47),
    ('Emma', 'Henry', (SELECT id FROM university.users WHERE username = 'asaunders'), 3, 26, 47),
    --B2
    ('Liam', 'Roussel', (SELECT id FROM university.users WHERE username = 'jgomez'), 3, 26, 48),
    ('Manon', 'Lucas', (SELECT id FROM university.users WHERE username = 'lsharp'), 3, 26, 48),
    ('Noah', 'Philippe', (SELECT id FROM university.users WHERE username = 'tturner'), 3, 26, 48),
    --2ème année
    --B1
    ('Inès', 'Renaud', (SELECT id FROM university.users WHERE username = 'kchase'), 3, 27, 49),
    ('Lucas', 'Leroux', (SELECT id FROM university.users WHERE username = 'sallen'), 3, 27, 49),
    ('Zoé', 'Noel', (SELECT id FROM university.users WHERE username = 'dgonzales1'), 3, 27, 49),
    --B2
    ('Léa', 'Muller', (SELECT id FROM university.users WHERE username = 'jellis'), 3, 27, 50),
    ('Hugo', 'Chevalier', (SELECT id FROM university.users WHERE username = 'jballard'), 3, 27, 50),
    ('Eléna', 'Blanche', (SELECT id FROM university.users WHERE username = 'tcurtis'), 3, 27, 50),
    --3ème année
    --B1
    ('Gabriel', 'Renard', (SELECT id FROM university.users WHERE username = 'jblake'), 3, 28, 51),
    ('Clara', 'Picard', (SELECT id FROM university.users WHERE username = 'lwhitaker'), 3, 28, 51),
    ('Raphaël', 'Legrand', (SELECT id FROM university.users WHERE username = 'nmcgee'), 3, 28, 51),
    --B2
    ('Anna', 'Giraud', (SELECT id FROM university.users WHERE username = 'tbailey'), 3, 28, 52),
    ('Jules', 'Lefevre', (SELECT id FROM university.users WHERE username = 'hstrickland'), 3, 28, 52),
    ('Lou', 'Nicolas', (SELECT id FROM university.users WHERE username = 'kmcdowell'), 3, 28, 52),
    --Groupes C
    --1ère année
    --C1
    ('Théo', 'Rolland', (SELECT id FROM university.users WHERE username = 'cbowman'), 3, 29, 53),
    ('Léa', 'Gallet', (SELECT id FROM university.users WHERE username = 'jholland'), 3, 29, 53),
    ('Tom', 'Joly', (SELECT id FROM university.users WHERE username = 'ccarlson'), 3, 29, 53),
    --C2
    ('Chloé', 'Rousseau', (SELECT id FROM university.users WHERE username = 'kgriffith'), 3, 29, 54),
    ('Jade', 'Morin', (SELECT id FROM university.users WHERE username = 'smccormick'), 3, 29, 54),
    ('Noah', 'Leger', (SELECT id FROM university.users WHERE username = 'jnash'), 3, 29, 54),
    --2ème année
    --C1
    ('Louise', 'Remy', (SELECT id FROM university.users WHERE username = 'awalter'), 3, 30, 55),
    ('Lucas', 'Hebert', (SELECT id FROM university.users WHERE username = 'kmcmahon'), 3, 30, 55),
    ('Maëlys', 'Julien', (SELECT id FROM university.users WHERE username = 'hburns'), 3, 30, 55),
    --C2
    ('Gabriel', 'Prevost', (SELECT id FROM university.users WHERE username = 'jkirk'), 3, 30, 56),
    ('Lina', 'Renard', (SELECT id FROM university.users WHERE username = 'sstanton'), 3, 30, 56),
    ('Emma', 'Leclerc', (SELECT id FROM university.users WHERE username = 'abryan'), 3, 30, 56),
    --3ème année
    --C1
    ('Mathéo', 'Gerard', (SELECT id FROM university.users WHERE username = 'rbeard'), 3, 31, 57),
    ('Eva', 'Lebrun', (SELECT id FROM university.users WHERE username = 'mmccarty'), 3, 31, 57),
    ('Jules', 'Michel', (SELECT id FROM university.users WHERE username = 'jthornton'), 3, 31, 57),
    --C2
    ('Sarah', 'Faure', (SELECT id FROM university.users WHERE username = 'lpatrick'), 3, 31, 58),
    ('Louane', 'Fournier', (SELECT id FROM university.users WHERE username = 'mrandolph'), 3, 31, 58),
    ('Théo', 'Perrin', (SELECT id FROM university.users WHERE username = 'cwise'), 3, 31, 58),
    --Groupes App
    --2ème année
    ('Lou', 'Roy', (SELECT id FROM university.users WHERE username = 'nbranch'), 3, 32, 59),
    ('Liam', 'Mathieu', (SELECT id FROM university.users WHERE username = 'bthorpe'), 3, 32, 59),
    ('Elise', 'Caron', (SELECT id FROM university.users WHERE username = 'ewalsh'), 3, 32, 59),
    --3ème année
    ('Nathan', 'Masson', (SELECT id FROM university.users WHERE username = 'jmayer'), 3, 33, 60),
    ('Manon', 'Guerin', (SELECT id FROM university.users WHERE username = 'cgolden'), 3, 33, 60),
    ('Lucas', 'Julien', (SELECT id FROM university.users WHERE username = 'ahays'), 3, 33, 60),
    

    ---------------------------------
    --GACO
    ---------------------------------
    
    --Groupes A

    --1ère année
    --A1
    ('Juliett', 'Marchand', (SELECT id FROM university.users WHERE username = 'jcolon'), 4, 34, 61),
    ('Emma', 'Denis', (SELECT id FROM university.users WHERE username = 'dmcmillan'), 4, 34, 61),
    ('Arthur', 'Perrin', (SELECT id FROM university.users WHERE username = 'krocha'), 4, 34, 61),
    --A2
    ('Léa', 'Lambert', (SELECT id FROM university.users WHERE username = 'arosales'), 4, 34, 62),
    ('Hugo', 'Michel', (SELECT id FROM university.users WHERE username = 'jbarton'), 4, 34, 62),
    ('Camille', 'Renard', (SELECT id FROM university.users WHERE username = 'sswanson'), 4, 34, 62),
    --2ème année
    --A1
    ('Clara', 'Joly', (SELECT id FROM university.users WHERE username = 'hmccarthy'), 4, 35, 63),
    ('Ethan', 'Giraud', (SELECT id FROM university.users WHERE username = 'ebrock'), 4, 35, 63),
    ('Jade', 'Nicolas', (SELECT id FROM university.users WHERE username = 'dgould'), 4, 35, 63),
    --A2
    ('Noah', 'Renault', (SELECT id FROM university.users WHERE username = 'kblair'), 4, 35, 64),
    ('Zoé', 'Lucas', (SELECT id FROM university.users WHERE username = 'jtrujillo'), 4, 35, 64),
    ('Léo', 'Faure', (SELECT id FROM university.users WHERE username = 'rswanson'), 4, 35, 64),
    --3ème année
    --A1
    ('Emma', 'Lambert', (SELECT id FROM university.users WHERE username = 'mjennings2'), 4, 36, 65),
    ('Lucas', 'Bernard', (SELECT id FROM university.users WHERE username = 'rbates'), 4, 36, 65),
    ('Léa', 'Durand', (SELECT id FROM university.users WHERE username = 'cbeasley'), 4, 36, 65),
    --A2
    ('Théo', 'Thomas', (SELECT id FROM university.users WHERE username = 'lhorton'), 4, 36, 66),
    ('Maëlys', 'Robert', (SELECT id FROM university.users WHERE username = 'kshaffer'), 4, 36, 66),
    ('Noah', 'Richard', (SELECT id FROM university.users WHERE username = 'amccall'), 4, 36, 66),
    
    --Groupes B
    
    --1ère année
    --B1
    ('Lily', 'Petit', (SELECT id FROM university.users WHERE username = 'wtilley'), 4, 37, 67),
    ('Hugo', 'Moreau', (SELECT id FROM university.users WHERE username = 'pcasey'), 4, 37, 67),
    ('Lou', 'Simon', (SELECT id FROM university.users WHERE username = 'jhodge'), 4, 37, 67),
    --B2
    ('Gabriel', 'Laurent', (SELECT id FROM university.users WHERE username = 'blangley'), 4, 37, 68),
    ('Chloé', 'Lefevre', (SELECT id FROM university.users WHERE username = 'jzimmerman'), 4, 37, 68),
    ('Tom', 'Garcia', (SELECT id FROM university.users WHERE username = 'kmcmillan'), 4, 37, 68),
    --2ème année
    --B1
    ('Eva', 'Michel', (SELECT id FROM university.users WHERE username = 'cenglish'), 4, 38, 69),
    ('Lina', 'Rodriguez', (SELECT id FROM university.users WHERE username = 'jacobson'), 4, 38, 69),
    ('Raphaël', 'Martinez', (SELECT id FROM university.users WHERE username = 'rschmitt'), 4, 38, 69),
    --B2
    ('Léa', 'Boucher', (SELECT id FROM university.users WHERE username = 'cchristian'), 4, 38, 70),
    ('Ethan', 'Dupont', (SELECT id FROM university.users WHERE username = 'mbowman'), 4, 38, 70),
    ('Zoé', 'Lambert', (SELECT id FROM university.users WHERE username = 'jphelps'), 4, 38, 70),
    --3ème année
    --B1
    ('Louis', 'Bonnet', (SELECT id FROM university.users WHERE username = 'dbolton'), 4, 39, 71),
    ('Clara', 'Fernandez', (SELECT id FROM university.users WHERE username = 'lstein'), 4, 39, 71),
    ('Manon', 'Lemoine', (SELECT id FROM university.users WHERE username = 'ncase'), 4, 39, 71),
    --B2
    ('Nathan', 'Roussel', (SELECT id FROM university.users WHERE username = 'mbaker'), 4, 39, 72),
    ('Juliett', 'Girard', (SELECT id FROM university.users WHERE username = 'tsloan'), 4, 39, 72),
    ('Liam', 'Brun', (SELECT id FROM university.users WHERE username = 'jgoodman'), 4, 39, 72),
    
    --Groupes C
    
    --1ère année
    --C1
    ('Emma', 'Guillaume', (SELECT id FROM university.users WHERE username = 'ckinney'), 4, 40, 73),
    ('Jade', 'Lucas', (SELECT id FROM university.users WHERE username = 'ngriffith'), 4, 40, 73),
    ('Tom', 'Faure', (SELECT id FROM university.users WHERE username = 'jweaver'), 4, 40, 73),
    --C2
    ('Léa', 'Henry', (SELECT id FROM university.users WHERE username = 'tdudley'), 4, 40, 74),
    ('Noah', 'Robin', (SELECT id FROM university.users WHERE username = 'swilcox'), 4, 40, 74),
    ('Louise', 'Roux', (SELECT id FROM university.users WHERE username = 'rdalton'), 4, 40, 74),
    --2ème année
    --C1
    ('Gabriel', 'David', (SELECT id FROM university.users WHERE username = 'jwilliams'), 4, 41, 75),
    ('Chloé', 'Bertrand', (SELECT id FROM university.users WHERE username = 'bdalton'), 4, 41, 75),
    ('Théo', 'Perrin', (SELECT id FROM university.users WHERE username = 'sburnett'), 4, 41, 75),
    --C2
    ('Eva', 'Lambert', (SELECT id FROM university.users WHERE username = 'rmoran'), 4, 41, 76),
    ('Jules', 'Gauthier', (SELECT id FROM university.users WHERE username = 'lwright'), 4, 41, 76),
    ('Clara', 'Morel', (SELECT id FROM university.users WHERE username = 'astuart'), 4, 41, 76),
    --3ème année
    --C1
    ('Liam', 'Simon', (SELECT id FROM university.users WHERE username = 'kcarter'), 4, 42, 77),
    ('Emma', 'Caron', (SELECT id FROM university.users WHERE username = 'jkent'), 4, 42, 77),
    ('Louis', 'Lefevre', (SELECT id FROM university.users WHERE username = 'lshelton2'), 4, 42, 77),
    --C2
    ('Léa', 'Andre', (SELECT id FROM university.users WHERE username = 'cmelton'), 4, 42, 78),
    ('Noah', 'Fournier', (SELECT id FROM university.users WHERE username = 'jhenry'), 4, 42, 78),
    ('Jade', 'Vincent', (SELECT id FROM university.users WHERE username = 'kgreen'), 4, 42, 78),
    --Groupes App
    --2ème année
    ('Tom', 'Vidal', (SELECT id FROM university.users WHERE username = 'sford'), 4, 43, 79),
    ('Zoé', 'Henry', (SELECT id FROM university.users WHERE username = 'tschwartz'), 4, 43, 79),
    ('Hugo', 'Roussel', (SELECT id FROM university.users WHERE username = 'aparks'), 4, 43, 79),
    --3ème année
    ('Juliett', 'Lucas', (SELECT id FROM university.users WHERE username = 'dherman'), 4, 44, 80),
    ('Chloé', 'Philippe', (SELECT id FROM university.users WHERE username = 'mwiley'), 4, 44, 80),
    ('Raphaël', 'Renaud', (SELECT id FROM university.users WHERE username = 'jjordan'), 4, 44, 80)
;