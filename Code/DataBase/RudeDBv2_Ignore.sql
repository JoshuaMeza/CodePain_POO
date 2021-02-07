DROP TABLE IF EXISTS `Ignore`;

CREATE TABLE `Ignore` (
  `idIgnore` int NOT NULL AUTO_INCREMENT,
  `word` varchar(20) COLLATE utf8_bin NOT NULL,
  `guildIdIg` bigint NOT NULL,
  PRIMARY KEY (`idIgnore`),
  UNIQUE KEY `idIgnore_UNIQUE` (`idIgnore`),
  KEY `fk_Ignore_1_idx` (`guildIdIg`),
  CONSTRAINT `fk_Ignore_1` FOREIGN KEY (`guildIdIg`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `Ignore` VALUES (1,'GG',794783492197187587);
