DROP TABLE IF EXISTS `CustomWords`;

CREATE TABLE `CustomWords` (
  `wordId` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) COLLATE utf8_bin NOT NULL,
  `guildIdCW` bigint NOT NULL,
  PRIMARY KEY (`wordId`),
  UNIQUE KEY `wordId_UNIQUE` (`wordId`),
  KEY `fk_CustomWords_1_idx` (`guildIdCW`),
  CONSTRAINT `fk_CustomWords_1` FOREIGN KEY (`guildIdCW`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `CustomWords` VALUES (1,'Caca',794783492197187587);
