-- MariaDB dump 10.19-11.0.2-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	11.0.2-MariaDB-1:11.0.2+maria~ubu2204

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `disabled_pages`
--

LOCK TABLES `disabled_pages` WRITE;
/*!40000 ALTER TABLE `disabled_pages` DISABLE KEYS */;
INSERT INTO `disabled_pages` VALUES
('Game');
/*!40000 ALTER TABLE `disabled_pages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `menus`
--

LOCK TABLES `menus` WRITE;
/*!40000 ALTER TABLE `menus` DISABLE KEYS */;
INSERT INTO `menus` VALUES
(1 , 'Mercredi' , 'Soir' , 'Chacun sa merde'        , '')      ,
(2 , 'Jeudi'    , 'Midi' , 'No sé'                  , '')      ,
(3 , 'Jeudi'    , 'Soir' , "Menu de l'équipe Orange" , 'Orange') ,
(4 , 'Vendredi' , 'Midi' , 'No sé'                  , '')      ,
(5 , 'Vendredi' , 'Soir' , "Menu de l'équipe Verte" , 'Vert')  ,
(6 , 'Samedi'   , 'Midi' , 'No sé'                  , '')      ,
(7 , 'Samedi'   , 'Soir' , "Menu de l'équipe Rose" , 'Rose')  ;

/*!40000 ALTER TABLE `menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `puzzles`
--

LOCK TABLES `puzzles` WRITE;
/*!40000 ALTER TABLE `puzzles` DISABLE KEYS */;
INSERT INTO `puzzles` VALUES
(3,'E1','héhéhé|hé hé hé','Je suis le mantra d\'un membre du Siphlard'),
(4,'E2 ','picon bière|pcb','assets/puzzles/rebu_p2.png'),
(5,'E3','Bande organisée','Mon 1er est l\'inverse du surnom d\'Emile'),
(6,'E4','La Rirette','assets/puzzles/musique.jpg'),
(7,'E5','Salomé','assets/puzzles/equation.png'),
(8,'E6','Jägermeister|jagermeister','assets/puzzles/police.jpg'),
(9,'E7','Jack Daniel\'s|Jack Daniels','assets/puzzles/celebrites.png'),
(11,'E8','bitcoin','assets/puzzles/bc.png'),
(12,'E9','tracteur|le tracteur','Je me fait monter quand le temps est clément'),
(13,'E10','pissenlit','assets/puzzles/mignon.png'),
(14,'E11','léchez moi le cul','assets/puzzles/leche.png'),
(15,'E12','jouir sur ses fesses','assets/puzzles/maroc.png'),
(16,'E13','daniel craig','assets/puzzles/sky_craie.png'),
(17,'E14','5',"Combiens de pourbelles ont elles été empilées sur le camion lors du premier colloc de la communauté d'Enduirduill"),
(18,'E15','andromede','assets/puzzles/ed.png');
/*!40000 ALTER TABLE `puzzles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `puzzles_hints`
--

LOCK TABLES `puzzles_hints` WRITE;
/*!40000 ALTER TABLE `puzzles_hints` DISABLE KEYS */;
INSERT INTO `puzzles_hints` VALUES
(1  , 'E1'  , 1 , 'assets/puzzles/haie.png'                                                  , 'E2')  ,
(2  , 'E1'  , 2 , 'assets/puzzles/haie.png'                                                  , 'E11') ,
(3  , 'E1'  , 3 , 'assets/puzzles/haie.png'                                                  , 'E3')  ,
(4  , 'E3'  , 1 , 'Mon second est une qualité dont Damien et Captain auraient bien besoin'   , 'E2')  ,
(5  , 'E3'  , 2 , "Mon tout est une chanson d'un collectif qui a buzzé fort en 2020"         , 'E11') ,
(6  , 'E4'  , 1 , 'Gislain prend sa tondeuse'                                                , 'E13') ,
(7  , 'E4'  , 2 , 'Et part arracher des roseaux'                                             , 'E5')  ,
(8  , 'E4'  , 3 , 'Sur la route, il fait la connaissance de 4 vielles et moches femmes.'     , 'E7')  ,
(9  , 'E5'  , 1 , "Mon tout est le prénom de quelqu'un que vous connaissez"                  , 'E8')  ,
(11 , 'E6'  , 1 , 'Alcool'                                                                   , 'E2')  ,
(12 , 'E6'  , 2 , 'Fort'                                                                     , 'E13') ,
(13 , 'E6'  , 3 , 'crazy tiger'                                                              , 'E13') ,
(14 , 'E7'  , 1 , 'assets/puzzles/bouteille.png'                                             , 'E5')  ,
(15 , 'E7'  , 2 , 'Prenom'                                                                   , 'E3')  ,
(16 , 'E8'  , 1 , 'Son du canard'                                                            , 'E10') ,
(17 , 'E9'  , 1 , 'Bien que partiellement composé de cuire, je broute mais pas de la chatte' , 'E10') ,
(18 , 'E9'  , 2 , "Pour fonctionner j'ai besoin qu'on me remplisse"                          , 'E8')  ,
(19 , 'E9'  , 3 , 'Je suis inofensif sauf quand Fuf me pilote'                               , 'E7')  ,
(20 , 'E14' , 1 , '<Coordonées de <ette enigme>'                                             , 'E4')  ,
(21 , 'E13' , 1 , 'assets/puzzles/leo.png'                                                   , 'E10') ,
(22 , 'E15' , 1 , 'Constellation'                                                            , 'E7')  ;
/*!40000 ALTER TABLE `puzzles_hints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES
(1 , 'Mercredi' , '08:00 -> 17:00' , 'Arrivées')                ,
(2 , 'Mercredi' , '19:00'          , 'Soirée')                  ,
(3 , 'Jeudi'    , '14:00'          , 'Jeu de piste par équipe') ,
(5 , 'Jeudi'    , '20:30'          , 'Mini jeux') ,
(6 , 'Vendredi' , '14:00'          , 'Activitée au choix (paintball | OGliss | OFun)')                   ,
(7 , 'Vendredi' , '21:00'          , 'Soirée théme Jungle, venez préparé !')                   ,
(8 , 'Samedi'   , '14:00'          , 'Plage'),
(9 , 'Samedi'   , '20:00'          , 'Jeux inventés par les équipes'),
(10, 'Dimanche' , '08:00'          , 'Rangement');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES
(3,'Orange','danger','2024-03-15 21:04:52'),
(4,'Vert','success','2024-03-15 21:04:59'),
(5,'Rose','primary','2024-04-08 07:47:04');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--


LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(4  , 'admin'   , 'hehehe'                , NULL      , NULL    , NULL   , '2024-03-29 19:53:07') ,
(5  , 'paul'    , TO_BASE64('paul')    , 'Vin rouge porte'  , 'Orange' , 'paul.png' , '2024-04-08 07:48:08') ,
(6  , 'bosh'    , TO_BASE64('bosh')    , 'Dodo buisson'    , 'Vert'  , 'bosh.png' , '2024-04-08 07:48:08') ,
(7  , 'yohan'   , TO_BASE64('yohan')   , 'Mr. Jul'   , 'Rose'  , 'yoyo.png' , '2024-04-08 07:48:08') ,
(8  , 'lucas'   , TO_BASE64('lucas')   , 'Rond point'   , 'Rose'  , 'lucas.png' , '2024-04-08 07:48:08') ,
(9  , 'alois'   , TO_BASE64('alois')   , 'Le gros geekos'   , 'Orange' , 'alois.png' , '2024-04-08 07:48:08') ,
(10 , 'dodo'    , TO_BASE64('dodo')    , 'Le tonton bof'    , 'Vert'  , 'dorian.png' , '2024-04-08 07:48:08') ,
(11 , 'fuf'     , TO_BASE64('fuf')     , 'Best blowjob of Budapest'     , 'Rose'  , 'fuf.png' , '2024-04-08 07:48:08') ,
(12 , 'léo'     , TO_BASE64('léo')     , 'Vomi manège (et ça pue)'     , 'Orange' , 'leo.png' , '2024-04-08 07:48:08') ,
(13 , 'maria'   , TO_BASE64('maria')   , 'Scooby-Doo'   , 'Rose'  , 'maria.png' , '2024-04-08 07:48:08') ,
(14 , 'mimole'  , TO_BASE64('mimole')  , 'Lundi dernier'  , 'Rose'  , 'mimole.png' , '2024-04-08 07:48:08') ,
(15 , 'francis' , TO_BASE64('francis') , 'Téma la taille du rat' , 'Vert'  , 'maele.png' , '2024-04-08 07:48:08') ,
(16 , 'glenn'   , TO_BASE64('glenn')   , 'Le curé'   , 'Orange' , 'glenn.png' , '2024-04-08 07:48:08') ,
(17 , 'sn'      , TO_BASE64('sn')      , 'Pleins de petits cailloux'      , 'Orange' , 'sn.png' , '2024-04-08 07:48:08') ,
(18 , 'solène'  , TO_BASE64('solène')  , 'Pas de jean sur le lit'  , 'Vert'  , 'soso.png' , '2024-04-08 07:48:08') ,
(19 , 'claire'  , TO_BASE64('claire')  , 'Poups2000'  , 'Rose'  , 'poups.png' , '2024-04-08 07:48:08') ,
(21 , 'dj'      , TO_BASE64('dj')      , 'Le vitrier raciste'      , 'Vert'  , 'didjo.png' , '2024-04-08 07:48:08') ,
(22 , 'captain' , TO_BASE64('captain') , "Simooooooooon T'AS PEUR" , 'Rose'  , 'captain.png' , '2024-04-08 07:48:08') ,
(23 , 'greg'    , TO_BASE64('greg')    , "L'électricien"    , 'Vert'  , 'greg.png' , '2024-04-08 07:48:08') ,
(24 , 'camille' , TO_BASE64('camille') , 'MAIS NON ?!?! *frappe cuisse*' , 'Orange' , 'camille.png' , '2024-04-08 07:48:08') ,
(25 , 'al'      , TO_BASE64('al')      , 'Vomi terrasse'      , 'Vert'  , 'alicia.png' , '2024-04-08 07:48:08') ,
(26 , 'sas'     , TO_BASE64('sas')     , 'PLS Boom Halloween (très tôt)'     , 'Orange' , 'sas.png' , '2024-04-08 07:48:08') ,
(27 , 'nathan'  , TO_BASE64('nathan')  , 'Caca UCPA'  , 'Vert'  , 'nath.png' , '2024-04-08 07:48:08') ,
(28 , 'sarah'   , TO_BASE64('sarah')   , 'Lit rouge'   , 'Rose'  , 'sarha.png' , '2024-04-08 07:48:08') ,
(29 , 'manon'   , TO_BASE64('manon')   , 'Galette de boyaux sur beton armé'   , 'Vert'  , 'manon.png' , '2024-04-08 07:48:08') ,
(30 , 'justin'  , TO_BASE64('justin')  , 'Lavabaise'  , 'Orange' , 'justin.png' , '2024-04-08 07:48:08') ,
(31 , 'damien'  , TO_BASE64('damien')  , 'Le sportif alcoolique'  , 'Orange' , 'damien.png' , '2024-04-08 07:48:08') ,
(32 , 'hugo'    , TO_BASE64('hugo')    , 'Papi'    , 'Rose'  , 'hugo.png' , '2024-04-08 07:48:08') ;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

LOCK TABLES `pronos` WRITE;
INSERT INTO `pronos` VALUES
(0, 'gagnant', 'paul,bosh,yohan,lucas,alois,dodo,fuf,léo,maria,mimole,francis,glenn,sn,solène,claire,dj,captain,greg,camille,al,sas,nathan,sarah,manon,justin,damien,hugo', 'Grand gagnant de la Gerbouilette')
;
UNLOCK TABLES;
-- Dump completed on 2024-04-08  7:52:09
