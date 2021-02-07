DROP TABLE IF EXISTS `RequestedWords`;

CREATE TABLE `RequestedWords` (
  `wordId` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) NOT NULL,
  `languageId` int NOT NULL,
  PRIMARY KEY (`wordId`),
  UNIQUE KEY `wordId` (`wordId`),
  KEY `FK_RequestedWord` (`languageId`),
  CONSTRAINT `FK_RequestedWord` FOREIGN KEY (`languageId`) REFERENCES `Languages` (`languageId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
