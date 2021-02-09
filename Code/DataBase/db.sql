-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: RudeDBv2
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Bugs`
--

DROP TABLE IF EXISTS `Bugs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bugs` (
  `idBugs` int NOT NULL AUTO_INCREMENT,
  `Comment` text COLLATE utf8_bin NOT NULL,
  `idGuildBugs` bigint NOT NULL,
  PRIMARY KEY (`idBugs`),
  UNIQUE KEY `idBugs_UNIQUE` (`idBugs`),
  KEY `fk_Bugs_1_idx` (`idGuildBugs`),
  CONSTRAINT `fk_Bugs_1` FOREIGN KEY (`idGuildBugs`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bugs`
--

LOCK TABLES `Bugs` WRITE;
/*!40000 ALTER TABLE `Bugs` DISABLE KEYS */;
INSERT INTO `Bugs` VALUES (1,'Los requests no se mandan :(',794783492197187587),(3,'The request system does not send anything >:(',794783492197187587),(4,'Tengo problemas con esto!',794783492197187587),(5,'test',794783492197187587);
/*!40000 ALTER TABLE `Bugs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CustomWords`
--

DROP TABLE IF EXISTS `CustomWords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CustomWords` (
  `wordId` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) COLLATE utf8_bin NOT NULL,
  `guildIdCW` bigint NOT NULL,
  PRIMARY KEY (`wordId`),
  UNIQUE KEY `wordId_UNIQUE` (`wordId`),
  KEY `fk_CustomWords_1_idx` (`guildIdCW`),
  CONSTRAINT `fk_CustomWords_1` FOREIGN KEY (`guildIdCW`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CustomWords`
--

LOCK TABLES `CustomWords` WRITE;
/*!40000 ALTER TABLE `CustomWords` DISABLE KEYS */;
INSERT INTO `CustomWords` VALUES (1,'CACA',794783492197187587),(3,'GOLFA',794783492197187587);
/*!40000 ALTER TABLE `CustomWords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Guilds`
--

DROP TABLE IF EXISTS `Guilds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Guilds` (
  `idGuilds` bigint NOT NULL,
  `penalizeMode` tinyint NOT NULL,
  PRIMARY KEY (`idGuilds`),
  UNIQUE KEY `idGuilds_UNIQUE` (`idGuilds`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Guilds`
--

LOCK TABLES `Guilds` WRITE;
/*!40000 ALTER TABLE `Guilds` DISABLE KEYS */;
INSERT INTO `Guilds` VALUES (123,1),(794783492197187587,0);
/*!40000 ALTER TABLE `Guilds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ignore`
--

DROP TABLE IF EXISTS `Ignore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ignore` (
  `idIgnore` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) COLLATE utf8_bin NOT NULL,
  `guildIdIg` bigint NOT NULL,
  PRIMARY KEY (`idIgnore`),
  UNIQUE KEY `idIgnore_UNIQUE` (`idIgnore`),
  KEY `fk_Ignore_1_idx` (`guildIdIg`),
  CONSTRAINT `fk_Ignore_1` FOREIGN KEY (`guildIdIg`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ignore`
--

LOCK TABLES `Ignore` WRITE;
/*!40000 ALTER TABLE `Ignore` DISABLE KEYS */;
INSERT INTO `Ignore` VALUES (1,'GG',794783492197187587),(3,'CHIRRION',794783492197187587),(4,'CRAZY',794783492197187587);
/*!40000 ALTER TABLE `Ignore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Languages`
--

DROP TABLE IF EXISTS `Languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Languages` (
  `languageId` int NOT NULL AUTO_INCREMENT,
  `language` varchar(20) NOT NULL,
  PRIMARY KEY (`languageId`),
  UNIQUE KEY `idLanguage_UNIQUE` (`languageId`),
  UNIQUE KEY `language_UNIQUE` (`language`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Languages`
--

LOCK TABLES `Languages` WRITE;
/*!40000 ALTER TABLE `Languages` DISABLE KEYS */;
INSERT INTO `Languages` VALUES (1,'English'),(3,'Maya'),(2,'Spanish');
/*!40000 ALTER TABLE `Languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RequestedWords`
--

DROP TABLE IF EXISTS `RequestedWords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RequestedWords` (
  `wordId` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) NOT NULL,
  `languageId` int NOT NULL,
  PRIMARY KEY (`wordId`),
  UNIQUE KEY `wordId` (`wordId`),
  KEY `FK_RequestedWord` (`languageId`),
  CONSTRAINT `FK_RequestedWord` FOREIGN KEY (`languageId`) REFERENCES `Languages` (`languageId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RequestedWords`
--

LOCK TABLES `RequestedWords` WRITE;
/*!40000 ALTER TABLE `RequestedWords` DISABLE KEYS */;
INSERT INTO `RequestedWords` VALUES (6,'GORDA',2),(8,'TEST',1),(9,'TEST',3);
/*!40000 ALTER TABLE `RequestedWords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stories`
--

DROP TABLE IF EXISTS `Stories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Stories` (
  `idStories` int NOT NULL AUTO_INCREMENT,
  `userId` bigint NOT NULL,
  `warnings` int NOT NULL,
  `guildIdSty` bigint NOT NULL,
  PRIMARY KEY (`idStories`),
  UNIQUE KEY `idStories_UNIQUE` (`idStories`),
  KEY `fk_Stories_1_idx` (`guildIdSty`),
  CONSTRAINT `fk_Stories_1` FOREIGN KEY (`guildIdSty`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stories`
--

LOCK TABLES `Stories` WRITE;
/*!40000 ALTER TABLE `Stories` DISABLE KEYS */;
INSERT INTO `Stories` VALUES (1,123,0,794783492197187587),(2,321,0,794783492197187587),(3,1234,1,123),(12,572589109412102228,0,794783492197187587),(16,601094698949410826,0,794783492197187587);
/*!40000 ALTER TABLE `Stories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Whitelist`
--

DROP TABLE IF EXISTS `Whitelist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Whitelist` (
  `idWhitelist` int NOT NULL AUTO_INCREMENT,
  `idUser` bigint NOT NULL,
  `idGuild` bigint NOT NULL,
  PRIMARY KEY (`idWhitelist`),
  UNIQUE KEY `idWhitelist_UNIQUE` (`idWhitelist`),
  KEY `fk_Whitelist_1_idx` (`idGuild`),
  CONSTRAINT `fk_Whitelist_1` FOREIGN KEY (`idGuild`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Whitelist`
--

LOCK TABLES `Whitelist` WRITE;
/*!40000 ALTER TABLE `Whitelist` DISABLE KEYS */;
/*!40000 ALTER TABLE `Whitelist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Words`
--

DROP TABLE IF EXISTS `Words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Words` (
  `wordId` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) COLLATE utf8_bin NOT NULL,
  `languageID` int NOT NULL,
  PRIMARY KEY (`wordId`),
  UNIQUE KEY `word_UNIQUE` (`word`),
  UNIQUE KEY `wordId_UNIQUE` (`wordId`),
  KEY `FK_WordLanguage` (`languageID`),
  CONSTRAINT `FK_WordLanguage` FOREIGN KEY (`languageID`) REFERENCES `Languages` (`languageId`)
) ENGINE=InnoDB AUTO_INCREMENT=274 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Words`
--

LOCK TABLES `Words` WRITE;
/*!40000 ALTER TABLE `Words` DISABLE KEYS */;
INSERT INTO `Words` VALUES (1,'AHOLE',1),(2,'ANAL',1),(3,'ANUS',1),(4,'ARSE',1),(5,'ASHOLE',1),(6,'ASHOLES',1),(7,'ASS',1),(8,'ASSFACE',1),(9,'ASSHOLE',1),(10,'ASSHOLES',1),(11,'ASSWIPE',1),(12,'BALLS',1),(13,'BALLSACK',1),(14,'BASTARD',1),(15,'BASTARDS',1),(16,'BITCH',1),(17,'BITCHES',1),(18,'BLOODY',1),(19,'BLOWJOB',1),(20,'BOLLOCK',1),(21,'BONER',1),(22,'BOOB',1),(23,'BUGGER',1),(24,'BUM',1),(25,'BUTT',1),(26,'BUTTHOLE',1),(27,'BUTTPLUG',1),(28,'CLIT',1),(29,'CLITORIS',1),(30,'COCK',1),(31,'COCK-HEAD',1),(32,'COCKHEAD',1),(33,'COON',1),(34,'CRAMPIE',1),(35,'CRAP',1),(36,'CUM',1),(37,'CUNT',1),(38,'DAMN',1),(39,'DICK',1),(40,'DICKHEAD',1),(41,'DILDO',1),(42,'DYKE',1),(43,'FACK',1),(44,'FACKER',1),(45,'FACKING',1),(46,'FAG',1),(47,'FAGGOT',1),(48,'FELCHING',1),(49,'FELLATE',1),(50,'FELLATIO',1),(51,'FLANGE',1),(52,'FUCK',1),(53,'FUCKER',1),(54,'FUCKING',1),(55,'FUDGEPACKER',1),(56,'GAY',1),(57,'GAYBOY',1),(58,'GODDAMN',1),(59,'HELL',1),(60,'JERK',1),(61,'JERKS',1),(62,'JIZZ',1),(63,'KNOBEND',1),(64,'LABIA',1),(65,'LMAO',1),(66,'LMFAO',1),(67,'MASTURBATE',1),(68,'MILF',1),(69,'MOTHERFUCKER',1),(70,'MUFF',1),(71,'NIBBA',1),(72,'N1GGA',1),(73,'NIGGER',1),(74,'NUDES',1),(75,'ORGASM',1),(76,'PENIS',1),(77,'PISS',1),(78,'POOP',1),(79,'PORN',1),(80,'PRICK',1),(81,'PUBE',1),(82,'PUSSY',1),(83,'QUEER',1),(84,'RAPE',1),(85,'RAPING',1),(86,'RETARD',1),(87,'SCROTUM',1),(88,'SENSUAL',1),(89,'SEX',1),(90,'SEXY',1),(91,'SHIT',1),(92,'SHITTY',1),(93,'SHITY',1),(94,'SLUT',1),(95,'SMEGMA',1),(96,'SPUNK',1),(97,'TESTICLE',1),(98,'TIT',1),(99,'TITIES',1),(100,'TITTIES',1),(101,'TOSSER',1),(102,'TURD',1),(103,'TWAT',1),(104,'VAGINA',1),(105,'WANK',1),(106,'WHORE',1),(107,'XXX',1),(108,'CULEABLE',2),(109,'ABRAZAFAROLAS',2),(110,'ADEFECIO',2),(111,'AGUEVADO',2),(112,'ALCORNOQUE',2),(113,'ALIMANIA',2),(114,'ANO',2),(115,'ASESINAR',2),(116,'ASESINEN',2),(117,'BABOSA',2),(118,'BABOSO',2),(119,'BOBA',2),(120,'BOBO',2),(121,'BOCAZAS',2),(122,'BUBIES',2),(123,'CABRON',2),(124,'CACHONDA',2),(125,'CAGADA',2),(126,'CAGAS',2),(127,'CAGASTE',2),(128,'CAGON',2),(129,'CAGUETAS',2),(130,'CALIENTAHUEVOS',2),(131,'CARACULO',2),(132,'CARAFLEMA',2),(133,'CARAPIJA',2),(134,'CHINGADA',2),(135,'CHINGADO',2),(136,'CHINGAQUEDITO',2),(137,'CHINGAR',2),(138,'CHINGAS',2),(139,'CHINGO',2),(140,'CHINGON',2),(141,'CHUPAME',2),(142,'CHUPAPIJAS',2),(143,'CIPOLLO',2),(144,'CIPOTE',2),(145,'COGER',2),(146,'COJAN',2),(147,'CONIO',2),(148,'CRETINA',2),(149,'CRETINO',2),(150,'CTM',2),(151,'CTRM',2),(152,'CULO',2),(153,'DESMADRE',2),(154,'ENCABRONADA',2),(155,'ENCABRONADO',2),(156,'ENCABRONAR',2),(157,'ENCABRONAS',2),(158,'ENCABRONASTE',2),(159,'ENPUTADA',2),(160,'ENPUTADO',2),(161,'ESTUPIDA',2),(162,'ESTUPIDO',2),(163,'FREGADA',2),(164,'FREGADO',2),(165,'GIL',2),(166,'GILIPOLLA',2),(167,'GILIPOLLAS',2),(168,'GONORREA',2),(169,'GUEVON',2),(170,'HDTPM',2),(171,'HIJUEPUTA',2),(172,'HUEVON',2),(173,'IDIOTA',2),(174,'IJUEPUTA',2),(175,'IMBECIL',2),(176,'JALAPIJA',2),(177,'JALAPIJAS',2),(178,'JIL',2),(179,'JODER',2),(180,'JODES',2),(181,'JOTO',2),(182,'JUEPUTA',2),(183,'LAMECULOS',2),(184,'LAMEME',2),(185,'LESBIANA',2),(186,'LESBICO',2),(187,'MALANDRO',2),(188,'MALANDRA',2),(189,'MALCRIADA',2),(190,'MALCRIADO',2),(191,'MALNACIDO',2),(192,'MALNACIDA',2),(193,'MALPARIDA',2),(194,'MALPARIDO',2),(195,'MAMADA',2),(196,'MAMADAS',2),(197,'MAMADOR',2),(198,'MAMANDO',2),(199,'MAMON',2),(200,'MARRANADA',2),(201,'MATAR',2),(202,'MATEN',2),(203,'MIARDA',2),(204,'MIERDA',2),(205,'MOJON',2),(206,'OJETE',2),(207,'PAJA',2),(208,'PAJERO',2),(209,'PANOCHA',2),(210,'PAPANATAS',2),(211,'PATAN',2),(212,'PENDEJA',2),(213,'PENDEJO',2),(214,'PENE',2),(215,'PENES',2),(216,'PERRA',2),(217,'PEZON',2),(218,'PEZONES',2),(219,'PICHA',2),(220,'PICHACORTA',2),(221,'PICHAFLOJA',2),(222,'PICHAFRIA',2),(223,'PICHAS',2),(224,'PINCHE',2),(225,'PINCHES',2),(226,'PIJA',2),(227,'POLLA',2),(228,'PORNO',2),(229,'PUTA',2),(230,'PUTO',2),(231,'SARNA',2),(232,'SARNOZA',2),(233,'SARNOZO',2),(234,'SECUESTREN',2),(235,'SECUESTRAR',2),(236,'SECUESTRE',2),(237,'SEXO',2),(238,'SIDOSO',2),(239,'SONSA',2),(240,'SONSO',2),(241,'SOPLAPOLLAS',2),(242,'SPM',2),(243,'TARADO',2),(244,'TESTICULOS',2),(245,'TETA',2),(246,'TETAS',2),(247,'TONTA',2),(248,'TONTO',2),(249,'TULA',2),(250,'TULAS',2),(251,'VAGINAS',2),(252,'VEGESTORIO',2),(253,'VENUDO',2),(254,'VERGA',2),(255,'VERGUDO',2),(256,'VIOLAR',2),(257,'VIOLE',2),(258,'VIOLEN',2),(259,'VOLUDO',2),(260,'BOLUDO',2),(261,'WEPUTA',2),(262,'WEPUTO',2),(263,'ZOQUETE',2),(264,'ZORRA',2),(265,'ZURULLO',2),(266,'CHOMANA',3),(267,'HUIRO',3),(268,'KAKBACH',3),(269,'PELANA',3),(270,'PIRIX',3),(271,'TA',3),(272,'GOLFA',2),(273,'ZORRO',2);
/*!40000 ALTER TABLE `Words` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-07 16:16:22
