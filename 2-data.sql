-- MariaDB dump 10.19-11.2.2-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	11.2.2-MariaDB-1:11.2.2+maria~ubu2204

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

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
(16,'E13','daniel craig','assets/puzzles/sky_craie.png');
/*!40000 ALTER TABLE `puzzles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `puzzles_hints`
--

LOCK TABLES `puzzles_hints` WRITE;
/*!40000 ALTER TABLE `puzzles_hints` DISABLE KEYS */;
INSERT INTO `puzzles_hints` VALUES
(1,'E1',1,'assets/puzzles/haie.png','E2'),
(2,'E1',2,'assets/puzzles/haie.png','E11'),
(3,'E1',3,'assets/puzzles/haie.png','E3'),
(20,'E13',1,'assets/puzzles/leo.png','E10'),
(4,'E3',1,'Mon second est une qualité dont Damien et Captain auraient bien besoin','E2'),
(5,'E3',2,'Mon tout est une chanson d\'un collectif qui a buzzé fort en 2020','E11'),
(6,'E4',1,'Gislain prend sa tondeuse','E13'),
(7,'E4',2,'Et part arracher des roseaux','E5'),
(8,'E4',3,'Sur la route, il fait la connaissance de 4 vielles et moches femmes.','E7'),
(9,'E5',1,'Mon tout est le prénom de quelqu\'un que vous connaissez','E8'),
(11,'E6',1,'Alcool','E2'),
(12,'E6',2,'Fort','E13'),
(13,'E6',3,'crazy tiger','E6'),
(14,'E7',1,'assets/puzzles/bouteille.png','E5'),
(15,'E7',2,'Prenom','E3'),
(16,'E8',1,'Son du canard','E10'),
(17,'E9',1,'Bien que partiellement composé de cuire, je broute mais pas de la chatte','E10'),
(18,'E9',2,'Pour fonctionner j\'ai besoin qu\'on me remplisse','E8'),
(19,'E9',3,'Je suis inofensif sauf quand Fuf\' me pilote','E7');
/*!40000 ALTER TABLE `puzzles_hints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES
(3,'Rouge','danger','2024-03-15 21:04:52'),
(4,'Vert','success','2024-03-15 21:04:59');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(2,'test0','123','Test 0','Rouge','None','2024-03-15 21:05:14'),
(3,'test1','123','Test 1','Vert','None','2024-03-15 21:05:26');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-15 21:34:56
