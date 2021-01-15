DROP TABLE IF EXISTS `Languages`;

CREATE TABLE `Languages` (
  `languageId` int NOT NULL AUTO_INCREMENT,
  `language` varchar(20) NOT NULL,
  PRIMARY KEY (`languageId`),
  UNIQUE KEY `idLanguage_UNIQUE` (`languageId`),
  UNIQUE KEY `language_UNIQUE` (`language`)
)

INSERT INTO `Languages` VALUES (1,'English'),(3,'Maya'),(2,'Spanish');
