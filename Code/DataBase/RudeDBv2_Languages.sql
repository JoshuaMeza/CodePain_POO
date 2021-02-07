DROP TABLE IF EXISTS `Languages`;

CREATE TABLE `Languages` (
  `languageId` int NOT NULL AUTO_INCREMENT,
  `language` varchar(20) NOT NULL,
  PRIMARY KEY (`languageId`),
  UNIQUE KEY `idLanguage_UNIQUE` (`languageId`),
  UNIQUE KEY `language_UNIQUE` (`language`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `Languages` VALUES (1,'English'),(3,'Mayan'),(2,'Spanish');
